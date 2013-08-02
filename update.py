from django.shortcuts import render_to_response
import sys,datetime

def project_update(request,projectName):
	project_list = ('bshare','lezhi','ads')
	if projectName not in project_list:
		print "[ERROR] no %s project." % projectName
		sys.exit()
	servers = get_servers()
	template_name = "update/%s.html" % projectName
	return render_to_response(template_name, {'servers':servers})

#from django.db import models
#from ops_platform.models import Server
def get_servers():
	#servers_list = VirtualServer.objects.all()
	pass