from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParagraphViewSet, LogoutView

router = DefaultRouter()
router.register(r'recipes', ParagraphViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', LogoutView.as_view(), name='logout'),
]
