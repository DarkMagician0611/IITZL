from django.contrib import admin
from .models import BatRecord, BallRecord, FieldRecord, PlayedRecord
# Register your models here.
admin.site.register(BatRecord)
admin.site.register(BallRecord)
admin.site.register(FieldRecord)
admin.site.register(PlayedRecord)