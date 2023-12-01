expresiones = [
    not False, 
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True * 5 == 2.5*2 or 123>=23,
    12 > 7 and True < False #true es 1 y false es 0
]

resultados : [
    True,
    True,
    True,
    True,
    True,
    False
]

print(bool(33/3==11))
