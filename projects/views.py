from django.shortcuts import render
from django.db.models import Q
from django.views.generic import DetailView
from .models import Program

def program(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    programs = get_program_queryset(query)
    
    context['programs'] = programs
    return render(request, "projects/projects.html", context)

class ProgramDetailView(DetailView):
    model = Program

def get_program_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        programs = Program.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(tag__icontains=q)
        ).distinct()

        for program in programs:
            queryset.append(program)

    return list(set(queryset))

def compro_time_series(request):
    return render(request, "projects/compro_sta257.html")

def compro_factor_analysis(request):
    return render(request, "projects/compro_csc356.html")
