# вивести всі непарні числа в діапазоні від до
'''
number1 = int(input("enter value from:"))
number2 = int(input("enter value to:"))
for i in range(number1, number2+1 ):
    if i%2 == 1:
        print(i)
'''

# вводити кольори світлофора, поки не буде зелений
'''
color = input("Enter red green yellow:")
while color != "green":
    if color == "red":
        print("red - stop")
    elif color == "yellow":
        print("yellow - wait")
    else:
        print("error")
    color = input("Enter red green yellow:")
print("green - go")
'''

'''Створіть програму калькулятор: програма повинна пропонувати по черзі ввести два числа (а, b), далі, користувачу необхідно вказати математичну дію,
 яку необхідно виконати з цими числами (+, -, *, /). Отриманий результат треба вивести на екран комп'ютера. Однак, якщо b=0 і вказується дія — ділення (/), 
 то в цьому випадку програма повинна виводити підказку: «Ділення на нуль».'''

def culculator(x1, x2, op):
    if op == "+":
        print("result = ",x1 + x2)
    elif op == "-":
        print("result = ", x1 - x2)
    elif op == "*":
        print("result = ", x1 * x2)
    elif op == "/":
        if x2 == 0:
            print("Ділення на нуль")
        else:
            print("result = ", x1 / x2)
    else:
        print("error")

a = float(input("enter number1:"))
b = float(input("enter number1:"))
operation = input("Enter operation (+, -, *, /)")

culculator(a, b, operation)
