# -*- coding: utf-8 -*-

# Модуль — это файл, содержащий определения и выражения на Python. 
# Именем файла является имя модуля с добавленным суффиксом .py
# Так распространяется код пайтона - его библиотеки - в простейшем случае

# Что бы иметь доступ к коду модуля из другого модуля надо его импортировать
import module_1_ass

# Это действие НЕ переводит имена определённых в модуле переменных в текущее пространство имен,
# в нем появляется лишь имя модуля  - module_1. Используя его вы можете получить доступ к коду:

import module_1_ass
print(module_1_ass.variable_1)
module_1_ass.function1()

# По факту module_1 - это переменная, указывающая на модуль
# С помощью dir() можно получить список имен, определенных в модуле
import module_1_ass
print(dir(module_1_ass))

###
# При импорте выполняются все операторы python. Если в модуле есть что-то,
# кроме определения переменных и функция (в будущем - классов),
# то этот код выполнится

import module_2


###
# Внутри модуля, имя модуля (в качестве строки) доступно
# в виде значения глобальной переменной с именем __name__.

import module_2

# Когда вы запускаете модуль Python из командной строки
# > python module_3.py
# то код в этом модуле будет исполнен в момент его импортирования,
# но значение __name__ будет установлено как "__main__".
# Это значит, что добавляя этот код в конец сценария:

if __name__ == "__main__":
    print("Меня вызвали!")

# вы можете сделать возможным запуск файла и в качестве сценария и в качестве импортируемого модуля

