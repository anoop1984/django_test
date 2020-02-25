from django.contrib import admin
from .models import healthCheck


"""
class healthcheckAdmin(admin.ModelAdmin):
    list_display =  ('id', 'date','test_id', 'desc', 'severity', 'ipaddr', 'hostname', 'command', 'verdict','remarks')
    #list_display_links = ('id', 'test_id')
    list_filter = ('test_id', 'hostname','date')
    search_fields = ('date','test_id', 'hostname' , 'ipaddr', 'command', 'verdict' , 'severity')
#admin.site.register(healthCheck,healthcheckAdmin)
admin.site.register(healthCheck, healthcheckAdmin)

"""


class healthcheckAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_display =  ('id', 'date','test_id', 'desc', 'severity', 'ipaddr', 'hostname', 'command', 'verdict','remarks')
    #list_display_links = ('id', 'test_id')
    list_filter = ('test_id', 'hostname','date')
    search_fields = ('date','test_id', 'hostname' , 'ipaddr', 'command', 'verdict' , 'severity')
#admin.site.register(healthCheck,healthcheckAdmin)
admin.site.register(healthCheck, healthcheckAdmin)
