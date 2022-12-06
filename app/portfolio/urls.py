from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='home'),
    path('download-cv', views.download_view, name='download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
