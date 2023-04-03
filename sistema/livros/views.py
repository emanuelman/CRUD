from django.shortcuts import render
from .models import Livro
# Create your views here.
def home(request):
    return render(request, "index.html")

def lista_livros(request):
    if request.method == "POST":
        livros = Livro()
        livros.nome_livro = request.POST.get("nome-livro")
        livros.nome_autor = request.POST.get("nome-autor")
        livros.save()

    livros = {
        'lista_livros': Livro.objects.all()
    }

    return render(request, "lista_livros.html", livros)

