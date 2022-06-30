from django.shortcuts import render
from .models import Image

def img_list(request):
    image = Image.objects.all()
    return render(request, 'img_list.html', {'image':image})
