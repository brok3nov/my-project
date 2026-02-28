import random

options = ["камень", "ножницы", "бумага"]

print("-----КАМЕНЬ, НОЖНИЦЫ, БУМАГА-----", end=" ")
print("чтобы выйти введите \"выход\"")


while True:

    try:

        x = random.choice(options)

        print("загадй вариант которым будешь бить !")
        user = input("введите ответ: ").lower()

        if user == "выход" or user == "выйти":
            print("выход осуществлен")
            break

        else:
            
            if user not in options:
                print("введите нормальный вариант ответа(камень, ножницы, бумага)")

            else:

                if user == x:
                    print(f"ничья, компьютер тоже выбрал - {x}")
                    
                elif user == "камень" and x == "ножницы":
                    print(f"ты победил! компьютер загадал {x}, а ты {user}")
                    break

                elif user == "ножницы" and x == "бумага":
                    print(f"ты победил! компьютер загадал {x}, а ты {user}")
                    break

                elif user == "бумага" and x == "камень":
                    print(f"ты победил! компьютер загадал {x}, а ты {user}")
                    break

                else:
                    print(f"ты проиграл, компьютер выбрал {x}, а ты {user}")

        print("конец программы!", end=" ")
        print("спасибо за внимание")

    except ValueError as e:
        print(f"что то пошло не так! сработала ошибка - {e}")