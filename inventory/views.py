from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Equipment


@login_required
def equipment_list(request):
    devices = Equipment.objects.select_related('owner').all()
    return render(request, 'inventory/equipment_list.html', {'devices': devices})
