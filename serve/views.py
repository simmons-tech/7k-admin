from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.templatetags.static import static
import os

# Create your views here.
def home(request):
    user_name = request.META.get('SSL_CLIENT_S_DN_CN', 'Anonymous')
    user_email = request.META.get('SSL_CLIENT_S_DN_Email', 'undefined')
    return render(request, 'home.html', {'user_name': user_name, 'user_email': user_email})

def render_7k(request):
    return HttpResponseRedirect(static('img/canvas.png'))
    #with open(os.path.join(settings.EXTERNAL_CONFIG, 'canvas.png'), "rb") as f:
    #    return HttpResponse(f.read(), content_type="image/png")
