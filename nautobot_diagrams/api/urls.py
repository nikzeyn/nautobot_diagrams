from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.APIRootView = views.NextBoxUIPluginRootView

router.register(r'savedtopologies', views.SavedTopologyViewSet)

# app_name = "nextbox_ui_plugin-api"
app_name = "nautobot_diagrams-api"
urlpatterns = router.urls
