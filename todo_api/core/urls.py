from rest_framework.routers import DefaultRouter
from .viewsets import ProjectViewSet, CategoryViewSet, TaskViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('categories', CategoryViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = router.urls