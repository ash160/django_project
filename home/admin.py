from django.contrib import admin
from .models import Salary,Address,Personal,Otherincome,House_property,Deduction,More_deduction,Tds,DocumentUpload

# Register your models here.
admin.site.register(Personal)
admin.site.register(Address)
admin.site.register(Salary)
admin.site.register(Otherincome)
admin.site.register(House_property)
admin.site.register(Deduction)
admin.site.register(More_deduction)
admin.site.register(Tds)
admin.site.register(DocumentUpload)





