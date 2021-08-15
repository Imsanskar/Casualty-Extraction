from django.db import models
from  datetime import date

#all datafields related to the news
class rssdata(models.Model):
	id = models.AutoField(primary_key=True)
	header = models.CharField(blank=True, max_length=200,unique_for_date=True)
	body = models.TextField(blank=False, null=False,unique_for_date=True)
	source = models.CharField(blank=True, max_length=200, null=True)
	death = models.CharField(blank=True, max_length=200, null=True)
	death_no = models.IntegerField(default=0,blank=True, null=True)
	injury = models.CharField(blank=True, max_length=200, null=True)
	injury_no = models.IntegerField(default=0,blank=True, null=True)
	location = models.CharField(blank=True, max_length=200, null=True)
	
	date = models.CharField(default=date.today, blank=True, null=True,max_length=100)
	link = models.CharField(blank=True, max_length=200, null=True)
   
	month = models.CharField(blank=True, max_length=200, null=True)
	year = models.CharField(blank=True, max_length=200, null=True)
	day = models.CharField(blank=True, max_length=200, null=True)


	#vehicle data
	vehicleNo = models.CharField(blank=True, max_length=200, null=True)
	vehicleCode = models.CharField(blank=True, max_length=200, null=True)
	vehicleType = models.CharField(blank=True, max_length=300, null=True) 


	# Timestamps for news object created
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'rssdata' #human readable alias for object
		ordering = ('-date', 'location') #sorting type in list


#override default save method 
	def save(self, *args, **kwargs):
		super(rssdata, self).save(*args, **kwargs)


#Just to identify the object by its header
	def __str__(self):
		return self.header

