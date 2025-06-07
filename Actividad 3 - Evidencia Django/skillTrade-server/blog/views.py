from django.http import HttpResponse
def inicio(request):
    return HttpResponse("<h1>Página de inicio del blog</h1>")
def contacto(request):
    return HttpResponse("<p>Contacto: contacto@miweb.com</p>")
