# -*-coding: UTF-8 -*-
d =  {'one':'конь', 'two':'коня', 'many':'коней'}
def humanize(n, d):
  if type(n) != int:
    print "Это не число"
  else:
    if (n % 10)>=1 and (n % 10)<5:
        if (n % 100)>=11 and (n % 100)<=15:
            print str(n) + " " + d['many']
        elif n % 10 == 1:
            print str(n) + " " + d['one']
        else:
            print str(n) + " " + d['two']    
    else:
        print str(n) + " " + d['many']
    
humanize(103, d)
humanize(211, d)
humanize(513, d)
