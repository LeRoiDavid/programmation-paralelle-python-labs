from math import *

def add(x, y):
    """ Somme entre deux nombres"""
    return x + y

def multiply(x, y):
    """ facteur entre 2 nombres """
    return x * y

def my_min(x, y):
    """ Min  entre 2 nombres """
    return min(x,y)

def minus(x, y):
    """ Diff entre 2 nombres """
    return x - y


def cal_distance(pointA, pointB):
    """ Calcule la distance entre 2 points """
    dist=0
    for i,j in zip(pointA,pointB):
        dist += pow((i-j),2)
    return sqrt(dist) 


def my_map(fun, arg1, arg2):
    """ Calcul the distance between two points"""
    res = []
    print(fun.__doc__)
    for i, j in zip(arg1, arg2):
        res.append(fun(i, j))
    return res

a = [1, 2, 3, 5, 8]
b = [8, 3, 7, 4, 6]

point1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
point2 = [(3.0, 2.0, 4.0), (3.0, 4.0, 5.0), (2.0, 2.0, 1.0)]

print(my_map(add, a, b))
print(my_map(multiply, a, b))
print(my_map(minus, a, b))
print(my_map(my_min, a, b))
print(my_map(cal_distance, point1, point2))