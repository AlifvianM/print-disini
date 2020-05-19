from django.contrib import admin
from .models import Print, Jilid, Pemesanan, Pengambilan, Status, CheckOut
# Register your models here.


admin.site.register(Print)
admin.site.register(Jilid)
admin.site.register(Pemesanan)
admin.site.register(Pengambilan)
admin.site.register(Status)
admin.site.register(CheckOut)
