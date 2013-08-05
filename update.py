from django.shortcuts import render_to_response
import sys,datetime

#from django.db import models
#from ops_platform.models import Server
#servers_list = VirtualServer.objects.all()
def get_project():
	from serverlists.projectlist import Projectlist
	return Projectlist

def get_servers(projectName):
	impstr = 'from serverlists.%s import Hostlist,Applist' % projectName
	exec(impstr)
	return Hostlist,Applist

def project_update(request,projectName):
	project_list = get_project()
	if projectName not in project_list:
		print "[ERROR] no %s project." % projectName
		sys.exit()
	servers,app = get_servers(projectName)
	template_name = "update/%s.html" % projectName
	return render_to_response(template_name, {'servers':servers,'app':app})