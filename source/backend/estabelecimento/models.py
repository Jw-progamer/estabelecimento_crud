import uuid
from django.db import models

# Create your models here.


class Estabelecimento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cnpj = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=30)
    endereco = models.TextField()
    raio_distancia = models.IntegerField()

    def __str__(self):
        return self.nome+str(self.raio_distancia)

    def distance(self, loc):
        location = self.raio_distancia - loc
        if location < 0:
            return location * -1
        return location

    class Meta:
        verbose_name = "Estabelecimento"
        verbose_name_plural = "Estabelecimentos"
