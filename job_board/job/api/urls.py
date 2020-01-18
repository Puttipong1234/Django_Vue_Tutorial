from django.urls import path

# from news.api.views import ArticleDetailAPIView , ArticleListCreateAPIView , JournalListCreateView
from job.api.views import JobOfferDetailAPIView , JobOfferListCreateAPIView
urlpatterns = [
    path("joboffers/",JobOfferListCreateAPIView.as_view(),
        name = "joboffer-list"),

    path("joboffers/<int:pk>/",
        JobOfferDetailAPIView.as_view(),
        name="joboffer-detail")``
]