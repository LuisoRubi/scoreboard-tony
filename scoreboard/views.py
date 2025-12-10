from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Team
from django.views.decorators.http import require_POST

def index(request):
    teams = Team.objects.all().order_by("id")
    return render(request, "scoreboard/index.html", {"teams": teams})

@require_POST
def add_points(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    # cada acierto suma 10 
    team.points += 10
    team.save()
    # Si la solicitud viene por HTMX, devolvemos solo fragmento de scores
    return render(request, "scoreboard/_scores.html", {"teams": Team.objects.all().order_by("id")})

@require_POST
def reset_scores(request):
    Team.objects.all().update(points=0)
    return render(request, "scoreboard/_scores.html", {"teams": Team.objects.all().order_by("id")})

@require_POST
def subtract_points(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.points = max(0, team.points - 10)  # no baja de 0
    team.save()
    return render(request, "scoreboard/_scores.html", {"teams": Team.objects.all().order_by("id")})

