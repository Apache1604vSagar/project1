from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")

def welcome(request):   
    data='''<html>
            <head>
            <title>welcome page</title>
            </head>
            <body>
            <h1>welcome to Django</h1>
            </body>
            <html>'''
    return HttpResponse(data)