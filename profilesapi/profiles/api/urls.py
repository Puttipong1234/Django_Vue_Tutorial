from django.urls import path , include
from rest_framework.routers import DefaultRouter
from profiles.api.views import ProfileViewSet , ProfileStatusViewSet , AvatarUpdateView
#adding viewset
# profile_list = ProfileViewSet.as_view({"get":"list"})
# profile_detail = ProfileViewSet.as_view({"get":"retrieve"})

##use router 
router = DefaultRouter()
router.register(r"profiles",ProfileViewSet)
router.register(r"status",ProfileStatusViewSet , basename="status") #define query set



urlpatterns = [
    path("",include(router.urls)),
    path("avatar/",AvatarUpdateView.as_view(),name="avatar-update")
]
