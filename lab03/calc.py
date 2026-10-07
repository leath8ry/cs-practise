def add(a, b):
    return a + b

def mns_add(a, b):
    return a - b

def prod(a, b):
    return a * b

if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *): ")
    
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = mns_add(num1, num2)
    elif operation == "*":
        result = prod(num1, num2)
    else:
        print("Неизвестная операция")
    
    print(f"Результат: {result}")
