from django.shortcuts import render
from .models import MenuItem

def my_view(request):
    context = {'menu_name': 'main_menu'}
    return render(request, 'menu.html', context)

