"""
To render html web pages
"""
from django.http import HttpResponse 

HTML_STRING = """
<h1> Hello World </h1>
 """ # This is a string

def home_view(request):
# Take in a request (Django sends request) Return
#Html as a response (we pick the response)


    return HttpResponse(HTML_STRING)