
messages = {
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move..."
}

while True:
    operations = ['+', '-', '/', '*']
    print(messages[0])
    calc = input()
    calc = calc.split(' ')
    x = calc[0]
    y = calc[2]
    oper = calc[1]
    try:
        float(x)
        float(y)
        if oper in operations:
          break
    except ValueError:
        print(messages[1])

    try:
      if oper not in operations:
        raise ValueError('oper is not in operations')
    except ValueError:
      print(message[2])
    