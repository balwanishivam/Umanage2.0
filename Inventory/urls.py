from django.urls import path
from . import views    
app_name='Inventory'
urlpatterns = [
    path('',views.index,name="index"),
    #path('<int:product_id>/',virws.detail,name="detail"),
    path('<int:pk>/', views.details,name="details"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('addnew/',views.addnew,name="addnew"),
    #path('delete/<int:pk>/',views.delete,name="delete")
    
    
    # url(r'^$', index, name="index"),
    # url(r'^(?P<product_id>[0-9]+)$', detail, name="detail"),
    # url(r'^(?P<pk>\d+)$', detail, name="detail"),
    # url(r'^edit/(?P<pk>\d+)$', edit, name="edit"),
    # url(r'^addnew$', addnew, name="addnew"),
    
]