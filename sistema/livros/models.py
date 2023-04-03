from django.db import models

# Create your models here.
class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    nome_livro = models.CharField(max_length=80)
    nome_autor = models.CharField(max_length=80)

