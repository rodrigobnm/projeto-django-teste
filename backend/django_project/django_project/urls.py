from django.contrib import admin
from django.conf import settings # p foto
from django.urls import path, include
from django.conf.urls.static import static # p foto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_app.urls')),
    path('sobre/', include('django_app.urls')),
    path('aba1/', include('django_app.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # p foto
