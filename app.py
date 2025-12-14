from pathlib import Path
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

# To install deps: pip install flask
# Run: python app.py

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "app.db"

app = Flask(__name__)
app.secret_key = "change-me"  # replace in production


def init_db() -> None:
    """Create the SQLite database and users table if they do not exist."""
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
    finally:
        conn.close()


def insert_user(username: str, password: str) -> tuple[bool, str]:
    """Insert a user row; return (success, message)."""
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username.strip(), password),
        )
        conn.commit()
        return True, "تم الحفظ بنجاح"
    except sqlite3.IntegrityError:
        return False, "اسم المستخدم موجود بالفعل"
    except Exception as exc:  # pragma: no cover - simple demo app
        return False, f"خطأ: {exc}"
    finally:
        conn.close()


def fetch_users() -> list[tuple]:
    """Return all saved users (id, username, created_at)."""
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, username, created_at FROM users ORDER BY created_at DESC"
        )
        return cur.fetchall()
    finally:
        conn.close()


@app.route("/", methods=["GET", "POST"])
def register():
    """Render the form and handle submissions."""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            flash("يجب إدخال اسم المستخدم وكلمة المرور", "error")
            return redirect(url_for("register"))

        success, message = insert_user(username, password)
        flash(message, "success" if success else "error")
        return redirect(url_for("register"))

    users = fetch_users()
    return render_template("form.html", users=users)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
