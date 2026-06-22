from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from library import common

@login_required
def home(request):
    return render(request, 'info_requests/home.html')

@login_required
def form(request, action, id=None):
    allowed = ["add", "view", "edit", "delete"]
    if action not in allowed:
        raise Http404("'Invalid action")
    
    context = ""
    
    if id: #    VIEW, EDIT, DELETE
        context = {
            "action": action,
            "id": id
        }
    else: #    ADD
        context = {
            "action": action,
            "new_number": str(common.get_next_request_number('2026'))
        }
        #   GET NEW NUMBER
        
    
    return render(
        request, 
        'info_requests/form.html',
        context=context
    )