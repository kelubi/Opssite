from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    comments = models.CharField(max_length=50,blank=True,null=True)

    def __unicode__(self):
        return self.name

class Mode(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    source_dir = models.CharField(max_length=30)
    target_dir = models.CharField(max_length=30)
    comments = models.CharField(max_length=50,blank=True,null=True)

    def __unicode__(self):
        return self.name

class App(models.Model):
    #Restart_Choices = (
    #	(u'restart', u'restart'),
    #	(u'false', u'false'),     
    #	) 
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project)
    source_dir = models.TextField()
    update_dir = models.TextField()
    backup_dir = models.TextField()
    working_dir = models.TextField()
    #update = models.CharField(max_length=10, choices=Restart_Choices)
    #rollback = models.CharField(max_length=10, choices=Restart_Choices)
    restart_file = models.CharField(max_length=50,blank=True,null=True)
    comments = models.CharField(max_length=50,blank=True,null=True)
    
    def __unicode__(self):
        return self.name 

class Host(models.Model):
    name = models.CharField(max_length=30)
    ip = models.IPAddressField(max_length=30)
    project = models.ForeignKey(Project)
    app = models.ForeignKey(App)
    status = models.CharField(max_length=30,blank=True,null=True)
    comments = models.CharField(max_length=50,blank=True,null=True)

    def __unicode__(self):
        return self.name
