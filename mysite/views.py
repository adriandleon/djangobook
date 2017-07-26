from django.shortcuts import render, Http404
from datetime import datetime, timedelta


def current_datetime(request):
    now = datetime.now()
    return render(request, 'mysite/current_datetime.html',
    {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404
    dt = datetime.now() + timedelta(hours=offset)
    return render(request, 'mysite/hours_ahead.html', {
        'hours_offset': offset, 'next_time': dt
    })
