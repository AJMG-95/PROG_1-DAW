import re

p = re.compile('abc')

p.match('def') #    >> none
p.match('abc') #    >> re.Match objet; span(0, 3) match('abc')
p.search('xabc') #    >> re.Match objet; span(1, 4) match('abc')
p.search('abcx') #    >> re.Match objet; span(0, 3) match('abc')
p.search('xxabcxx') #    >> re.Match objet; span(3, 5) match('abc')

p = re.compile('ab*c')

p.search('abbbc') #    >> re.Match objet; span(0, 5) match('abc')

p = re.compile('ab+c')

p.search('ac') #    >> none
p.search('abc') #    >> re.Match objet; span(0, 5) match('abc')

p = re.compile('ab?')

p.search('abb') #    >> re.Match objet; span(0, 2) match('ab')
p.search('bab') #    >> re.Match objet; span(1, 2) match('ab')
p.match('bab') #    >> none

p = re.compile('a.c')

p.search('a\nc') #  >> none
p.search('a\tc') #  >> re.Match objet; span(1, 3) match('a\tc')

'''
Escribir una expresion regular que sea un identificadr valido
(no puede empezar por un digito)
Algo que sea alfabetico incluyendo _ y despues sea alfanumerico
[a-zA-Z_]\w*
'''

ñ = re.compile(r'[a-zA-Z_]\w*')
