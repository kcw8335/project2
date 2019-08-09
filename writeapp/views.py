from django.shortcuts import render

def writeapp(request):
    return render(request, 'writeapp.html')

def writeuser(request):
    return render(request, 'writeuser.html')