from django.shortcuts import render_to_response
import sys,datetime

def project_update(request,projectName):
	project_list = ('bshare','lezhi','ads')
	if projectName not in project_list:
		print "[ERROR] no %s project." % projectName
		sys.exit()
	
	servers = ('button1','button2','button3')
	template_name = "update/%s.html" % projectName
	return render_to_response(template_name, {'servers':servers})