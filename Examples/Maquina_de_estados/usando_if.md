

1) Condicion uno es verdadera y dos falso
    a. -> a
    b. -> a
    c. -> a

2) Uno false y dos verdadero
    a. -> b
    b. -> b
    c. -> b


3) Uno verdadero y dos verdadero
    a. -> a
    b. -> ab
    c. -> a

a)
if uno:
    print("a")
    pass
else:
    print("b")
    pass

b)
if uno:
    print("a")
    pass

if dos:
    print("b")
    pass

c)
if uno:
    print("a")
    pass
elif dos:
    print("b")
    pass
else:
    print("c")
    pass