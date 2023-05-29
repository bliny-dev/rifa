
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # url autenticação
    path('auth/', include('autenticacao.urls')),


    # url de criação lógica do sorteio
    path('sorteio/', include('sorteio.urls')),

]

# urls de arquivos de midia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
