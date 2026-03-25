def somarTodos(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(somarTodos(1,2,3))
print(somarTodos(10,20,30,40,50))
print(somarTodos())