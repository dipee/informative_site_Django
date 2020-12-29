from django import urls
from .views import HeaderImageViewSet, ServicesViewSet, TestimonailViewSet, ContactViewSet, TestView
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register(r'header', HeaderImageViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'testimonial', TestimonailViewSet)
router.register(r'contact', ContactViewSet)
schema_view = get_schema_view(
   openapi.Info(
      title="Clinic Info API",
      default_version='v1',
      description="This API allows us manage content of informative site",
      terms_of_service="https://www.scvconsultants.com",
      contact=openapi.Contact(email="michal@scvconsultants.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
   
 
