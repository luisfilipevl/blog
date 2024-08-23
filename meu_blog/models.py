from django.db import models

# Create your models here.


class Sobre (models.Model):
    escola = models.CharField(max_length=50)
    curso = models.CharField(max_length=20)
    ano = models.IntegerField()
    interece = models.TextField()
    descricao = models.TextField()
    habilidades = models.TextField()
    experiencia_profissional = models.TextField()
    projetos = models.TextField()

    def __str__(self):
        return f"{self.curso} - {self.escola}"
    
class Eu (models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    sobre = models.ForeignKey(Sobre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome