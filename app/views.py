from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':10,'b':40,'c':50}
    return render(request,'operations.html',d)