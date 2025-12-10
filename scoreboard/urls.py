from django.urls import path
from . import views

app_name = "scoreboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/<int:team_id>/", views.add_points, name="add_points"),
    path("reset/", views.reset_scores, name="reset_scores"),
    path("subtract/<int:team_id>/", views.subtract_points, name="subtract_points"),
]
