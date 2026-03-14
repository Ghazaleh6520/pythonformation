nombres = range(5)
nombres_double = [i * 2 for i in nombres]

print(nombres_double)

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]

print(nombres_inverses)