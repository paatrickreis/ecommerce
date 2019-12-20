from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from .views import (home_page, 
                    about_page, 
                    contact_page, 
                    login_page, 
                    register_page
)

urlpatterns = [
    path('', home_page),
    path('sobre/', about_page),
    path('contato/', contact_page),
    path('login/', login_page),
    path('registro/', register_page),
    path('produtos/', include('produtoapp.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)