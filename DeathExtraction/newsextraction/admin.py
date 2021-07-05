from newsextraction.models import rssdata
from django.contrib import admin
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","link","header","source","body","death","death_no","injury","injury_no","location","date","day","month","year","created_at","updated_at",]

    #list_display_links = ["updated"]


    class Meta:
        model = rssdata
admin.site.register(rssdata, PostModelAdmin)