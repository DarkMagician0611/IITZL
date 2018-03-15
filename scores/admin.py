from django.contrib import admin
from .models import BatRecord, BallRecord, FieldRecord
# Register your models here.
admin.site.register(BatRecord)
admin.site.register(BallRecord)
admin.site.register(FieldRecord)