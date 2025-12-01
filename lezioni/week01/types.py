# Tipi

#num : int = 2

#print(type(num))

#num_f : float = 2.6

#print(type(num_f))

#num_str : str = "2.6"

#print(type(num_str))

#booleano : bool = False

#print(type(booleano))

#import sys

#a : int = 500

#b : int = a

#print(sys.getrefcount(b))

#print(sys.version)

#print(sys.platform)

#print(dir(sys))

#print(help(sys))

import psutil

from sys import version

print(version)

#print(dir(psutil))

print(psutil.cpu_stats)


codice : str = input("inserire codice di tre cifre:")

print(codice)
