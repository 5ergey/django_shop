from django.shortcuts import render
from django.views import generic

# Create your views here.
class AdminDashboardView(generic.TemplateView):
    pass

class AdminStatsView(generic.TemplateView):
    pass

class AdminSearchView(generic.TemplateView):
    pass

class AdminPermissionsView(generic.TemplateView):
    pass