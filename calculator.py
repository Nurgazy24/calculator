
while True:
    a = input("Введите 'exit' для выхода из программы\nВведите ЗНАК ('+','-','*','/'): ")
    
    if a == "EXIT": break
    elif a == "Exit": break
    elif a == "exit": break
    elif a == "УЧШЕ": break
    elif a == "Учше": break
    elif a == "учше": break
     
    num1 = int(input("Введите число 1: "))
    num2 = int(input("Введите число 2: "))

    if a == "+":
        print(num1, "+", num2, "=", num1+num2)
    elif a == "-":
        print(num1, "+", num2, "=", num1-num2)
    elif a == "*":
        print(num1, "*", num2, "=", num1*num2)
    elif a == "/":
        if num2 != 0:
            print(num1, "/", num2, "=", num1/num2)
        else:
            print("Ошибка деления на ноль!!!")
    else:
        print("Неверный знак!!!")
 