from django.urls import path
from . import views

urlpatterns = [

    path('',views.cart_view,name='cart_view'),
    path('product/',views.product, name='product'),
    path('add/<int:product_id>/', views.add_pro, name='add_pro'),
    path('creat/', views.creat, name='creat'),
    path('delete/<int:product_id>',views.delete,name='delete'),
    path('cat/',views.add_cat,name='cat'),
    path('search/',views.search,name='search'),
    path('add/<int:product_id>',views.add_pro,name='add'),
    path('remove_cart/<int:item_id>',views.remove_cart,name='remove'),
    path('increase_cart/<int:item_id>',views.increase,name='inc'),
    path('decrease_cart/<int:item_id>',views.decrease,name='dec'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('invoice/',views.invoice,name='invoice'),

    
]