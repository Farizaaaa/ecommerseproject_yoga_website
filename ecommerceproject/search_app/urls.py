from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name='search_app'
urlpatterns=[
    path('',views.SearchResult,name='SearchResult'),
]

app_name='search_app'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)