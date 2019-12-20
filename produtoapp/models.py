from django.db import models

from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

#Custom queryset
class ProdutoQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(ativo = True)

    def featured(self):
        return self.filter(destaque = True, ativo = True)


class ProdutoManager(models.Manager):

    def get_queryset(self):
        return ProdutoQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        # return self.get_queryset().filter(featured = True)
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

class Produto(models.Model): #product_category
    nome_produto = models.CharField(max_length=120)
    desc_produto = models.TextField()
    preço_produto = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    imagem_produto = models.ImageField(upload_to = 'products/', null=True, blank=True)
    destaque = models.BooleanField(default = False)
    ativo = models.BooleanField(default = True)
    slug = models.SlugField(blank= True, unique= True)

    objects = ProdutoManager()

    def get_absolute_url(self):
        return "/produtos/{slug}/".format(slug=self.slug)

    # python 3
    def __str__(self):
        return self.nome_produto

    # python 2
    def __unicode__(self):
        return self.nome_produto


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender= Produto )