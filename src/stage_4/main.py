logo = """
 _____________________
|  _________________  |
| | Bea_PyCalc  0.  | | 
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| |
| | . | 0 | = | | / | | 
| |___|___|___| |___| |
|_____________________|
"""
print(logo)


def is_one_digit(v):
    return v % 1 == 0 and -10 < v < 10
    

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if v3 == "*" and (v1 == 1 or v2 == 1):
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 != "/"):
        msg += msg_8

    if msg:
        msg = msg_9 + msg
        print(msg)

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"


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

    check(x, y, oper)

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