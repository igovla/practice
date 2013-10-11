# -*- coding: utf-8 -*-
consts = { 'pi' : float(3.141592653589), 'e' : float(2.711828182845),}

inp = raw_input("Введите <имя константы>:<точность>\n")
l = []
for word in inp.split(":"):
   l.append(word)
if len(l) == 2:
   num = int(l[1])
   name = l[0]
   if consts.has_key(name):
     print "name ~=", round(consts[name], num)
   else:
     print "Такая константа не задана"
else:
   print "Неправильный формат введённых данных"
