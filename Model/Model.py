import csv
import pathlib
from pathlib import Path
from Controller.CreateNewRecord import createNewRecord


def addNewRecord():
    record_id = idLastRow() + 1
    f = open(Path(pathlib.Path.cwd(), 'Data', 'DataBase.csv'), 'a')
    f.write(f'{record_id},{createNewRecord()}\n')
    f.close()

def readData():
    data = []
    f = open(Path(pathlib.Path.cwd(), 'Data', 'DataBase.csv'), 'r')
    for line in f.read().split('\n'):
        element = line.strip().split(',')
        final_element = []
        if len(line) > 0:
            for member in element:
                cleared_member = member.strip()
                final_element.append(cleared_member)
            data.append(final_element)
    f.close()
    return data

def rewriteData(newRecords):
    f = open(Path(pathlib.Path.cwd(), 'Data', 'DataBase.csv'), 'w', newline='')
    writer = csv.writer(f)
    writer.writerows(newRecords)
    f.close()

def idLastRow():
    data = readData()
    if len(data) == 0:
        return 0
    return int(data[-1][0])

def showAll():
    return readData()

def sortDateASC():
    return sorted(readData(), key=lambda p: (p[4]))

def sortDateDESC():
    return sorted(readData(), key=lambda p: (p[4]), reverse=True)

def sortCostASC():
    return sorted(readData(), key=lambda p: (float(p[3])))

def sortCostDESC():
    return sorted(readData(), key=lambda p: (float(p[3])), reverse=True)

def selectDate(dateBuy):
    data = readData()
    selectData = list()
    for record in data:
        if record[4] == dateBuy:
            selectData.append(record)
    return selectData

def selectCategory(category):
    data = readData()
    selectData = list()
    for record in data:
        if record[1] == category:
            selectData.append(record)
    return selectData


def deleteItem(index):
    flag = 3
    data = readData()
    buffer = list()
    for record in data:
        if record[0] == index:
            confirm = input('Вы действительно хотите удалить запись? [y/n]')
            if confirm.lower() == 'y':
                for record in data:
                    if record[0] != index:
                        buffer.append(record)
                rewriteData(buffer)
                flag = 1
            else:
                flag = 2
    return flag

def checkingNumber(int):
    flag = 4
    if int.isdigit():
        flag = deleteItem(int)
    return flag