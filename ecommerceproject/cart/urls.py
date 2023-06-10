from django.conf.urls.static import static
from django.urls import path

from django.conf import settings
from . import views


urlpatterns = [

    path('add/<int:product_id>',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('full_remove/<int:product_id>', views.full_remove, name='full_remove'),
    path('', views.cart_detail, name='cart_detail'),

]

app_name='cart'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)