from django.db import models

# Create your models here.
class Produto(models.Model): #product_category
    nome_produto = models.CharField(max_length=120)
    desc_produto = models.TextField()
    preço_produto = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)

    # python 3
    def __str__(self):
        return self.nome_produto

    # python 2
    def __unicode__(self):
        return self.nome_produto