import json
import importlib


def process(key, parameters=None):
    # Альфа версия хранения и вызова функций по её названию и модулю
    # мы можем хранить и вызывать функции по его текстовому имени используя рефлексию,
    # например функция выключить находится в модуле "moduls.Shutdown",
    # мы можем сохранит в json файл или легковесную БД название модуля, название функции
    # и набор ключевых слов которые вызывают определяют эту функцию,
    with open("functions.json", "r") as read_file:
        data = json.load(read_file)

    funct = data[key]
    if not funct is None:
        # при вызове этой функции мы определяем её по строке используя importlib
        module = importlib.import_module("moduls.{0}".format(funct['module']))
        # затем используя системный метод getAttr мы получаем эту функцию по строке
        f = getattr(module, funct['function'])
        if parameters:
            # и просто вызываем её передавая параметры
            f(parameters)
        else:
            f()
    else:
        print("Function {0} not found".format(key))
