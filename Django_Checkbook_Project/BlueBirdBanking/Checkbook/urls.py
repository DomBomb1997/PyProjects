from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Checkbook.urls'))
    path('<int:ok>/balance/', views.balance, name='balance'),
]