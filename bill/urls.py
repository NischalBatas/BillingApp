from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('customer/<int:id>',views.customer,name='customer'),
    path('bills/<int:id>',views.bills,name='bills'),
    path('prod_update',views.prod_update,name='prod_update'),
    path('customform/<int:id>',views.customform,name='customform')
]


urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)