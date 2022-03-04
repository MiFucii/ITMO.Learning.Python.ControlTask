from View.View import *
import Model.Model as mod
from Controller.SortedController import sortedMenu


def main():
    while (True):
        showMenu()
        valueMenu = input('Введите номер меню: ')
        if valueMenu == "1":
            mod.addNewRecord()
        elif valueMenu == "2":
            showAllObject(mod.showAll())
        elif valueMenu == "3":
            date = input('Введите дату: ')
            showObjectByDate(mod.selectDate(date), date)
        elif valueMenu == "4":
            category = input('Введите категорию: ')
            showObjectByCategory(mod.selectCategory(category), category)
        elif valueMenu == "5":
            sortedMenu()
        elif valueMenu == "6":
            index = input('Введите номер удаляемой записи: ')
            showDelete(mod.checkingNumber(index), index)
        elif valueMenu == "0":
            break