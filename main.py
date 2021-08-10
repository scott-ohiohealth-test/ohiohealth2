# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
from datetime import datetime


def main():
    """Write a python program to generate a series of random numbers divisible by 5. Generate 20 sequence of numbers"""
    dt_for_log = datetime.now()
    formatted_time = dt_for_log.strftime('%Y-%m-%d-%H-%M')
    series_of_series = range(20)
    list_of_rnd = []
    fn = f'/home/scott2/{formatted_time}.log'
    for i in series_of_series:
        rnd = str(divisible_random(0, 1000, 5))
        list_of_rnd.append(rnd)
    #print(list_of_rnd)
    with open(fn, 'w') as file:
        file.write(str(list_of_rnd))


def divisible_random(a, b, n):
    if b - a < n:
        raise Exception('{} is too big'.format(n))
    result = random.randint(a, b)
    while result % n != 0:
        result = random.randint(a, b)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
