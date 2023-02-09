from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('customer/<int:id>',views.customer,name='customer'),
    path('bills/<int:id>',views.bills,name='bills'),
    path('prod_update',views.prod_update,name='prod_update'),
    path('customform/<int:id>',views.customform,name='customform'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('delete_customer/<int:id>',views.delete_customer,name='delete_customer'),
    path('update_customer/<int:id>',views.update_customer,name='update_customer'),
    path('bar_graph',views.bar_graph_view,name='bar_graph'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('customer',views.customer_list,name='customer_list'),
    path('search',views.searchs,name="searchs"),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('signup',views.user_signup,name='signup')
]


urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)