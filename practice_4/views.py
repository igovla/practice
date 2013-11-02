from django.shortcuts import render
from django.template import Template
from django.template import Context
import time
import os
from pages.models import Author
from pages.models import Book
import datetime


def home(request):
    context = {'ts': datetime.datetime.now()}
    return render(request, 'home.html', context)


def books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books.html', context)


def book(request, book_id):
    context = {'book': Book.objects.get(id=book_id)}
    return render(request, 'book.html', context)


def author(request, author_id):
    context = {'author': Author.objects.get(id=author_id)}
    return render(request, 'author.html', context)


def authors(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'authors.html', context)


def listing(request, diry):
    lidir = []
    for fd in os.listdir('/var/log/' + str(diry)):
      if os.path.isdir('/var/log/' + str(diry) + '/' + fd):
        templ = '<tr><td><a href="' + str(fd) + '/">' + fd + '</a></td>'
      else:
        templ = '<tr><td>' + fd + '</td>'
      templ = templ + '<td>' + str(os.path.getsize('/var/log/' + str(diry) + '/' + fd)) + '</td>'
      templ = templ + '<td>' + str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(os.path.getmtime('/var/log/' + str(diry) + '/' + fd)))) + '</td></tr>'
      lidir.append(templ)
    context = {u'dir_content': lidir, }
    return render(request, 'listing.html', context)
