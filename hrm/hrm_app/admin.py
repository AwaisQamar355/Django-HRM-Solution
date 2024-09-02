from django.contrib import admin
from .models import Employe
from .models import Designation
from .models import Department
from .models import Employeeducation
from .models import Employeentitlement
from .models import Employedepartment
from .models import Employeattendance

# Register your models here.

class EmployeeducationTublerinline(admin.TabularInline):
    model = Employeeducation
class EmployeentitlementTublerinline(admin.TabularInline):
    model = Employeentitlement
class EmployedepartmentTublerinline(admin.TabularInline):
    model = Employedepartment
class EmployeattendanceTublerinline(admin.TabularInline):
    model = Employeattendance

class Employedataadmin(admin.ModelAdmin):
    inlines = [EmployeeducationTublerinline , EmployeentitlementTublerinline , EmployedepartmentTublerinline
               , EmployeattendanceTublerinline]


admin.site.register(Employe , Employedataadmin)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(Employeeducation)
admin.site.register(Employeentitlement)
admin.site.register(Employedepartment)
admin.site.register(Employeattendance)


