from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Postagem(models.Model):
#Atributos
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	data_criacao = models.DateTimeField(default=timezone.now)
	data_publicacao = models.DateTimeField(blank=True, null=True)
#Metodos 
	def publicar(self):
		self.data_publicacao = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo