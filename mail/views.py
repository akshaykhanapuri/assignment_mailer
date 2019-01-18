from django.shortcuts import render
from .emailadmin import em_admin, em_user
from multiprocessing import Process
# Create your views here.

def home(request):
    if request.method == 'POST':
        p1 = Process(target=em_user(request))
        p1.start()
        p2 = Process(target=em_admin())
        p2.start()
        p1.join()
        p2.join()
        return render(request, 'mail/home.html')
    else:
        return render(request, 'mail/home.html')
