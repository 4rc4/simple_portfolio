from django.shortcuts import render, get_object_or_404
from .models import PorscheModel

def home_page(request):
    return render(request, 'pages/home.html')

def model_list(request):
    models = PorscheModel.objects.all()
    return render(request, 'pages/model_list.html', {'models': models})

def model_detail(request, id):
    model = get_object_or_404(PorscheModel, id=id)
    return render(request, 'pages/model_detail.html', {'model': model})
