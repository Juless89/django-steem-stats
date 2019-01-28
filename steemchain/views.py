from django.shortcuts import render
from django.http import HttpResponse
from .services import blockchain_data

import json

# Create your views here.

def homePageView(request):
    data = blockchain_data()

    response = HttpResponse()
    # refresh every 3 seconds
    response.write('<meta http-equiv="refresh" content="3" />')

    # add each key, value par on a separate line
    for k, v in data.items():
	    response.write(f'{k}: {v}<br>')
    return response