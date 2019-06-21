import argparse
import random

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name",
        help='python renzi <subcommand> -h for more info')

    # create the parser for the "shengzi" command
    shengzi_parser = subparsers.add_parser('shengzi',
                                           help='print out shenngzi to test')
    shengzi_parser.add_argument('--count', dest='count', default=10, type=int,
                                help='How many shengzi you want to test')

    # create the parser for the "zuci" command
    zuci_parser = subparsers.add_parser('zuci',
                                        help='print out cizu to test')
    zuci_parser.add_argument('--count', dest='count', default=10, type=int,
                             help='How many cizu you want to test')
    zuci_parser.add_argument('--category', dest='category', default='general',
                             help='Where do those cizu belong, such as animal, food')


    namespace = parser.parse_args()
    return namespace

def load_cihui(file_name):
    cihui = []
    with open(file_name, "r", encoding='utf-8', ) as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                ci = line.split()[0]
                if len(ci) > 1:
                    cihui.append(ci)
    return cihui

def filter_cihui(clist, zilist):
    '''Filter the cihui list by the shengzi list

    Find all the possible cihui from clist using only shengzi
    found in the zilist
    '''
    _ret = []
    for ci in clist:
        found = True
        for z in ci:
            if z in zilist:
                continue
            else:
                found = False
                break
        if found:
           _ret.append(ci)
    return _ret

def load_shengzi(file_name):
    shengzi = []
    with open(file_name, "r", encoding='utf-8', ) as f:
        for line in f.readlines():
            shengzi += line.strip().split()
    return shengzi

def load_shengzi(file_name):
    shengzi = []
    with open(file_name, "r", encoding='utf-8', ) as f:
        for line in f.readlines():
            shengzi += line.strip().split()
    return shengzi

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

def random_zprint(target_list, number):
    '''Print random number of zi/ci from the target list
    '''
    if number <= len(target_list) and number > 0:
        zprint(random.sample(target_list, number))
    else:
        random.shuffle(target_list)
        zprint(target_list)

if __name__ == '__main__':
    namespace = parse_args()
    cilist = []
    if namespace.subparser_name == 'zuci':
       if namespace.category == 'animal':
           cilist = load_cihui('./animals.txt')
       elif namespace.category == 'food':
           cilist = load_cihui('./food.txt')
       elif namespace.category == 'idiom':
           cilist = load_cihui('./chengyu.txt')
       elif namespace.category == 'poem':
           cilist = load_cihui('./poem.txt')
       elif namespace.category == 'place':
           cilist = load_cihui('./place.txt')
       elif namespace.category == 'general':
           cilist = load_cihui('./changyongcidian.txt')

    zilist = load_shengzi('./shengzi.txt')
    filterd_ci = filter_cihui(cilist, zilist)

    if namespace.subparser_name == 'shengzi':
        random_zprint(zilist, namespace.count)
    elif namespace.subparser_name == 'zuci':
        random_zprint(filterd_ci, namespace.count)
