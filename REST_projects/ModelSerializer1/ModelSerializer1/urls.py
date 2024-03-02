
from django.contrib import admin
from django.urls import path,include

import test1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include('test1.urls'))
]
