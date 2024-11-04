from django.urls import path

from . import views

urlpatterns = [
    path("", views.IncomingListView.as_view(), name="list"),
    path("create/", views.IncomingCreateView.as_view(), name="create"),
    path("details/<slug:slug>/", views.IncomingDetailView.as_view(), name="detail"),
    path("update/<slug:slug>/", views.IncomingUpdateView.as_view(), name="update"),
    path(
        "change-status/<slug:slug>/",
        views.ChangeStatusCreateView.as_view(),
        name="change-status",
    ),
]
