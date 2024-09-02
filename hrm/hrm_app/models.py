from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Designation(models.Model):
    desig_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    descraption = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='designation_created_by', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='designation_updated_by', on_delete=models.CASCADE)
    enabled_status = models.TextField()

    def __str__(self):
        return self.name

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    descraption = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='department_created_by', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='department_updated_by', on_delete=models.CASCADE)
    enabled_status = models.TextField()

    def __str__(self):
        return self.name



class Employe(models.Model):
    employe_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    father_name = models.CharField(max_length=155 ,blank=True, null=True)
    cnic_nu = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    blood_group = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    dateofbirth = models.DateField()
    marital_status = models.CharField(max_length=250)
    passport_no = models.CharField(max_length=155)
    is_pf_member = models.CharField(max_length=155)
    is_ss_member = models.CharField(max_length=155)
    dateofconfirmation = models.DateField()
    date_of_joining = models .DateField()
    bankname = models.CharField(max_length=255)
    accountnumber = models.IntegerField()
    relation_name = models.CharField(max_length=200)
    relation_phonenum = models.CharField(max_length=200)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='media/images' , default="")

    def __str__(self):
        return self.first_name
class Employeeducation(models.Model):
    education_id = models.AutoField(primary_key=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    certificate_title = models.CharField(max_length=255)
    institute = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.certificate_title

class Employeentitlement(models.Model):
    entitlement_id = models.AutoField(primary_key=True)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    basic_pay = models.CharField(max_length=255)
    conveyance_all = models.CharField(max_length=255)
    medical = models.CharField(max_length=255)
    utilities = models.CharField(max_length=255)
    cola = models.CharField(max_length=255)
    gross_pay = models.CharField(max_length=255)
    effective_date = models.DateField()
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.basic_pay

class Employedepartment(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    effectiv_date = models.DateField()

    

class Employeattendance(models.Model):
    month = models.CharField(max_length=200)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    days_worked = models.PositiveIntegerField()
    def __str__(self):
        return self.month

