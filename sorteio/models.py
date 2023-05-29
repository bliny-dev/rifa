from django.db import models
from django.contrib.auth.models import User


class Premios(models.Model):
    
    numero_premio = models.IntegerField()
    descricao_premio = models.CharField(max_length=50)


class Sorteio(models.Model):

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.FloatField()
    qtd_bilhetes = models.IntegerField()
    data_sorteio = models.DateTimeField()
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_sorteio = models.ImageField(upload_to="rifa_img/") 
    premio = models.ManyToManyField(Premios, related_name='sorteios')


    def __str__(self):
        return self.nome


class Promocaos(models.Model):
    qtd_cotas = models.IntegerField()
    preco_cotas = models.FloatField() 
    Sorteio = models.ForeignKey(Sorteio, on_delete=models.CASCADE, null=True, blank=True)
