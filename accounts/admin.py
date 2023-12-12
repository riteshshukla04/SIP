from django.contrib import admin
from .models import SIP
from django.contrib.auth.models import Group,User

class SIPAdmin(admin.ModelAdmin):
    list_display = ('id', 'nameofSIP', 'holderName', 'sipAmount', 'dateOfRenewel')
    search_fields = ('nameofSIP', 'holderName')
    list_filter = ('holderName', 'dateOfRenewel')

admin.site.register(SIP,SIPAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
