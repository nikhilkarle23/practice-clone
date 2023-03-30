from django.urls import path

from complaint_app import views

app_name = 'complaint_app'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('create_complaint/', views.CreateComplaint.as_view(), name='create_complaint'),
    path('complaint_list/', views.ComplaintList.as_view(), name='complaint_list'),
]