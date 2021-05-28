x = 42
# y = "The answer is {}, {}"
y = "The answer is"
message = "Well Done!"
# z = y + str(x)
# z = y.format(x, message)
z = f"{y} {x}, {message} {6 * 9}"
print(z)