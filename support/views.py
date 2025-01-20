from django.shortcuts import render, get_object_or_404
from service_requests.models import ServiceRequest

def dashboard(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'support/dashboard.html', {'requests': requests})

def manage_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == "POST":
        service_request.status = request.POST.get('status')
        service_request.save()
        return redirect('support_dashboard')
    return render(request, 'support/manage_request.html', {'service_request': service_request})
