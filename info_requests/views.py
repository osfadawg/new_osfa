from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'info_requests/home.html')

@login_required
def form(request, action, id):
    allowed = ["add", "view", "edit", "delete"]
    if action not in allowed:
        raise Http404("'Invalid action")
    
    return render(
        request, 
        'info_requests/form.html',
        {
            "action": action,
            "id": id
        }
    )