from django.urls import path
from .views import index, by_rubric, DbCreateView, product,delItem,pay, stocks, about_us, basket, cart, addToCart,plusNumber,minusNumber

app_name = 'main'
urlpatterns = [
	path('product/<int:product_id>/' , product, name = "product"),
	path('add/', DbCreateView.as_view(), name='add'),
	path('about_us/', about_us, name = 'about_us'),
	path('product/<int:product_id>/addToCart/', addToCart, name = 'addToCart'),
	path('makeComment/', basket, name = 'makeComment'),
	path('stocks/', stocks, name = 'stocks'),
	path('<int:rubric_id>/', by_rubric, name = 'by_rubric'),
	path('product/<int:product_id>/plus/', plusNumber, name = 'plusNumber'),
	path('product/<int:product_id>/minus/', minusNumber, name = 'minusNumber'),
	path('cart/', cart, name = 'cart'),
	path('product/<int:product_id>/del/', delItem, name = 'delItem'),
	path('', index, name = 'index'),
	path('pay/', pay, name = 'pay'),


]