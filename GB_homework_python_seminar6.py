'''
Домашняя работа. Семинар 6.

Задача 34.
Даны два файла в каждом из которых находится запись многочлена. 
Сформировать файл содержащий сумму многочленов.
'''

'''
def work_with_file(name_file):
    data = open(name_file, "r")
    result = data.readline()
    data.close()
    return result

def decomposition_formula(formula):
    new_formula = ""
    if formula[-2] == "=":
        formula = formula[:-2]
    if formula[-1].isdigit:
        formula += "*x**0"
    for i in range(len(formula)):
        if i > 0 and formula[i] == "-":
            new_formula += "+"
            new_formula += formula[i]
        elif formula[i] == "x":
            if formula[i - 1] != "*":
                new_formula += "1*"
            new_formula += formula[i]
            if formula[i + 1] != "*":
                new_formula += "**1"
        else:
            new_formula += formula[i]
    formula_list = list(new_formula.split("+"))
    new_formula_list = [list(map(int, c.split(
                             "*x**"))) for c in formula_list]
    # print(formula_list)
    formula = "".join(formula_list)
    # print(new_formula_list)
    return new_formula_list

def sum_dec_lists(arg_list1, arg_list2):
    for char in arg_list1:
        for c in arg_list2:
            if char[1] == c[1]:
                char[0] = char[0] + c[0]
                arg_list2.remove(c)
    arg_list1 += arg_list2
    # print(arg_list1)
    return arg_list1

def sort_list(arg_list):
    for i in range(len(arg_list) - 1):
        for j in range(1, len(arg_list)):
            if arg_list[j] < arg_list[j - 1]:
                arg_list[j], arg_list[j-1] = arg_list[j-1], arg_list[j]
    return arg_list

def assemble_formula(arg_list):
    result = ""
    for i in range(len(arg_list)):
        if arg_list[i][0] == 1: arg_list[i][0] = ""
        if arg_list[i][0] == -1: arg_list[i][0] = "-"
        if arg_list[i][1] == 0:
            arg_list[i] = str(arg_list[i][0])
        elif arg_list[i][1] == 1:
            if arg_list[i][0] == "" or arg_list[i][0] == "-":
                arg_list[i] = "x**".join(map(str, arg_list[i]))
            else:
                arg_list[i] = str(arg_list[i][0]) + "*x"
        else:
            if arg_list[i][0] == "" or arg_list[i][0] == "-":
                arg_list[i] = "x**".join(map(str, arg_list[i]))
            else:
                arg_list[i] = "*x**".join(map(str, arg_list[i]))
    # print(arg_list)
    for c in arg_list:
        if c[0] == "-":
            result += c
        else:
            result += ("+" + c)
    result += "=0"
    return result

print("\nВзять из указанных файлов по одной формуле и сложить их")
name_file1 = "task32_file1.txt"
print("Имя первого файла:", name_file1)
file_input1 = work_with_file(name_file1)
print("Фармула из первого файла:\n"
      f"{file_input1}")
# print(type(file_input1))

name_file2 = "task32_file2.txt"
print("Имя второго файла:", name_file2)
file_input2 = work_with_file(name_file2)
print("Формула из второго файла:\n"
      f"{file_input2}")
# print(type(file_input2))

dec_list1 = decomposition_formula(file_input1)
dec_list2 = decomposition_formula(file_input2)
# print(dec_list1)
# print(dec_list2)
sum_list = sum_dec_lists(dec_list1, dec_list2)
# print(sum_list)
sort_sum_list = sort_list(sum_list)
# print(sort_sum_list)
result_assemble_formula = assemble_formula(sort_sum_list)
print("Результат сложения двух многочленов:\n"
      f"{result_assemble_foremula}")
'''

'''
Задача 39.
Помните игру с конфетами из модуля "Математика и Информатика"? 
Создайте такую игру для игры человек против человека
a. Добавьте игру против бота
b. Подумайте как наделить бота "интеллектом"
'''

'''
import random

def player_move(arg_candies):
    print(f"Конфет в куче {arg_candies}")
    player_moves = int(input("Возьмите конфеты но "
                             "не больше 28:\n"))
    if player_moves > 28:
        print("\nТак, кто то не умеет считать\n"
              "нужно было взять не больше 28 конфет, "
              f"а вы взяли {player_moves}\n"
              "на этом игра окончена")
        return
    arg_candies -= player_moves
    return arg_candies

def computer_move(arg_candies):
    print(f"Конфет в куче {arg_candies}")
    if arg_candies < 30:
        temp_num = arg_candies - 1
        arg_candies -= temp_num
        print(f"Компьютер взял {temp_num} конфет")
        return arg_candies
    elif arg_candies != 30 and arg_candies < 58:
        temp_num = arg_candies - 30
        arg_candies -= temp_num
        print(f"Компьютер взял {temp_num} конфет")
        return arg_candies
    else:
        temp_num = random.randint(1, 28)
        arg_candies -= temp_num
        print(f"Компьютер взял {temp_num} конфет")
        return arg_candies

def moves(arg_candies):
    count = 0
    while arg_candies > 0:
        count += 1
        num_player = int(count % 2 == 0) + 1
        print(f"Ходит игрок номер {num_player}")
        arg_candies = player_move(arg_candies)
        if arg_candies == None: return
    num_win = int(not(count % 2 == 0)) + 1
    return num_win

def moves_comp_player(arg_candies):
    print("Хорошо, вы играете с компьютером")
    num = int(input("Выберете кто будит ходить первым\n"
                    "если вы введите 1\n"
                    "если компьютер введите 2\n"))
    while arg_candies > 0:
        if num == 1:
            print("Ходит игрок")
            arg_candies = player_move(arg_candies)
            if arg_candies == None: return
            if arg_candies < 1: return "Победил компьютер"
            print("Ходит компьютер")
            arg_candies = computer_move(arg_candies)
            if arg_candies < 1: return "Победил игрок"
        else:
            print("Ходит компьютер")
            arg_candies = computer_move(arg_candies)
            if arg_candies < 1: return "Победил игрок"
            print("Ходит игрок")
            arg_candies = player_move(arg_candies)
            if arg_candies == None: return
            if arg_candies < 1: return "Победил компьютер"

def main():
    print("\nДавайте сыграем в игру про жадность и конфеты\n"
          "Кто последний заберёт конфеты тот проиграл")
    num_candies = int(input("Напишите сколько всего в начале "
                            "игры конфет: "))
    if num_candies < 1:
        print("\nНевозможно победить в игре про конфеты, которых нет\n"
              "Но если нет победителя, то нет и проигравшего\n"
              "В любом случае игра окончена")
        return
    select_player = int(input(
                        "\nЕсли вы хотите играть с компьютером "
                        "введите 0\n"
                        "Если вы хотите играть с человеком "
                        "введите 1\n"
                        "С кем сыграете?\n"))
    if select_player == 1:
        result_game = moves(num_candies)
        if result_game == None: return
        print("Победил игрок {0}".format(result_game))
    else:
        result_game = moves_comp_player(num_candies)
        print(result_game)

main()
'''

'''
Задача 42.
Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления 
данных.
a. входные и выходные данные хранятся в отдельных текстовых файлах
'''

'''
def encoding(arg_data):
    result = []
    count = 1
    flag = arg_data[0] == arg_data[1]
    for i in range(1, len(arg_data)):
        temp = arg_data[i - 1]
        if (arg_data[i] == arg_data[i - 1]) == flag:
            count += 1
            temp += arg_data[i]
        else:
            result.append(count)
            result.append(arg_data[i - 1])
            count = 1
            temp = arg_data[i]
    result.append(count)
    result.append(arg_data[i])
    return result
'''

def encoding(arg_data):
    temp_list = []
    count = 0
    result_str = ""
    flag = True # arg_data[0] == arg_data[1]
    for i in range(len(arg_data) - 1):
        if (arg_data[i] == arg_data[i+1]):
            temp_list.append(arg_data[i])
        else:
            temp_list.append(arg_data[i])
            temp_list.append(";")
    if arg_data[-1] == arg_data[-2]:
        temp_list.append(arg_data[-1])
    else:
        temp_list.append(":")
        temp_list.append(arg_data[-1])
    new_str = "".join(temp_list)
    temp_list = new_str.split(";")
    new_str = ""
    temp_str = ""
    for i in range(len(temp_list)):
        if len(temp_list[i]) == 1:
            count = count - 1
            temp_str += temp_list[i]
        else:
            if count < 0:
                result_str = result_str + str(count) + temp_str
                count = 0
                temp_str = ""
            result_str = (result_str + "+" + 
                          str(len(temp_list[i])) +
                          temp_list[i][0])
    
    return result_str

data_input = "111111111111111111222222222222222222"
print(encoding(data_input))
data_input = "WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
print(encoding(data_input))
data_input = "ABCABCABCDDDFFFFFF"
print(encoding(data_input))

# encoding(data_input)
