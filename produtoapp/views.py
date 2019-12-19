
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Produto

#Class Based View

class ProdutoDetailSlugView(DetailView):
    queryset = Produto.objects.all()
    template_name = "produtos/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug = slug, active = True)
        try:
            instance = Produto.objects.get(slug = slug, ativo = True)
        except Produto.DoesNotExist:
            raise Http404("Não encontrado!")
        except Produto.MultipleObjectsReturned:
            qs = Produto.objects.filter(slug = slug, ativo = True)
            instance =  qs.first()
        return instance

class ProdutoFeaturedListView(ListView):
    template_name = "produtos/list.html"

    def get_queryset(self, *args, **kwargs):
        return Produto.objects.featured()

class ProdutoFeaturedDetailView(DetailView):
    queryset = Produto.objects.all().featured()
    template_name = "produtos/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    # request = self.request
    # return Product.objects.featured()


class ProdutoListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada
    #queryset = Produto.objects.all()
    template_name = "produtos/list.html"
#    def get_context_data(self, *args, **kwargs):
#       context = super(ProdutoListView, self).get_context_data(*args, **kwargs)
#       print(context)
#       return context

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Produto.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance

class ProdutoDetailView(DetailView):
    # traz todos os produtos do banco de dados sem filtrar nada
    queryset = Produto.objects.all()
    template_name = "produtos/detail.html"

    # def get_context_data(self, *args, **kwargs):
    # context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    # print(context)
    # return context
