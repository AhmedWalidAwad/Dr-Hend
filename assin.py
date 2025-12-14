print("=" * 60)
print("Question 1: Transform and Clean Data")
print("=" * 60)


products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "]
print(f"Original products: {products}")

cleaned_products = list(map(lambda x: x.strip().title(), products))
print(f"Cleaned products: {cleaned_products}")

print("\n" + "=" * 60)
print("Question 2: Convert Temperatures (Celsius → Fahrenheit)")
print("=" * 60)

celsius = [0, 10, 20, 30, 40]
print(f"Celsius: {celsius}")

fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius))
print(f"Fahrenheit: {fahrenheit}")

print("\n" + "=" * 60)
print("Question 3: Apply Multiple Transformations")
print("=" * 60)

nums = [1, 2, 3, 4, 5]
print(f"Original numbers: {nums}")


result = list(map(lambda x: x**2 + 10, nums))
print(f"Squared + 10: {result}")

print("\n" + "=" * 60)
print("Question 4: Extract First and Last Characters")
print("=" * 60)

words = ["python", "lambda", "programming", "map", "function"]
print(f"Words: {words}")

first_last = list(map(lambda w: (w[0], w[-1]), words))
print(f"First and last characters: {first_last}")

print("\n" + "=" * 60)
print("Question 5: Nested Map Transformation (Challenge)")
print("=" * 60)

marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
print("Original marks:")
for row in marks:
    print(row)


increased_marks = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print("\nMarks after 5% increase:")
for row in increased_marks:
    print(row)

print("\n" + "=" * 60)
print("Question 6: Normalize Numbers Between 0 and 1")
print("=" * 60)

numbers = [10, 20, 30, 40, 50]
print(f"Original numbers: {numbers}")

min_val = min(numbers)
max_val = max(numbers)
print(f"Min: {min_val}, Max: {max_val}")


normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), numbers))
print(f"Normalized (0-1): {normalized}")

print("\n" + "=" * 60)
print("Question 7: Extract Length of Each Word in Sentences")
print("=" * 60)

sentences = [
    "Python is awesome",
    "Lambda functions are powerful",
    "Map makes coding easier"
]
print("Original sentences:")
for sentence in sentences:
    print(f"  - {sentence}")


word_lengths = list(map(lambda sentence: list(map(lambda word: len(word), sentence.split())), sentences))
print("\nWord lengths in each sentence:")
for i, lengths in enumerate(word_lengths):
    print(f"  Sentence {i+1}: {lengths}")

print("\n" + "=" * 60)
print("All questions solved successfully! ✓")
print("=" * 60)

