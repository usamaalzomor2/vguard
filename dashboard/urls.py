from rest_framework import routers
from .views import AgeGenderCountView, AgeGenderSummaryView, CameraViewSet, FireSmokeWeaponDetectionViewSet, AgeGenderViewSet, FaceRecognitionViewSet, LicensePlateRecognitionViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register('camera', CameraViewSet)
router.register('detection', FireSmokeWeaponDetectionViewSet)
router.register('agegender', AgeGenderViewSet)
router.register('facerecog', FaceRecognitionViewSet)
router.register('platerecog', LicensePlateRecognitionViewSet)

urlpatterns = [
    path('agegender/summary/', AgeGenderSummaryView.as_view(), name='agegender-summary'),
    path('agegender/now/', AgeGenderCountView.as_view(), name='agegender-now'),
]

urlpatterns += router.urls
