import argparse
import random
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name",
        help='python renzi <subcommand> -h for more info')

    # create the parser for the "shengzi" command
    shengzi_parser = subparsers.add_parser('shengzi',
                                           help='print out shenngzi to test')
    shengzi_parser.add_argument('--count', '-c', dest='count', default=10, type=int,
                                help='How many shengzi you want to test, default (10)')

    # create the parser for the "zuci" command
    zuci_parser = subparsers.add_parser('zuci',
                                        help='print out cizu to test')
    zuci_parser.add_argument('--count', '-c', dest='count', default=10, type=int,
                             help='How many cizu you want to test, default (10)')
    zuci_parser.add_argument('--category', '-t', dest='category', default='general',
                             help='Catetory of cizu, such as animal, food, idiom, poem, default (general)')
    zuci_parser.add_argument('--zi', '-z', dest='zi',
                             help='Find all the cizu with the particular shengzi')

    # create the parser for the "similar" command
    similar_shengzi_parser = subparsers.add_parser('similar',
                                                   help='print out similar shenngzi to test')
    similar_shengzi_parser.add_argument('--count', '-c', dest='count', default=10, type=int,
                                        help='How many similars shengzi you want to test, default (10)')

    namespace = parser.parse_args()

    if (namespace.subparser_name != 'shengzi' and namespace.subparser_name != 'zuci'
        and namespace.subparser_name != 'similar'):
        parser.print_help()
        sys.exit(1)

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

def shengzi_zuci(zi, clist):
    '''Find all the zicu associated with a zi
    '''
    _ret = []
    for ci in clist:
        if zi in ci:
           _ret.append(ci)
    return _ret

def load_shengzi(file_name):
    shengzi = []
    with open(file_name, "r", encoding='utf-8', ) as f:
        for line in f.readlines():
            shengzi += line.strip().split()
    return shengzi

def load_similar_shengzi(file_name):
    similar_shengzi = []
    with open(file_name, "r", encoding='utf-8', ) as f:
        for line in f.readlines():
            similar_shengzi.append(line.strip())
    return similar_shengzi

def dedup(zilist):
    _dict = {}
    for zi in zilist:
        if zi in _dict:
            _dict[zi] += 1
        else:
            _dict[zi] = 1
    for k, v in _dict.items():
        if v > 1:
            print(k)

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

def random_zprint(target_list, number, width=10):
    '''Print random number of zi/ci from the target list
    '''
    if number <= len(target_list) and number > 0:
        zprint(random.sample(target_list, number), width)
    else:
        random.shuffle(target_list)
        zprint(target_list, width)

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
    dedup(zilist)
    filterd_ci = filter_cihui(cilist, zilist)
    if namespace.subparser_name == 'zuci' and namespace.zi:
        filterd_ci = shengzi_zuci(namespace.zi, filterd_ci)

    if namespace.subparser_name == 'shengzi':
        random_zprint(zilist, namespace.count)
    elif namespace.subparser_name == 'zuci':
        random_zprint(filterd_ci, namespace.count)
    elif namespace.subparser_name == 'similar':
        similar_zilist = load_similar_shengzi('./similar.txt')
        random_zprint(similar_zilist, namespace.count, width=1)
