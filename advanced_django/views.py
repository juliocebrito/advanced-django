import re
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from django.core.mail import send_mail

def index(request):
    # import ipdb; ipdb.set_trace()
    # print(request.GET)
    # print(request.POST)
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    response = HttpResponse('<h1>Django Advanced! Current server time is: {now}</>'.format(now=now))
    # import pdb; pdb.set_trace()
    return response

def sending_email():
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    send_mail(
        'Django Advanced!',
        'Current server time is: {now}'.format(now=now),
        'from@example.com',
        ['jucebridu@gmail.com'],
        fail_silently=False,
        )

def file_manipulation():
  try:
      now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
      file = open('temp/test_file.txt', 'w')
      file.write('Django Advanced! Current server time is: {now}'.format(now=now))
      file.close()
      return file
  except OSError as err:
      print("Error: {0}".format(err))