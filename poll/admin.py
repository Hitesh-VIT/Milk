from django.contrib import admin
from poll.models import *


class Bill_MilkAdmin(admin.ModelAdmin):
	pass
admin.site.register(Bill_Milk,Bill_MilkAdmin)
class MissAdmin(admin.ModelAdmin):
	pass
admin.site.register(Miss,MissAdmin)
class ProfileAdmin(admin.ModelAdmin):
	pass
admin.site.register(Profile,ProfileAdmin)
class MissedAdmin(admin.ModelAdmin):
	pass
admin.site.register(Missed,MissedAdmin)


