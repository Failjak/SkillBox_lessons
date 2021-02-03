# -*- coding: utf-8 -*-

from room_1 import folks as folks_1
from room_2 import folks as folks_2

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...


def names(folks):
    for name in folks:
        if name == folks[-1]:
            print(name, end='.')
        else:
            print(name, end=', ')


print('In the room_1 living:', end=' ')
names(folks_1)

print('\nIn the room_2 living:', end=' ')
names(folks_2)


