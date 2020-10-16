from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

import praggregator.views
from app.views import ProductViewSet, UserViewSet, OfferViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', praggregator.views.signup, name='signup'),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', views.obtain_auth_token, name='auth'),
]
