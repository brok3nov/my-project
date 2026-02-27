import random

# Это мой первый простой проект на Python с использованием модуля random
# Чтобы почувствовать сам проект, лучше не читать его как код, а запустить и поиграть)

enemies = ["Орк", "Дракон", "Слайм"]
heros_path_chest = ["Меч", "Артефакт", "Броня"]
chect = ["100 серебрянных монет", "200 серебрянных монет", "300 серебрянных монет"]

while True:

    user_damage = random.randint(10, 50)
    user_luck = random.uniform(1.1, 1.5)
    user_enemies = random.choice(enemies)
    critical_hit = random.randrange(35, 100, 5)

    try:

        print("Привет дружище, хочешь поиграть в игру ? Чтобы выйти напишите \"Выход\"")
        user_game = input("Введите ответ (да/нет): ").lower()

        if user_game in ["не хочу", "нет", "неа"]:
            print("Понял тебя! сыграем в другой раз")
            break

        elif user_game in ["хочу", "да", "давай", "конечно"]:
            print("---ИГРА ГЕРОЙ РАНДОМНЫХ ЧИСЕЛ---")

            nick = input("Введите свой ник: ")

            print(f"Итак {nick}, ты готов пройти путь героя, тебе на пути могут", end=" ")
            print("встретиться монстры! Ты к этому готов ?")

            answer = input("Введите ответ (да/нет): ").lower()

            if answer in ["не хочу", "нет", "неа"]:
                print("Раз то что ты отказался пройти путь георя я дам тебе только утешительнй приз!")
                
                user_chect = input("Открой сундук с призом (открыть): ").lower()
                
                if user_chect == "открыть":
                    print(f"Тебе выпало - {random.choice(chect)} !")
                    print("До следующей игры, пока !")
                    break

                else:
                    print("Напиши - \"Открыть\"")

            elif answer in ["хочу", "да", "давай", "конечно"]:
                print("Отлично! я знал, что ты очень храбрый, начинает наш путь")

                print("О нет, вот и первый враг который нам стретился", end=", ")
                print(f"это кровожадный {user_enemies}")

                i = 3

                while i > 0:

                    attack = input(f"Ударь {user_enemies}! На удар у тебя всего {i}")

                    if attack in ["ударить", "атаковать", "удар", "атака"]:

                        if critical_hit == 95 or critical_hit == 100:
                            user_damage = user_damage * 2
                            print(f"Молодец, ты нанес крит. удар {user_enemies}, твой урон - {user_damage}")

                            print(f"{user_enemies} повержен, тебя ждет твоя награда!")
                            print(f"В качестве награды за настоящий путь героя тебе выпало - {random.sample(heros_path_chest, 2)}")

                            gold = 100 * user_luck
                            print(f"Бонусом получаешь - {round(gold)} золотых!")

                            print("Спасибо за то, что поиграл в мою игру, заходи еще, пока !")
                            break
                            
                        else:
                            print(f"Молодец, ты нанес удар {user_enemies}, твой урон - {user_damage}")

                            print(f"{user_enemies} повержен, тебя ждет твоя награда!")
                            print(f"В качестве награды за настоящий путь героя тебе выпало - {random.sample(heros_path_chest, 2)}")

                            gold = 100 * user_luck
                            print(f"Бонусом получаешь - {round(gold)} золотых!")
                            
                            print("Спастбо за то, что поиграл в мою игру, заходи еще, пока !")
                            break

                    else:
                        i = i - 1
                        print(f"Ты не ударил {user_enemies}! Осталось всего {i} попыток!")

                    if i == 0:
                        print("Ты проиграл эту игру. Попробуй в следующий раз!")
                        break

                break

            else:
                print("Ответь нормально - да или нет")

        print("Конец моей мини игры. Большое спасибо за внимание!")

    except ValueError as e:
        print(f"Что-то пошло не так, возникла ошибка - {e}")