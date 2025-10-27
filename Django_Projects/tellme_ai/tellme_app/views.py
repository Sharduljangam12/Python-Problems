from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello, Django!</h1><p>welcome to Tell Me App</p>")