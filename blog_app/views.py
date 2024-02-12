import datetime
import random

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        "name": "farzona",
        "age": random.randint(a=1,b=24),
        "time":datetime.datetime.now().strftime("%Y.%m.%d")
    }
    return HttpResponse(f"""
    <h1>{context['name']} ning yoshi {context['age']} da</h1>
    <p>bugun:<code> {context['time']} </code></p>

""")