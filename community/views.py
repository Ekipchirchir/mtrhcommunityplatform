from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html')

def about(request):
    return render (request, 'about.html')

def login(request):
    return render (request, 'login.html')

def messages(request):
    return render (request, 'messages.html')

def departments(request):
    return render (request, 'departments.html')

def ict(request):
    return render (request, 'ict.html')

def pharmacy(request):
    return render (request, 'pharmacy.html')

def finance(request):
    return render (request, 'finance.html')

def administration(request):
    return render (request, 'administration.html')

def lab(request):
    return render (request, 'lab.html')

def radiology(request):
    return render (request, 'radiology.html')

def supplychain(request):
    return render (request, 'supplychain.html')

def kitchen(request):
    return render (request, 'kitchen.html')

def icu(request):
    return render (request, 'icu.html')

def emergency(request):
    return render (request, 'emergency.html')

def ict(request):
    return render (request, 'ict.html')

def footer(request):
    return render (request, 'footer.html')

def announcements(request):
    return render (request, 'announcements.html')