from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet, basename='booking',)
urlpatterns = [
    path('', views.index, name='home'),
    path('users/', views.UserViews.as_view()),
    path('menu/', views.MenuItemsView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path("booking/", include(router.urls)),
]
