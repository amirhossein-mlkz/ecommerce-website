from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('<slug:the_slug>', views.single_category, name='scat' ),
    path('', views.archive_category, name='acat' )

]
