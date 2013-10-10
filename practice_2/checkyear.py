# -*- coding: utf-8 -*-
y = input("Введите год для проверки: ")
if type(y) != int:
  print "Это не год :("
else:
  if y%400==0:
    print("Високосный")
  elif y%100==0:
    print("Невисокосный")
  elif y%4==0:
    print("Високосный")
  else:
    print("Не високосный")
