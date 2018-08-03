from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Village(models.Model):
	name = models.CharField(_('गांव का नाम'), max_length=100, default=None)
	code = models.IntegerField(_('गांव कोड'), default=None)

	def __str__(self):             
	    return "%s" % (self.name)


class Plot(models.Model):
	village = models.ForeignKey(Village, on_delete=models.CASCADE)

	SHRENI_CHOICES = (
		('5', '5'),
		('6', '6')
	)
	shreni = models.CharField(_('श्रेणी'),max_length=1, choices=SHRENI_CHOICES)
	gata_number = models.CharField(_('गाटा संख्या'), max_length=50, default=None)
	area = models.FloatField(_('क्षेत्रफल (हैक्‍टेयर)'),default=None)
	distance_road = models.FloatField(_('सड़क से दूरी (कि.मी.)'), default=None)
	connectivity = models.BooleanField(_('कनेक्टिविटी'))
	allotted = models.BooleanField(_('आवंटित'), default=False)
	latitude_coordinate = models.CharField(_('अक्षांश निर्देशांक'), max_length=15, default=None)
	longitude_coordinate = models.CharField(_('देशांतर निर्देशांक'), max_length=15, default=None)
	image1 = models.ImageField(upload_to='images/', null=True, blank=True)
	image2 = models.ImageField(upload_to='images/', null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True, editable=False)
	modified_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s" %(self.gata_number)
    