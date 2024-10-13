from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard_index(request):
    template_name = 'dashboard/dashboard.html'
    context = {
        'page_name': 'Панель управления',
    }
    return render(request, template_name, context)
