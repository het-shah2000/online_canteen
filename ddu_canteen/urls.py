from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homepage'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name = 'register'),
    path('update_item/', views.updateItem, name = 'update_item'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)