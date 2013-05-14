from django.shortcuts import render
import datetime

def hello(request):
	return HttpResponse("Hello World")
	
def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', { 'current_date' : now })
	
def hours_ahead(request, offset):
	try: 
		offset = int(offset)
	except ValueError:
		raise Http404()
	now = datetime.datetime.now()
	soon = now + datetime.timedelta(hours=offset)
	return render(request, 'hours_ahead.html', { 
		'current_date' : now,
		'next_time' : soon,
		'hour_offset' : offset 
		}
	)