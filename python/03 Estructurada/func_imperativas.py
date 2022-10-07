from collections import defaultdict
from typing import DefaultDict


def saluda(persona):
    print('Hola {persona}')
    print('Encantado de conocerte')

def despide():
    print('Adios Ceeerdo!!')

# Funcion que llama a otra
def uno():
    print('Estoy en uno')
    dos()
def dos():
    print('Estoy en dos')

# Funcion recursiva infinita
def one(x):
    print(x)
    one(x + 1)
