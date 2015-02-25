from django.shortcuts import render

# Create your views here.
def home(request):
    user_name = request.META.get('SSL_CLIENT_S_DN_CN', 'Anonymous')
    user_email = request.META.get('SSL_CLIENT_S_DN_Email', 'undefined')
    return render(request, 'home.html', {'user_name': user_name, 'user_email': user_email})
