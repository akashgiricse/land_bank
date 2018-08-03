from django.contrib import admin
from .models import Village, Plot
# Register your models here.


class VillageAdmin(admin.ModelAdmin):
	model = Village
	list_display = ['name', 'code']
	search_fields = ['name', 'code']


class PlotAdmin(admin.ModelAdmin):
	model = Plot
	list_display = ['gata_number', 'village','connectivity', 'allotted', 'shreni']
	list_filter = ['connectivity', 'allotted', 'shreni']
	search_fields = ['village__name','gata_number']


admin.site.register(Village, VillageAdmin)
admin.site.register(Plot, PlotAdmin)
