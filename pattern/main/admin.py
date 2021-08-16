from django.contrib import admin
from .models import Process
#from .models import *

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields

from .models import Post

from import_export.admin import ImportExportModelAdmin
 
#admin.site.register(Post)

@admin.register(Post)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'activity_count', 'mean_time', 'activity_from', 'activity_to')