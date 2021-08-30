#!/usr/bin/env python3
"""Reading in and writing out files"""


def main():
    myfile = open("vendor.txt", 'r')

    with open('vendor-ips.txt', 'w') as myoutfile:
        for line in myfile.readlines():
            splitline = line.split(' ')
            myoutfile.write(splitline[-1] + '\n')


    myfile.close()
main() 
