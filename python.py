try:    

    print("привет как дела от 1 до 10?")
    user = int(input("введите ответ: "))

    if user > 7 and user > 0:
        print("ооо, рад что у тебя все хорошо!")

    elif user > 4 and user > 0:
        print("блин, не хорошо конечно, но скоро все наладиться")

    elif user >= 2 and user > 0:
        print("соболезную, но ты держись")

    else:
        print("ответь нормально!")

    print("конец программы")

except:
    print("попробуйте ввести цифры")