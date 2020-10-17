from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from rest_framework import routers, permissions
from rest_framework.authtoken import views

import praggregator.views
from app.views import ProductViewSet, OfferViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Product Aggregator API",
        default_version='v1',
        description="Let this be the ultimate source of the Product aggregator knowledge. Use it wisely and if "
                    "anything is wrong, contact the developer.",
        contact=openapi.Contact(email="johnunar@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view = get_schema_view(
    openapi.Info(
        title="Product Aggregator API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="johnunar@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view = get_schema_view(
    openapi.Info(
        title="Product Aggregator API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="johnunar@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'offers', OfferViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', praggregator.views.signup, name='signup'),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', views.obtain_auth_token, name='auth'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
