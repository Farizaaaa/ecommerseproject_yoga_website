from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from ecommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name='index'),
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='Product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='ProdCatdetail'),
]


app_name='ecommerce'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)