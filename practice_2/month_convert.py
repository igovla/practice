# -*-coding: UTF-8 -*-
months = {'JANUARY': 1, 'FEBRUARY':2, 'MARCH':3, 'APRIL':4, 'MAY':5, 'JUNE':6, 'JULY':7, 'AUGUST':8, 'SEPTEMBER':9, 'OCTOBER':10, 'NOVEMBER':11, 'DECEMBER':12,}
try:
  month = raw_input("Введите название месяца\n")
  mm = month.upper()
  print "Порядковый номер месяца", months[mm]
except:
  print "Такого месяца не бывает"
