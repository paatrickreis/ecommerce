from django.urls import path

from .views import (
                        ProdutoListView,
                        ProdutoDetailSlugView,
                    )

urlpatterns = [
    path('', ProdutoListView.as_view()),
    path('<slug:slug>/', ProdutoDetailSlugView.as_view())
]