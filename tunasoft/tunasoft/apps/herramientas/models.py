from django.db import models

# Create your models here.
class herramienta(models.Model):
	nombre	= models.CharField(max_length=50)
	url		= models.URLField()
	status	= models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre