from django.contrib import admin
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('view/<int:p_id>/', views.product_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
