from django.shortcuts import render_to_response
import sys,datetime

#from django.db import models
#from ops_platform.models import Server
#servers_list = VirtualServer.objects.all()
def get_project():
	from serverlists.projectlist import Projectlist
	return Projectlist

def get_apps(request,ProjectName):
	project_list = get_project()
	if ProjectName not in project_list:
		print "[ERROR] no %s project." % ProjectName
		sys.exit()
	impstr = 'from serverlists.%s import Applist' % ProjectName
	exec(impstr)
	template_name = "update/%s.html" % ProjectName
	return render_to_response(template_name, {'apps':apps})

def get_servers(request,ProjectName,AppName):
	impstr = 'from serverlists.%s import Hostlist,Applist' % ProjectName
	exec(impstr)
	template_name = "update/%s/%s.html" % (ProjectName,AppName)
	return render_to_response(template_name, {'servers':servers,'apps':apps})