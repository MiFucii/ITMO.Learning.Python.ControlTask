from View.View import *
import Model.Model as mod


def sortedMenu():
    while (True):
        showMenuSort()
        valueMenu = input('Введите номер меню: ')
        if valueMenu == "1":
            showAllObject(mod.sortCostASC())
        elif valueMenu == "2":
            showAllObject(mod.sortCostDESC())
        elif valueMenu == "3":
            showAllObject(mod.sortDateASC())
        elif valueMenu == "4":
            showAllObject(mod.sortDateDESC())
        elif valueMenu == "5":
            break