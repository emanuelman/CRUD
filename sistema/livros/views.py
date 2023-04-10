from django.shortcuts import render
from .models import Livro

# Create your views here.

def home(request):
    if request.method == "POST":
        nome_livro = request.POST.get('nome_livro')
        nome_autor = request.POST.get('nome_autor')
        livro = Livro(nome_livro=nome_livro,nome_autor=nome_autor)
        livro.save()
    return render(request, "index.html")

