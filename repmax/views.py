from django.shortcuts import render
from django.http import HttpResponse
from .func import oneCal

# Create your views here.




def index(request):
    return render(request, "repmax/index.html", {'index':'index'})


def oneCal(request):
    context = dict()
    reps = float(request.GET['R'])
    weight = float(request.GET['W'])
    if request.GET['kind'] == 'E':
        rxw = round(weight*(1 + (reps/30)), 2)
    else:
        rxw = round(weight*(36/(37 - reps)), 2)

    percent = []

    for i in range(100, 45, -5):
        percent.append([i, round(rxw*(i/100), 2)])
    context['result'] = percent
    return render(request, 'repmax/index.html', context=context)



# 1RM=W×(36/(37−R))