import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))

for ind, dat in enumerate(lst_in):
    lst_in[ind] = dat.replace(' ', '-')
    lst_in[ind] = lst_in[ind].replace('--', '-')
    while '--' in lst_in[ind]:
        continue

for i in lst_in:
    print(i)
