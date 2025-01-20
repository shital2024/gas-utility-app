from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def create_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_status', pk=service_request.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})

def request_status(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk, user=request.user)
    return render(request, 'service_requests/request_status.html', {'service_request': service_request})
