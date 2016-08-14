from django.contrib import admin
from poll.models import Bill_Milk,Miss,Missed


class Bill_MilkAdmin(admin.ModelAdmin):
	pass
admin.site.register(Bill_Milk,Bill_MilkAdmin)
class MissAdmin(admin.ModelAdmin):
	pass
admin.site.register(Miss,MissAdmin)



