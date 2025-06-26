from django.db import models

class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.cargo} - {self.empresa}"

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    tecnologias = models.CharField(max_length=200)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

