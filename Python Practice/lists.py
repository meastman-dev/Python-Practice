colors = ['blue', 'red', 'green']
print(colors)
print(colors[0])
print(colors[0].title())
print(colors[-1])
message = f"My favorite color is {colors[0].title()}"
print(message)

colors[0] = 'yellow'
print(colors)

colors.append('orange')
print(colors)

colors.insert(0, 'magenta')
print(colors)

del colors[0]
print(colors)

popped_color = colors.pop()
print(colors)
print(popped_color)

colors.sort()
print(colors)

colors.reverse()
print(colors)
print(len(colors))

