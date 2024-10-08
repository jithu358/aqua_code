"""
URL configuration for sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pro1',views.about1),
    path('pro2',views.index1),
    path('',views.index1),
    path('pro3',views.register1),
    path('pro4',views.option1),
    path('pro5',views.login1),
    path('pro6',views.option2),
    path('pro7',views.loginmain),
    path('pro8',views.shop1),
    path('pro9',views.single1),
    path('pro10',views.regdrive),
    path('pro11',views.admin1),
    path('main',views.loginmain),
    path('main1',views.user_profile),
    path('main2',views.profile1),
    path('pro12',views.contact1),
    path('pro13',views.delivery1),
    path('pro14',views.show1),
    path('userd',views.userdetails),
    path('userpro',views.userprof),
    path('req',views.request1),
    path('chpass',views.changepass),
    path('userup',views.upuser),
    path('userupdate',views.userupdate),
    path('addpro',views.addproduct),
    path('delete',views.delete),
    path('update',views.update),
    path('profi',views.profile2),
    path('wait',views.waitdriver),
    path('outlog',views.logout),
    path('delipro',views.deliverprof),
    path('deliup',views.deliupdate),
    path('updeli',views.deliupdate1),
    path('pshow',views.showp),
    path('sshow',views.sampleshopp),
    path('carty',views.addcart),
    path('carty1',views.addcart1),
    path('removecart',views.removecart1),
    path('pay/<int:id>',views.pay),
    path('success',views.success11),
    path('ord',views.ordersdisp),
    path('dishow',views.deliveryshow),
    path('diaccept',views.deliveryaccept),
    path('onway',views.deliveryonway),
    path('delivered',views.delivered1),
    path('payad',views.paymentadmin),
    path('editpro',views.editproduct),
    path('productup',views.upproduct),
    path('productsupdate1',views.productsupdate),
    path('comp',views.comp),
    path('adviewco',views.advicomp),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
