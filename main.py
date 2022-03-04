from random import randint
from datetime import datetime

attempts = int(input('Введите количество попыток: '))
name = input('Введите свое имя: ')

start = datetime.now()

i = 1

while i < attempts:
    try:
        a = randint(1, 9)
        b = randint(1, 9)
        result = a * b
        i = i + 1
        answer = int(input( f'{a} * {b}: '))
        print(result)
    except:
        print("Вводите только числа!")
        i -= 1
        continue
    with open('results.txt', 'a', encoding="utf-8") as file:
        if result == answer:
            file.write(f"\n{a} * {b} = {answer} ({result}) правильно ")
        elif result != answer:
            file.write(f"\n{a} * {b} = {answer} ({result}) не правильно")
    if i >= attempts:
        print("количество попыток закончино!")
        print(f"потрачена время {datetime.now() - start}")
        with open('results.txt', 'a', encoding="utf-8") as file:
            file.write(f" \nбыло {i} попыток, потрачено время: {datetime.now() - start} секунд, имя: {name.title()}")
        break
