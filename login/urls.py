from django.urls import path
from .views import indexclass, Loginclass, viewproduct, AddForm


app_name = 'login'  # url namespace
urlpatterns = [
    path('', indexclass.as_view(), name='index'),
    path('login/', Loginclass.as_view(), name='login'),
    path('auth/', viewproduct, name='auth'),
    path('addpost/', AddForm.as_view(), name='addpost'),
]