from django.shortcuts import render
from django.http import HttpResponse
from .models import Notice
from django.conf import settings

# Create your views here.
def index(request):
     
    queryset = Notice.objects.filter(to=request.user)
    context = {
        "queryset" : queryset
    }
    return render (request ,'index/index.html', context)
    #return HttpResponse('Yo mama yokohama')