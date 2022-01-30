msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"

running = True
memory = 0
while running:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split()

    try:
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    valid_oper = "+-*/"
    if oper not in valid_oper:
        print(msg_2)
        continue

    result = 0
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        if y == 0.0:
            print(msg_3)
            continue
        else:
            result = x / y

    print(result)

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_4)
        answer = input()
        if answer == "y":
            memory = result

    answer = ""
    while answer != "y" and answer != "n":
        print(msg_5)
        answer = input()
        if answer == "n":
            running = False
