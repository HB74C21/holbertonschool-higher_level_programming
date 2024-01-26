#!/usr/bin/python3
import sys

count_arg = sys.argv[1:]
length_argv = 1

if len(count_arg) < 1:
    print("{} arguments.".format(len(count_arg)))
elif len(count_arg) == 1:
    print("{} argument:".format(len(count_arg)))
    print("{}: {}".format(len(count_arg), sys.argv[length_argv]))
else:
    print("{} arguments:".format(len(count_arg)))
    while length_argv <= len(count_arg):
        print("{}: {}".format(length_argv, sys.argv[length_argv]))
        length_argv += 1
