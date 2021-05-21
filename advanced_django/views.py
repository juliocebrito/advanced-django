from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    response = HttpResponse('<h1>Django Advance! Current server time is: {now}</>'.format(now=now))
    # import pdb; pdb.set_trace()
    return response