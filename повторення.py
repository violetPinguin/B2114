# вивести всі непарні числа в діапазоні від до
number1 = int(input("enter value from:"))
number2 = int(input("enter value to:"))

for i in range(number1, number2+1 ):
    if i%2 == 1:
        print(i)