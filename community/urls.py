from django.urls import path, include
from .views import (
    CommunityView,
    CommunityDetailView,
    CommunitySubAdminView,
    CommunityForbiddenView,
    CommunityBookmarkView,
    SearchCommunityView,
    CommunityCategoryView,
)

urlpatterns = [
    path("", CommunityView.as_view(), name="community_view"),
    path("<str:community_url>/", include("feed.urls")),
    path(
        "<str:community_url>/",
        CommunityDetailView.as_view(),
        name="community_detail_view",
    ),
    path(
        "<str:community_url>/category/",
        CommunityCategoryView.as_view(),
        name="community_category_view",
    ),
    path(
        "<str:community_url>/subadmin/",
        CommunitySubAdminView.as_view(),
        name="community_subadmin_view",
    ),
    path(
        "<str:community_url>/forbidden/",
        CommunityForbiddenView.as_view(),
        name="community_forbidden_view",
    ),
    path(
        "<str:community_url>/forbidden/<str:forbidden_word>/",
        CommunityForbiddenView.as_view(),
        name="community_forbidden_view",
    ),
    path(
        "<str:community_url>/bookmark/",
        CommunityBookmarkView.as_view(),
        name="community_bookmark_view",
    ),
    path("search", SearchCommunityView.as_view(), name="search_community_view"),
]
