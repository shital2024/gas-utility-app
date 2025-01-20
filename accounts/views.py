from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def account_details(request):
    return render(request, 'accounts/account_details.html', {'user': request.user})
