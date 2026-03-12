# Проект - rtm(random, time module)

import random
import time
one_time = time.time()
hour, two_min, sek = 0

blows = ["вертушка", "апперкот", "джеб", "хук"]
attempt = 3
hp_user = 100
hp_enemy = 100

print("Привет, хочешь сыграть в игру ?")

try:
    
    time.sleep(0.2)
    play_a_game = input("Введите ответ(да/нет): ").lower().strip()


    if play_a_game in ["да", "давай", "хочу"]:
        time.sleep(0.3)
        print("-" * 30)
        data_one = "Игра - бокс"
        for cycle in data_one:
            print(cycle, end="", flush=True)
            time.sleep(0.1)

        d = "-" * 30
        print(f"\n{d}")

        while attempt > 0:
            damage_user = random.randint(10, 40)
            damage_enemy = random.randint(5, 40)
            rand_blows = random.choice(blows)
            crit = random.random()

            time.sleep(0.3)
            user_hit = input("Введите слово - удар, чтобы нанести урон сопернику: ").lower().strip()

            if user_hit == "удар":
                if crit > 0.70:
                    damage_user = damage_user * 2
                    hp_enemy = hp_enemy - damage_user
                    print(f"Вы нанесли удар {rand_blows}, он отнял у соперника {damage_user} хп, у соперника осталось {max(hp_enemy, 0)} здоровья")

                else:
                    hp_enemy = hp_enemy - damage_user
                    time.sleep(0.3)
                    print(f"Вы нанесли удар {rand_blows}, он отнял у соперника {damage_user} хп, у соперника осталось {max(hp_enemy, 0)} здоровья")

                if hp_enemy <= 0:
                    data_three = f"Ты нанес {rand_blows} и победил, у врага кончилось здоровье"
                    for cycle_three in data_three:
                        print(cycle_three, end="", flush=True)
                        time.sleep(0.1)

                    two_time = time.time()
                    result = two_time - one_time
                    one_min, sek = divmod(int(result), 60)
                    hour, two_min = divmod(one_min, 60)

                    data_for = f"\nИтого время программы - {hour:02d}:{two_min:02d}:{sek:02d}\n"
                    for cycle_for in data_for:
                        print(cycle_for, end="", flush=True)
                        time.sleep(0.1)

                    break

                elif hp_enemy > 0:
                    hp_user = hp_user - damage_enemy
                    time.sleep(0.3)
                    print(f"Соперник нанес удар на {damage_enemy} урона", end=", ")
                    print(f"у тебя осталось {max(hp_user, 0)} здоровья")

                    if hp_user <= 0:
                        data_five = "Ты проиграл! У тебя не осталось здоровья, попробуй в следующий раз"
                        for cycle_five in data_five:
                            print(cycle_five, end="", flush=True)
                            time.sleep(0.1)

                        two_time = time.time()

                        result = two_time - one_time
                        one_min, sek = divmod(int(result), 60)
                        hour, two_min = divmod(one_min, 60)

                        data_six = f"\nИтого время программы - {hour:02d}:{two_min:02d}:{sek:02d}\n"
                        for cycle_six in data_six:
                            print(cycle_six, end="", flush=True)
                            time.sleep(0.1)

                        break

            else:
                attempt -= 1
                print(f"У тебя осталось {attempt} попыток")

    elif play_a_game in ["нет", "неа", "не", "не хочу"]:
        time.sleep(0.3)
        print("Понял, сыграем в следующий раз")

    else:
        print("Ответь мне по шаблону - да или нет")

    if attempt < 1:
        print("-" * 30)
        data_seven = "Ты проиграл, твои попытки закончились"
        for cycle_seven in data_seven:
            print(cycle_seven, end="", flush=True)
            time.sleep(0.1)

        d_two = "-" * 30
        print(f"\n{d_two}")

        two_time = time.time()

        result = two_time - one_time
        one_min, sek = divmod(int(result), 60)
        hour, two_min = divmod(one_min, 60)

        data_eight = f"\nИтого время программы - {hour:02d}:{two_min:02d}:{sek:02d}\n"
        for cycle_eight in data_eight:
            print(cycle_eight, end="", flush=True)
            time.sleep(0.1)

    if play_a_game in ["да", "давай", "хочу"]:
        with open("Время игры.txt", "w", encoding="utf-8") as file:
            file.write(f"Итого время программы - {hour:02d}:{two_min:02d}:{sek:02d}")

except ValueError as e:
    print(f"Что-то пошло не так, возникла ошибка - {e}")

# Прошу строго не судить, это один из моих первых проектов