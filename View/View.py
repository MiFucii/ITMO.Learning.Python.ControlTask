def showMenu():
    print("\n-------------------------------------\n"
          "                 Меню\n"
          "-------------------------------------\n"
          "1>|           Добавить            |<1\n"
          "2>|         Показать все          |<2\n"
          "3>|   Показать по выбранной дате  |<3\n"
          "4>|Показать по выбранной категории|<4\n"
          "5>|       Сортировать по...       |<5\n"
          "6>|         Удалить запись        |<6\n"
          "0>|             Выход             |<0\n")

def showMenuSort():
    print("\n------------------------------------------\n"
          "            Меню сортировки\n"
          "------------------------------------------\n"
          "1>|Сортировать по возрастанию стоимости|<1\n"
          "2>|  Сортировать по убыванию стоимости |<2\n"
          "3>|   Сортировать по возрастанию даты  |<3\n"
          "4>|    Сортировать по убыванию даты    |<4\n"
          "5>|                Назад               |<5\n")

def formatText(text):
    string = text
    if len(text) < 4:
        string += '\t\t\t\t\t'
    elif len(text) < 8:
        string += '\t\t\t\t'
    elif len(text) < 12:
        string += '\t\t\t'
    elif len(text) < 16:
        string += '\t\t'
    elif len(text) < 20:
        string += '\t'
    return string

def stringAssembly(iSub):
    string = formatText(iSub[1])
    string +=formatText(iSub[2])
    string +=formatText(iSub[3])
    string +=formatText(iSub[4])
    return string

def showTable(text, data):
    print(text, '\nN\tКатегория  \t\t\tНазвание  \t\t\tЦена  \t\t\t\tДата')
    for iSub in data:
        print(iSub[0], '\t', stringAssembly(iSub), sep="")


def showAllObject(data):
    showTable('\n - - - - ->  Список трат', data)


def showObjectByDate(data, date):
    print(f'\n - - - - ->  Список трат за {date}:')
    if len(data) == 0:
        print(f'Трат за {date} не найдено')
    else:
        showTable('', data)


def showObjectByCategory(data, category):
    print(f'\n - - - - ->  Список трат по категории {category}:')
    if len(data) == 0:
        print(f'Трат в категории {category} не найдено')
    else:
        showTable('', data)

def showDelete(flag, index):
    if flag == 1:
        print('\nЭлемент успешно удален!')
    elif flag == 2:
        print('Изменения отменены!')
    elif flag == 3:
        print(f'Элемент с номером {index} не найден!')
    elif flag == 4:
        print('Ошибка ввода значения!')