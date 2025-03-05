from django.urls import path # type: ignore
from . import views

urlpatterns= [
    path('',views.home,name='home'),
    path('generate-resume/',views.generate_resume, name='generate_resume'),
]
