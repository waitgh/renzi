import random
import sys

def zprint(zlist, width=10):
    count = 0
    line = ''
    for zi in zlist:
        line += '{0} '.format(zi)
        count +=1
        if count % width == 0:
            print('{0}\n'.format(line))
            line = ''
    if line:
        print('{0}\n'.format(line))

def load_shengzi(file_name):
    shengzi = []
    with open(file_name, "r", encoding='utf-8', ) as f:
        for line in f.readlines():
            shengzi += line.strip().split()
    return shengzi

if __name__ == '__main__':
    while True:
        _input = input('## please put the size of the test set or \'q\' to quit: ')
        if _input.lower() == 'q':
            sys.exit(0)
        _num = int(_input)
        shengzi = load_shengzi('./shengzi.txt')
        if _num <= len(shengzi):
            zprint(random.sample(shengzi, _num))
        else:
            random.shuffle(shengzi)
            zprint(shengzi)
