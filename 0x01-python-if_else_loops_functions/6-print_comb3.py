#!/usr/bin/python3
for item in range(0, 10):
    for i in range(1, 10):
        if item < i:
            if item < 8:
                print("{}{}, ".format(item, i), end='')
            else:
                    print("{}{}".format(item, i), end='')
