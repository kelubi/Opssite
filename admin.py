from django.contrib import admin
from django.db import connection
from ops_release.models import Project, Mode , App , Host
import sys

"""
Add class Rsyncer.
"""
script_path = '/var/www/sites/djcode/opssite/ops_release/scrpits'
if script_path not in sys.path:
    sys.path.append(script_path)
    from rsync_model import Rsyncer

def print_log(*n):
    """
    For code debug.
    """
    f = open('/var/www/sites/djcode/opssite/ops_release/out.txt', 'a')
    print >>f,n
    f.write("\n\n")
    f.close()

def get_app_unique(hosts):
    """
    In the same time,only one app can run.Otherwise,raise error.
    """
    apps = []
    [ apps.append(host['app_id']) for host in hosts if not host['app_id'] in apps ]
    if len(apps) == 1:
	return apps[0]
    else:
	sys.exit()

def release_filter(queryset):
    """
    Filter info from queryset and return.
    """
    hosts = queryset.values()
    app_id = get_app_unique(hosts)
    app = App.objects.filter(id=app_id).values()[0]
    hosts_ips = []
    [ hosts_ips.append(host['ip']) for host in hosts ]
    return app, hosts_ips, app['restart_file']

def release_status(pdo, mode_name, app_id, hosts_ips):
    """
    Check and update status of release.
    """
    if pdo == 'do':
	for ip in hosts_ips:
	    status = Host.objects.filter(ip=ip, app_id=app_id).values()[0]['status']
	    if status != '':sys.exit()
	    Host.objects.filter(ip=ip, app_id=app_id).update(status=mode_name)
    if pdo == 'done':
	for ip in hosts_ips:
	    Host.objects.filter(ip=ip, app_id=app_id).update(status=mode_name)

def release_shell(pmode, app, hosts_ips, restart_file=''):
    """
    Processing patameters,then running remote python script.
    """
    print_log(restart_file)
    mode = Mode.objects.filter(name=pmode).values()[0]
    source = app[mode['source_dir']]
    target = app[mode['target_dir']]
    release_status('do' ,mode['name'], app['id'], hosts_ips)
    r = Rsyncer(mode['type'], source, target, hosts_ips, restart_file)
    r.rsyncer_ctl()
    release_status('done', '', app['id'], hosts_ips)

def release_send(modeladmin, request, queryset):
    app, hosts_ips, restart_file = release_filter(queryset)
    release_shell('send', app, hosts_ips)

def release_backup(modeladmin, request, queryset):
    app, hosts_ips, restart_file = release_filter(queryset)
    release_shell('backup', app, hosts_ips)

def release_update(modeladmin, request, queryset):
    app, hosts_ips, restart_file = release_filter(queryset)
    release_shell('update', app, hosts_ips, restart_file)

def release_rollback(modeladmin, request, queryset):
    app, hosts_ips, restart_file = release_filter(queryset)
    release_shell('rollback', app, hosts_ips, restart_file)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ModeAdmin(admin.ModelAdmin):
    list_display = ('name','type','source_dir','target_dir')

class AppAdmin(admin.ModelAdmin):
    list_display = ('name','project','source_dir','update_dir','backup_dir','working_dir','restart_file') 
    list_filter = ('project',)
    search_fields = ('name',)
    ordering = ('project__name',)

class HostAdmin(admin.ModelAdmin):
    list_display = ('name','project','app','ip','status')
    list_filter = ('project','app',)
    search_fields = ('name', 'ip', 'project__name','app__name',)
    ordering = ('project__name','app__name','name',)
    actions = [release_send, release_backup, release_update, release_rollback]
    
admin.site.disable_action('delete_selected')
admin.site.register(Project,ProjectAdmin)
admin.site.register(Mode,ModeAdmin)
admin.site.register(App,AppAdmin)
admin.site.register(Host,HostAdmin)
