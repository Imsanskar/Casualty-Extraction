from django.db import models
from  datetime import date

#all datafields related to the news
class rssdata(models.Model):
    header = models.CharField(blank=True, max_length=200)
    body = models.TextField(blank=False, null=False)
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


    # Timestamps for news object created
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'rssdata'
        ordering = ('-date', 'location')

    def save(self, *args, **kwargs):
        super(rssdata, self).save(*args, **kwargs)

    def __str__(self):
        return self.header

