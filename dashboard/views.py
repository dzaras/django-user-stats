from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.functions import TruncDate
from django.db.models import Count
from datetime import datetime

from django.shortcuts import render

def user_stats_page(request):
    return render(request, 'dashboard/user_stats.html')


def user_stats(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    queryset = User.objects.all()

    if start:
        queryset = queryset.filter(date_joined__gte=start)
    if end:
        queryset = queryset.filter(date_joined__lte=end)

    data = (
        queryset
        .annotate(day=TruncDate('date_joined'))
        .values('day')
        .annotate(count=Count('id'))
        .order_by('day')
    )

    return JsonResponse(list(data), safe=False)
