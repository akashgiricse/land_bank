from django.contrib import admin
from .models import Village, Plot, Shreni
from django.http import HttpResponse

import csv
import datetime
import random

# Register your models here.


class VillageAdmin(admin.ModelAdmin):
    model = Village
    list_display = ['name', 'code']
    search_fields = ['name', 'code']


class ShreniAdmin(admin.ModelAdmin):
    model = Shreni
    list_display = ['shreni', 'shreni_description']
    search_fields = ['shreni', 'shreni_description']


class PlotAdmin(admin.ModelAdmin):
    model = Plot
    actions = ['download_csv', 'download_excel']
    list_display = ['gata_number', 'village', 'connectivity', 'allotted', 'shreni', 'area', 'distance_road']
    list_filter = ['connectivity', 'allotted', 'shreni']
    search_fields = ['village__name', 'gata_number']

    def download_csv(self, request, queryset):

        now = datetime.datetime.now()

        f = open('some.csv', 'w')
        writer = csv.writer(f)

        writer.writerow(['gata_number', 'village', 'connectivity', 'allotted', 'shreni', 'area', 'distance_road'])

        for s in queryset:
            writer.writerow([s.gata_number, s.village, s.connectivity, s.allotted, s.shreni, s.area, s.distance_road])

        f.close()

        name = str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "--" + str(random.randint(1, 10000)) + ".csv"

        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + name
        return response

    download_csv.short_description = "Download CSV file."

    def download_excel(self, request, queryset):
        import xlwt

        now = datetime.datetime.now()
        name = str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "--" + str(random.randint(1, 10000)) + ".xls"

        # content-type of response
        response = HttpResponse(content_type='application/ms-excel')

        # decide file name
        response['Content-Disposition'] = 'attachment; filename=' + name

        # creating workbook
        wb = xlwt.Workbook(encoding='utf-8')

        # adding sheet
        ws = wb.add_sheet("sheet1")

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        # headers are bold
        font_style.font.bold = True

        # column header names, you can use your own headers here
        columns = ['No', 'gata_number', 'connectivity', 'allotted', 'shreni', 'area', 'distance_road', ]

        # write column headers in sheet
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        row_num = 1
        for s in queryset:
            row_num = row_num + 1
            # [s.gata_number, s.village, s.connectivity, s.allotted, s.shreni, s.area, s.distance_road]
            ws.write(row_num, 0, row_num-1, font_style)
            ws.write(row_num, 1, s.gata_number, font_style)
            # ws.write(row_num, 2, s.village, font_style)
            ws.write(row_num, 2, s.connectivity, font_style)
            ws.write(row_num, 3, s.allotted, font_style)
            ws.write(row_num, 4, s.shreni, font_style)
            ws.write(row_num, 5, s.area, font_style)
            ws.write(row_num, 6, s.distance_road, font_style)

        wb.save(response)
        return response

    download_excel.short_description = "Download Excel file."


admin.site.register(Village, VillageAdmin)
admin.site.register(Plot, PlotAdmin)
admin.site.register(Shreni, ShreniAdmin)
