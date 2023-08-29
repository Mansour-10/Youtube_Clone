from django.contrib import admin
from .models import membership

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "Monthly_fee", "joined_date",)
  
admin.site.register(membership, MemberAdmin)