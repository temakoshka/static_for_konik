from datetime import datetime


def letter_to_str(input_str, time_str):

    if not time_str:
        time_str = datetime.now().strftime('%H:%M')
    char_map = {
        'w': 'Woman',
        'm': 'Man',
        'h': 'Home customer',
        'n': 'New client',
        'f': 'Foreigner',
        's': 'Slovak'
    }
    result = []
    for char in input_str.lower():
        if char in char_map:
            result.append(char_map[char])

    # Формируем финальную строку
    client_info = ', '.join(result)
    final_str = f"Klient: {client_info}, Cas: {time_str}"

    return final_str


def take_info():
    while True:
        input_string = input("Info about client: ").strip()
        input_time = input("Time: ").strip()
        output_str = letter_to_str(input_string, input_time)
        count_of_group = 1
        if input_string[0].isdigit():
            count_of_group = int(input_string[0])
        with open('static_who_goes_to_konik.txt', 'a') as file:
            for i in range(count_of_group):
                file.write(f"{output_str}\n")


def take_static_of_time():
    file_for_stats = 'static_who_goes_to_konik.txt'
    cast_at_hours = []

    try:
        with open(file_for_stats, 'r') as file:
            for line in file:
                start = line.find('Cas:')
                if start != -1:
                    hour = int(line[start + 5:start + 7])
                    cast_at_hours.append(hour)
    except FileNotFoundError:
        print(f"Файл {file_for_stats} не найден.")

    return cast_at_hours


def take_static():
    file_for_stats = 'static_who_goes_to_konik.txt'
    with open(file_for_stats, 'r') as file:
        content = file.read()
        count_of_people = content.count('Klient')
        count_of_men, count_of_women = content.count(
            'Man'), content.count('Woman')
        count_of_home, count_of_new = content.count(
            'Home'), content.count('New')
        count_of_slovak, count_of_foreigner = content.count(
            'Slovak'), content.count('Foreigner')
    profit_today = int(input('Enter your profit today:'))
    average_bill = round(profit_today / count_of_people, 2)
    cast_at_hours = take_static_of_time()

    with open('days_static.txt', 'a') as file:
        current_day = datetime.now().strftime('%A')
        file.write(f'\n')
        file.write(f'{current_day}\n')
        file.write(f'Total clients: {count_of_people}\n')
        file.write(f'Total profit: {profit_today} EUR\n')
        file.write(f'Average bill: {average_bill} EUR\n')
        file.write(f'Men: {count_of_men} ({round(count_of_men/count_of_people * 100, 2)}%)\n')
        file.write(f'Women: {count_of_women} ({round(count_of_women/count_of_people * 100, 2)}%)\n')
        file.write(f'Home customers: {count_of_home} ({round(count_of_home/count_of_people * 100, 2)}%)\n')
        file.write(f'New customers: {count_of_new} ({round(count_of_new/count_of_people * 100, 2)}%)\n')
        file.write(f'Slovak: {count_of_slovak} ({round(count_of_slovak/count_of_people * 100, 2)}%)\n')
        file.write(f'Foreigner: {count_of_foreigner} ({round(count_of_foreigner/count_of_people * 100, 2)}%)\n')
        file.write(f'\n')
        if current_day == "Sunday" or current_day == "Saturday":
            for i in range(15, 24):  
                file.write(f'At {i}:00 were {cast_at_hours.count(i)} customers\n')
        else:
            for i in range(11, 24):  
                file.write(f'At {i}:00 were {cast_at_hours.count(i)} customers\n')
        file.write('\n')


# c - for start counting, s - for stats today, e - end the day
take_command = input("Welcome, let's try your best! Enter a command: ")
if take_command == 'c':
    take_info()
elif take_command == 's':
    take_static()
elif take_command == 'e':
    with open('static_who_goes_to_konik.txt', 'w') as file:
        file.write('')
