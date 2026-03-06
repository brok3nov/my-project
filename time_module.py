# простой проект с использованием модуля time

import time
final_time = "00:00:00"

try:
    print("Привет, у тебя есть два режима на выбор")

    time.sleep(0.3)
    print("1 - секундомер, засекает время, чтобы его остановить", end=" ")
    print("нужно просто нажать Ctrl + C")

    time.sleep(0.3)
    print("2 - функция обратного отчета, ты вводишь цифру, а она считает от нее до нуля")

    time.sleep(0.2)
    print("Какую функцию выбираешь ?")

    try:
        time.sleep(0.3)
        function_user = int(input("Введите ответ(1/2): "))

        if function_user == 1:
            time.sleep(0.3)
            print("Секундомер запущен, введие Ctrl + C чтобы остановить")
            one_time = time.time()

            while True:
                time.sleep(0.1)

                two_time = time.time()
                result = two_time - one_time

                minut, sek = divmod(int(result), 60)
                hour, total_min = divmod(minut, 60)

                final_time = f"Итоговое время: {hour:02d}:{total_min:02d}:{sek:02d}"
                print(final_time, end="\r", flush=True)

        elif function_user == 2:
            time.sleep(0.3)
            user_number = int(input("Введите число: "))
            
            for cycle in range(user_number, 0, -1):
                print(f"Резултьтат: {cycle:02d}", end="\r")
                time.sleep(1)

            print("-" * 30)
            print("Конец отчета")
                
    except ValueError as e:
        time.sleep(0.3)
        print(f"Попробуй ввести число, возникла ошибка - {e}")

except KeyboardInterrupt:
    time.sleep(0.3)
    print("\nПрограмма остановлена")
    print(final_time)