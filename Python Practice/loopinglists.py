colors = ['blue', 'green', 'red', 'orange', 'yellow']

print("My favorite colors are: ")
for color in colors:
    print(color.title())
print()
print("My favorite numbers are: ")
for num in range(0,6):
    print(num)
print()
numbers = list(range(0,6))
print(numbers)
print()
squares = []
for value in range(0,11):
    square = value ** 2
    squares.append(square)
print(squares)
print()
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()
squares = [value**2 for value in range(0,11)]
print(squares)

