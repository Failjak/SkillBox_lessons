# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('Dad')
my_family.insert(0, "Brother")
my_family.append('Mum')

for person in my_family:
    print(person)
print(my_family)

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Nikita', 177],
    ['Ilya', 155],
    ['Alex', 183],
    ["Yulia", 155]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца - ", my_family_height[2][1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
hight = 0
for h in my_family_height:
    hight =hight + h[1]
print("Общий рсот моей семьи - ", hight, 'см')