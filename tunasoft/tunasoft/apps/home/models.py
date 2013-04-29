from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	def url(self,filename):
		ruta = "Users/%s/%s"%(self.user.username,filename)
		return ruta

	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to=url)
	descripcion = models.TextField(max_length=300)

	def __unicode__(self):
		return self.user.username