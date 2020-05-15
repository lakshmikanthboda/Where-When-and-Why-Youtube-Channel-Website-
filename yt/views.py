from django.shortcuts import render
from . import ytdata
# Create your views here.
def index(request):
    d=ytdata.go()
    s=ytdata.subdat()
    return render(request,'index.html',{'data':d,'s':s})