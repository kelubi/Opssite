from django.shortcuts import render_to_response
import datetime

def project_update(request):
    servers = ('button1', 'button2', 'button3')
    return render_to_response('update/list.html', {'servers': servers})

