from django.contrib import admin

# Register your models here.

from .models import Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('__str__','slug')
    class meta:
        model = Produto

admin.site.register(Produto, ProdutoAdmin)
