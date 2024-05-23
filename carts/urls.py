from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.cart, name='cart'),
    path("<int:product_id>/", view=views.add_to_cart, name="add_cart"),
    path("change_quanity/<int:item_id>/<str:state>", view=views.change_quanity, name="change_quanity")

]
