from django.urls import path,include
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("employees",views.employees,name="employees"),
    path("tracking",views.tracking,name="tracking"),
    path("final",views.final,name="final")
]