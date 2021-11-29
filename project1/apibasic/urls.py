
from django.db import router
from django.urls import path,include
from .views import employee_list,employee_details,StudentAPIView,studentdetails,GenericAPIView,studentViewSet,studentgenericviewset,stuModelciewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('studentviewset',studentViewSet,basename='studentviewset')

router.register('stugenericviewset',studentgenericviewset,basename='stugenericviewset')
router.register('stuModelviewset',stuModelciewset,basename='stuModelviewset')


urlpatterns = [

    path('viewset/',include(router.urls)),
    # path('viewset/<int:pk>/',include(router.urls)),
    # path('genericview/',include(router.urls)),
    # path('genericview/',include(router.urls)),
    # path('mdlviewset/',include(router.urls)),


    path('employeelist/', employee_list),
    path('empdetails/<int:pk>/', employee_details),
    path('studentapi/', StudentAPIView.as_view()),
    path('studentdetails/<int:id>/',studentdetails.as_view()),
    path('Genericstudent/<int:id>/', GenericAPIView.as_view()),
    path('Genericstudent/', GenericAPIView.as_view()),

    # path('stugenericviewset/', studentgenericviewset.as_view()),




]
