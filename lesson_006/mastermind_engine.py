#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
import random
from copy import copy


def guess_num():
    num_str = str(random.randint(1000, 9999))
    num_list_int = list(map(lambda x: int(x), num_str))
    return num_list_int


def check(num_list, our_list):
    cow_count = bull_count = 0
    for i in range(len(num_list)):
        if num_list[i] is our_list[i]:
            bull_count += 1
        else:
            cow_count += 1
    return bull_count, cow_count
    # return {'bulls': bull_count, 'cows': cow_count}

"""
После первой провеки, даже если нулевое, добавляем 1 к ind и если чет поменялось запоминаем его в нужный нам индекс.
И соотв удаляем его из nun и our.
И так до len(num) > 0
"""
def search(num_list, our_num):
    while len(num_list) > 0:
        print('это resault в начале {}'.format(resault_num))
        counters = check(num_list, our_num)
        ind = 0
        old_count = counters[0]
        if 0 < old_count < len(num_list):
            while True:
                new_our_num = copy(our_num)
                for i in range(len(new_our_num)):
                    if i == ind:
                        pass
                    else:
                        new_our_num[i] += 1
                        new_our_num[i] %= 10
                new_count = check(num_list, new_our_num)
                if new_count[0] < old_count:
                    new_our_num = our_num
                    ind += 1
                else:
                    print('i work')
                    resault_num.append(new_our_num[ind])
                    new_our_num.pop(ind)
                    our_num.pop(ind)
                    num_list.pop(ind)
                    break
        else:
            for i in range(len(our_num)):
                our_num[i] += 1
                our_num[i] %= 10
    return resault_num


resault_num = list()
num = guess_num()
our_num = list(str(random.randint(1000, 9999)))
our_num = list(map(lambda x: int(x), our_num))
print(our_num, num, sep='\n')
search(num, our_num)
print(resault_num)