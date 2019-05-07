from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
# Create your views here.

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'player/index.html',
        {
            'title':'Player page',
            'year':datetime.now().year,
        }
    )