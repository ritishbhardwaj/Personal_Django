
from django.contrib import admin
from django.urls import path,include

import testapp1
from testapp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/', views.studentDetail),
    path('testapp/',include('testapp1.urls'))

]
