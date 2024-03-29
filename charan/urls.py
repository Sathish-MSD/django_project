"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path



from charan.views import OrderReg, Orderlist ,Orderdetail , OrderUpdate, OrderDelete 

app_name='charan'

urlpatterns = [
   
   path('Orderreg', OrderReg.as_view(), name = 'Orderreg'),
   path('<pk>/Orderdetail', Orderdetail.as_view(), name = 'Orderdetail'),
   path('',Orderlist.as_view(), name = 'Orderlist'),
   path('<pk>/Orderupdate',OrderUpdate.as_view(),name = 'Orderupdate'),
   path('<pk>/Orderdelete', OrderDelete.as_view(), name = 'Orderdelete'),
]