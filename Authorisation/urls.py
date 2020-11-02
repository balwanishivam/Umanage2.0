from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="Authorisation"

urlpatterns=[
    # path('',views.index,name='index'),
    path('index/',views.index,name="index"),
    path('',views.LoginView.as_view(),name='login'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    # path('forgotpassword/',views.forgotpassword,name='forgotpasssword')
]
