from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from .models import Employe
from datetime import datetime
from django.contrib import messages
from .models import Designation
from .models import Department
from django.contrib.auth.models import User
from .models import Employeeducation
from .models import Employeentitlement
from .models import Employedepartment
from .models import Employeattendance
# Create your views here    

def home(request): 
    HttpResponse("WelCome to the home page")
    return render(request , 'home.html')
def employe_add(request):
    HttpResponse("WelCome to the home page")
    designation = Designation.objects.all()
    department = Department.objects.all()
    # employe = Employe.objects.all()
    # employeattendance = Employeattendance.objects.all()
    # employedepartment = Employedepartment.objects.all()
    # employeeducation = Employeattendance.objects.all()
    # employeentitlement = Employeentitlement.objects.all()


    context = {
        'designation':designation,
        'department' :department,          
        # 'employe': employe,
        # 'employeattendance': employeattendance,
        # 'employedepartment': employedepartment,
        # 'employeeducation': employeeducation,
        # 'employeentitlement': employeentitlement,
    }
    if request.method == "POST":
        employe_id = request.POST.get('employe_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        cnic_nu = request.POST.get('cnic_nu')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        blood_group = request.POST.get('blood_group')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        passport_no = request.POST.get('passport_no')  
        is_pf_member = request.POST.get('is_pf_member')
        is_ss_member = request.POST.get('is_ss_member')
        dateofconfirmation = request.POST.get('dateofconfirmation')
        relation_name = request.POST.get('relation_name')
        relation_phonenum = request.POST.get('relation_phonenum')
        designation_id = request.POST.get('designation')
        date_of_joining = request.POST.get('date_of_joining')
        dateofbirth = request.POST.get('dateofbirth')
        department_id = request.POST.get('department')
        status = request.POST.get('status')
        accountnumber = request.POST.get('accountnumber')
        bankname = request.POST.get('bankname')
        profile_picture = request.FILES.get('profile_picture')
        
        designation = get_object_or_404(Designation, pk=designation_id)
        department = get_object_or_404(Department, pk=department_id)
        # employe = get_object_or_404(Employe, pk=employe_id)

        # employe_id = request.POST.get('employe')
        # education_id = request.POST.get('education_id')
        # certificate_title = request.POST.get('certificate_title')
        # institute = request.POST.get('institute')
        # from_date = request.POST.get('form_date')
        # to_date = request.POST.get('to_date')
        # entitlement_id = request.POST.get('entitlement_id')
        # employe_id = request.POST.get('employe')
        # basic_pay = request.POST.get('basic_pay')
        # conveyance_all = request.POST.get('conveyance_all')
        # medical = request.POST.get('medical')
        # utilities = request.POST.get('utilities')
        # cola = request.POST.get('cola')
        # gross_pay = request.POST.get('gross_pay')
        # effective_date = request.POST.get('effective_date')
        # designation_id = request.POST.get('designation')
        # employe_id = request.POST.get('employe')
        # department_id = request.POST.get('dept_id')
        # effectiv_date = request.POST.get('effectiv_date')
        # employe_id = request.POST.get('employe')
        # month = request.POST.get('month') 
        # days_worked = request.POST.get('days_worked')



        


        if Employe.objects.filter(employe_id=employe_id).exists():
            messages.error(request, 'Company ID already exists!')        
            return render(request, 'employe_add.html')
        else: 
            
            employe = Employe.objects.create(first_name = first_name , last_name = last_name ,
                      email = email , phone_number = phone_number , department = department , 
                               designation = designation , date_of_joining = date_of_joining,
                               dateofbirth = dateofbirth , status = status,
                               father_name = father_name , accountnumber = accountnumber, bankname = bankname,
                              cnic_nu = cnic_nu ,blood_group = blood_group ,
                                gender =gender , marital_status = marital_status , passport_no = passport_no,
                                is_pf_member = is_pf_member , is_ss_member = is_ss_member , dateofconfirmation = dateofconfirmation,
                                relation_name = relation_name , relation_phonenum = relation_phonenum,
                                  profile_picture = profile_picture )
                
            messages.success(request, 'Employe added successfully!')
            return redirect('employe_education')


                
    return render(request , 'employe_add.html' , context)

# def employe_delete(request,pk):
#     HttpResponse("WelCome to the home page")
#     employe = get_object_or_404(Employe,pk=pk)
#     if request.method == "POST":
#         employe.delete()
#         return redirect('employe_list')
#     return render(request , 'employe_delete.html' , {'employe': employe})
def employe_list(request):
    HttpResponse("WelCome to the home page")
    employe = Employe.objects.all()
    employeattendance = Employeattendance.objects.all()
    employedepartment = Employedepartment.objects.all()
    employeeducation = Employeattendance.objects.all()
    employeentitlement = Employeentitlement.objects.all()
    
    context = {
        'employe': employe,
        'employeattendance': employeattendance,
        'employedepartment': employedepartment,
        'employeeducation': employeeducation,
        'employeentitlement':employeentitlement,
    }
    return render(request , 'employe_list.html',context)
# def employe_update(request,employe_id):
#     HttpResponse("WelCome to the home page")
#     employe = get_object_or_404(Employe, employe_id=employe_id)
#     designation = Designation.objects.all()
#     department = Department.objects.all()

#     if request.method == "POST":
#         employe.first_name = request.POST['first_name']
#         employe.last_name = request.POST['last_name']
#         employe.email = request.POST['email']
#         employe.phone_number = request.POST['phone_number']
#         # employe.department = request.POST['department']
#         employe.father_name = request.POST['father_name']
#         employe.cnic_nu = request.POST['cnic_nu']
#         employe.blood_group = request.POST['blood_group']
#         employe.gender = request.POST['gender']
#         employe.marital_status = request.POST['marital_status']
#         employe.passport_no = request.POST['passport_no']
#         employe.is_pf_member = request.POST['is_pf_member']
#         employe.is_ss_member = request.POST['is_ss_member']
#         employe.dateofconfirmation = request.POST['dateofconfirmation']
#         employe.relation_name = request.POST['relation_name']
#         employe.relation_phonenum = request.POST['relation_phonenum']
#         designation_id = request.POST['designation']
#         department_id = request.POST['department']
#         employe.date_of_joining = request.POST['date_of_joining']
#         employe.status = request.POST['status']
#         employe.accountnumber = request.POST['accountnumber']
#         employe.bankname = request.POST['bankname']
#         employe.dateofbirth = request.POST['dateofbirth']
#         employe.profile_picture = request.POST['profile_picture']
#         employe.designation = get_object_or_404(Designation, pk=designation_id)
#         employe.department = get_object_or_404(Department, pk=department_id)


  
#         if 'profile_picture' in request.FILES:   
#             employe.profile_picture = request.FILES['profile_picture']
#         employe.save()
#         return redirect('employeeducation_update')
        
#     context = {
#             'employe': employe,
#             'designation':designation,
#             'department' :department,

#     }

#     return render(request , 'employe_update.html' , context)



def employe_update(request, employe_id):
    employe = get_object_or_404(Employe, employe_id=employe_id)
    designation = Designation.objects.all()
    department = Department.objects.all()

    if request.method == "POST":
        employe.first_name = request.POST['first_name']
        employe.last_name = request.POST['last_name']
        employe.email = request.POST['email']
        employe.phone_number = request.POST['phone_number']
        employe.father_name = request.POST['father_name']
        employe.cnic_nu = request.POST['cnic_nu']
        employe.blood_group = request.POST['blood_group']
        employe.gender = request.POST['gender']
        employe.marital_status = request.POST['marital_status']
        employe.passport_no = request.POST['passport_no']
        employe.is_pf_member = request.POST['is_pf_member']
        employe.is_ss_member = request.POST['is_ss_member']
        employe.dateofconfirmation = request.POST['dateofconfirmation']
        employe.relation_name = request.POST['relation_name']
        employe.relation_phonenum = request.POST['relation_phonenum']
        designation_id = request.POST['designation']
        department_id = request.POST['department']
        employe.date_of_joining = request.POST['date_of_joining']
        employe.status = request.POST['status']
        employe.accountnumber = request.POST['accountnumber']
        employe.bankname = request.POST['bankname']
        employe.dateofbirth = request.POST['dateofbirth']

        if 'profile_picture' in request.FILES:
            employe.profile_picture = request.FILES['profile_picture']
        
        employe.designation = get_object_or_404(Designation, pk=designation_id)
        employe.department = get_object_or_404(Department, pk=department_id)

        employe.save()

        employeeducation = Employeeducation.objects.filter(employe=employe).first()
        if employeeducation:
            employeeducation_id = employeeducation.education_id  # Use the correct field name
        else:
            # Handle the case where no Employeeducation instance is found
            employeeducation_id = None

        if employeeducation_id:
        # Find the related Employeeducation instance
            return redirect('employeeducation_update',education_id=employeeducation_id)
        else:
            # Handle the case where redirection is not possible
            return redirect('some_default_url')  # Replace with your default URL
        

    context = {
        'employe': employe,
        'designation': designation,
        'department': department,
    }

    return render(request, 'employe_update.html', context)



# def employe_view(request):
#     HttpResponse("WelCome to the home page")
#     return render(request , 'employe_view.html')
def employe_detail(request,pk):
    HttpResponse("WelCome to the home page")
    employe = get_object_or_404(Employe, pk=pk)
    employeattendances= get_object_or_404(Employeattendance, pk=pk)
    employedepartments =get_object_or_404(Employedepartment, pk=pk)
    employeeducations = get_object_or_404(Employeeducation, pk=pk)
    employeentitlements = get_object_or_404(Employeentitlement, pk=pk)

    # employeattendances = Employeattendance.objects.filter(employe=employe)
    # employedepartments = Employedepartment.objects.filter(employe=employe)
    # employeeducations = Employeeducation.objects.filter(employe=employe)
    # employeentitlements = Employeentitlement.objects.filter(employe=employe)

   
    context = {
        'employe': employe,
        'employeattendances': employeattendances,
        'employedepartments': employedepartments,
        'employeeducations': employeeducations,
        'employeentitlements': employeentitlements,
    }

    return render(request, 'employe_detail.html', context)
    # return render(request , 'employe_detail.html' , {'employe': employe},{'employeattendance': employeattendance} , {'employedepartment': employedepartment} ,{'employeeducation', employeeducation} ,{'employeentitlement': employeentitlement})






def designation_add(request):
    HttpResponse("WelCome to the home page")
    if request.method == "POST":
        name = request.POST.get('name')

        designation_add = Designation(name = name)
        designation_add.save()
        return redirect('designation_list')
                
    return render(request , 'designation_add.html')





# def designation_delete(request,pk):
#     HttpResponse("WelCome to the home page")
#     designation = get_object_or_404(Designation,pk=pk)
#     if request.method == "POST":
#         designation.delete()
#         return redirect('designation_list')
#     return render(request , 'designation_delete.html' , {'designation': designation})


def designation_list(request):
    HttpResponse("WelCome to the home page")
    HttpResponse("WelCome to the home page")
    design = Designation.objects.all()

    context = {
        'design': design,
    }
    return render(request , 'designation_list.html',context)



def designation_update(request, designation_id):
    designation = get_object_or_404(Designation, pk=designation_id)

    if request.method == "POST":
        # designation.desig_id = request.POST['desig_id']
        designation.name = request.POST['name']
        # designation.created_on = request.POST['created_on']
        # designation.created_by = request.POST['created_by']
        # designation.updated_on = request.POST['updated_on']
        # designation.updated_by = request.POST['updated_by']
        designation.descraption = request.POST['descraption']
        designation.enabled_status = request.POST['enabled_status']
        
        designation.save()
        return redirect('designation_list')

    context = {
        'designation': designation,
    }

    return render(request, 'designation_update.html', context)
def designation_detail(request,pk):
    HttpResponse("WelCome to the home page")
    designation = get_object_or_404(Designation, pk=pk)
    return render(request , 'designation_detail.html' , {'designation': designation})


def designation_add(request):
    HttpResponse("WelCome to the home page")
    if request.method == "POST":
        desig_id = request.POST.get('desig_id')  # If dept_id is auto-generated, you may not need to handle this
        name = request.POST.get('name')
        created_by = User.objects.get(id=request.user.id)
        updated_by = User.objects.get(id=request.user.id)
        descraption = request.POST.get('descraption')
        enabled_status = request.POST.get('enabled_status')
        

        designation_add = Designation(name = name ,
                                      created_by = created_by , updated_by = updated_by ,
                                      descraption = descraption , enabled_status = enabled_status)
        designation_add.save()
        return redirect('designation_list')
                
    return render(request , 'designation_add.html')





# def designation_delete(request,pk):
#     HttpResponse("WelCome to the home page")
#     designation = get_object_or_404(Designation,pk=pk)
#     if request.method == "POST":
#         designation.delete()
#         return redirect('designation_list')
#     return render(request , 'designation_delete.html' , {'designation': designation})

# def designation_add(request):
#     HttpResponse("WelCome to the home page")
#     if request.method == "POST":
#         name = request.POST.get('name')

#         department_add = Designation(name = name)
#         department_add.save()
#         return redirect('designation_list')
                
#     return render(request , 'designation_add.html')






def department_list(request):
    HttpResponse("WelCome to the home page")
    HttpResponse("WelCome to the home page")
    dessign = Department.objects.all()

    context = {
        'dessign': dessign,
    }
    return render(request , 'department_list.html',context)



def department_update(request, department_id):
    department = get_object_or_404(Department, pk=department_id)

    if request.method == "POST":
        # department.dept_id = request.POST['dept_id']
        department.name = request.POST['name']
        # department.created_on = request.POST['created_on']
        # department.created_by = request.POST['created_by']
        # department.updated_on = request.POST['updated_on']
        # department.updated_by = request.POST['updated_by']
        department.descraption = request.POST['descraption']
        department.enabled_status = request.POST['enabled_status']
        
        department.save()
        return redirect('department_list')

    context = {
        'department': department,
    }

    return render(request, 'department_update.html', context)
def department_detail(request,pk):
    HttpResponse("WelCome to the home page")
    department = get_object_or_404(Department, pk=pk)
    return render(request , 'department_detail.html' , {'department': department})

     
def department_add(request):
    HttpResponse("WelCome to the home page")
    if request.method == "POST":
        dept_id = request.POST.get('dept_id')  # If dept_id is auto-generated, you may not need to handle this
        name = request.POST.get('name')
        descraption = request.POST.get('descraption')
        enabled_status = request.POST.get('enabled_status')
        created_by = User.objects.get(id=request.user.id)  # Ensure you set the correct user
        updated_by = User.objects.get(id=request.user.id)

        # Creating a new department instance
        department_add = Department(
            name=name,
            descraption=descraption,
            enabled_status=enabled_status,
            created_by=created_by,
            updated_by=updated_by
        )
        department_add.save()
        return redirect('department_list')
        
                
    return render(request , 'department_add.html')



# 











def employe_education(request):
    employe = Employe.objects.all()

    context = {
        'employe': employe,
    }
    if request.method == "POST":
        employe_id = request.POST.get('employe')
        education_id = request.POST.get('education_id')
        certificate_title = request.POST.get('certificate_title')
        institute = request.POST.get('institute')
        from_date = request.POST.get('form_date')
        to_date = request.POST.get('to_date')

        employe = get_object_or_404(Employe, pk=employe_id)
        


        if Employeeducation.objects.filter(education_id=education_id).exists():
            messages.error(request, 'Company ID already exists!')        
            return render(request, 'employe_add.html')
        else: 
            
            employes = Employeeducation.objects.create(
                               certificate_title = certificate_title , 
                                  institute = institute , from_date = from_date , to_date = to_date,
                                  employe = employe)
                
            messages.success(request, 'Employe added successfully!')
            return redirect('employe_entitlement')

    return render(request, 'employe_education.html',context)
def employe_entitlement(request):
    designation = Designation.objects.all()
    department = Department.objects.all()
    employe = Employe.objects.all()

    context = {
        'designation':designation,
        'department' :department,
        'employe': employe,
    }
    if request.method == "POST":
        entitlement_id = request.POST.get('entitlement_id')
        employe_id = request.POST.get('employe')
        basic_pay = request.POST.get('basic_pay')
        conveyance_all = request.POST.get('conveyance_all')
        medical = request.POST.get('medical')
        utilities = request.POST.get('utilities')
        cola = request.POST.get('cola')
        gross_pay = request.POST.get('gross_pay')
        effective_date = request.POST.get('effective_date')
        designation_id = request.POST.get('designation')


        employe = get_object_or_404(Employe, pk=employe_id)
        designation = get_object_or_404(Designation, pk=designation_id)
        


        if Employeentitlement.objects.filter(entitlement_id=entitlement_id).exists():
            messages.error(request, 'Company ID already exists!')        
            return render(request, 'employe_add.html')
        else: 
            
            employes = Employeentitlement.objects.create(
                               designation = designation  ,  basic_pay = basic_pay , 
                               conveyance_all = conveyance_all , 
                                  medical = medical ,utilities = utilities , cola = cola,
                                  gross_pay = gross_pay , effective_date = effective_date ,
                                  employe = employe)
                
            messages.success(request, 'Employe added successfully!')
            return redirect('employe_department')

    return render(request, 'employe_entitlement.html',context)

# def employe_department(request):
#     department = Department.objects.all()
#     employe = Employe.objects.all()
#     context = {
#         'department' :department,
#         'employe': employe,
#     }
#     if request.method == "POST":
#         employe_id = request.POST.get('employe')
#         department_id = request.POST.get('dept_id') 
#         effectiv_date = request.POST.get('effectiv_date')
#         employe = get_object_or_404(Employe, pk=employe_id)
#         department = get_object_or_404(Department, pk=department_id)

#         if Employedepartment.objects.filter().exists():
#             messages.error(request, 'Company ID already exists!')        
#             return render(request, 'employe_add.html')
#         else: 
#             employes = Employedepartment.objects.create(
#                                employe = employe  , department = department ,effectiv_date = effectiv_date 
#                                )
                
#             messages.success(request, 'Employe added successfully!')
#             return redirect('employe_attendance')
#     return render(request, 'employe_department.html',context)

def employe_department(request):
    if request.method == "POST":
        employe_id = request.POST.get('employe')
        department_id = request.POST.get('department')
        effectiv_date = request.POST.get('effectiv_date')

        employe = get_object_or_404(Employe, pk=employe_id)
        department = get_object_or_404(Department, pk=department_id)

        if Employedepartment.objects.filter(employe=employe, department=department).exists():
            messages.error(request, 'Employee is already assigned to this department!')
            return render(request, 'employe_department.html', context)

        Employedepartment.objects.create(
            employe=employe,
            department=department,
            effectiv_date=effectiv_date
        )

        messages.success(request, 'Employee assigned to department successfully!')
        return redirect('employe_attendance')

    department = Department.objects.all()
    employe = Employe.objects.all()
    context = {
        'department': department,
        'employe': employe,
    }
    return render(request, 'employe_department.html', context)


def employe_attendance(request):
    designation = Designation.objects.all()
    department = Department.objects.all()
    employe = Employe.objects.all()

    context = {
        'designation':designation,
        'department' :department,
        'employe': employe,
    }
    if request.method == "POST":
        employe_id = request.POST.get('employe')
        month = request.POST.get('month') 
        days_worked = request.POST.get('days_worked')
        employe = get_object_or_404(Employe, pk=employe_id)
        


        if Employeattendance.objects.filter(employe=employe).exists():
            messages.error(request, 'Company ID already exists!')        
            return render(request, 'employe_add.html')
        else: 
            
            employes = Employeattendance.objects.create(
                                       month= month , employe = employe  , days_worked = days_worked
                               )
                
            messages.success(request, 'Employe added successfully!')
            return redirect('employe_list')
    return render(request, 'employe_attendance.html' , context)












def employeeducation_update(request, education_id):
    employeeducation = get_object_or_404(Employeeducation, education_id=education_id)
    designation = Designation.objects.all()
    department = Department.objects.all()
    employee = Employe.objects.all()

    if request.method == "POST":
        employe_id = request.POST['employe']
        # employeeducation.education_id = request.POST['education_id']
        employeeducation.certificate_title = request.POST['certificate_title']
        employeeducation.institute = request.POST['institute']
        employeeducation.from_date = request.POST['form_date']
        employeeducation.to_date = request.POST['to_date']
        employeeducation.employe = get_object_or_404(Employe, pk=employe_id)
        
        employeeducation.save()
        return redirect('employeentitement_update', employeentitement_id=employeeducation.employe.pk)
    
    context = {
        'employeeducation': employeeducation,
        'designation': designation,
        'department': department,
        'employee': employee,
    }

    return render(request, 'employeeducation_update.html', context)



# def employeeducation_update(request,employeeducation_id):
#     HttpResponse("WelCome to the home page")
#     employe = get_object_or_404(Employeeducation, employeeducation_id=employeeducation_id)
#     designation = Designation.objects.all()
#     department = Department.objects.all()
#     employee = Employe.objects.all()

#     if request.method == "POST":
#         employe_id = request.POST['employe']
#         employe.education_id = request.POST['education_id']
#         employe.certificate_title = request.POST['certificate_title']
#         employe.institute = request.POST['institute']
#         employe.from_date = request.POST['form_date']
#         employe.to_date = request.POST['to_date']
#         # employe.designation = get_object_or_404(Designation, pk=designation_id)
#         # employe.department = get_object_or_404(Department, pk=department_id)
#         employe.employee = get_object_or_404(Employe, pk=employe_id)
        



#         employe.save()
#         return redirect('employeentitement_update')
        
#     context = {
#             'employe': employe,
#             'designation':designation,
#             'department' :department,
#             'employee': employee,

#     }

#     return render(request , 'employeeducation_update.html' , context)


def employeentitement_update(request,employeentitement_id):
    HttpResponse("WelCome to the home page")
    employeentitement = get_object_or_404(Employeentitlement, pk=employeentitement_id)
    designation = Designation.objects.all()
    department = Department.objects.all()
    employee = Employe.objects.all()


    if request.method == "POST":
        # employeentitement.entitlement_id = request.POST['entitlement_id']
        employe_id = request.POST['employe']
        employeentitement.basic_pay = request.POST['basic_pay']
        employeentitement.conveyance_all = request.POST['conveyance_all']
        employeentitement.medical = request.POST['medical']
        employeentitement.utilities = request.POST['utilities']
        employeentitement.cola = request.POST['cola']
        employeentitement.gross_pay = request.POST['gross_pay']
        employeentitement.effective_date = request.POST['effective_date']
        designation_id = request.POST['designation']
        employeentitement.designation = get_object_or_404(Designation, pk=designation_id)
        employeentitement.employee = get_object_or_404(Employe, pk=employe_id)
        employeentitement.save()
        return redirect('employedepartment_update' , employedepartment_id=employeentitement.employe.pk)
        
    context = {
            'employeentitement': employeentitement,
            'designation':designation,
            'department' :department,
            'employee': employee,

    }

    return render(request , 'employeentitement_update.html' , context)


def employedepartment_update(request,employedepartment_id):
    HttpResponse("WelCome to the home page")
    employedepartment = get_object_or_404(Employedepartment, pk=employedepartment_id)
    designation = Designation.objects.all()
    department = Department.objects.all()
    employee = Employe.objects.all()

    if request.method == "POST":
        employe_id = request.POST['employe']
        department_id = request.POST['department']
        employedepartment.effectiv_date = request.POST['effectiv_date']
        # employe.designation = get_object_or_404(Designation, pk=designation_id)
        employedepartment.department = get_object_or_404(Department, pk=department_id)
        employedepartment.employee = get_object_or_404(Employe, pk=employe_id)
        
        employedepartment.save()
        return redirect('employeattendance_update' , employeattendance_id=employedepartment.employe.pk)
        
    context = {
            'employedepartment': employedepartment,
            'designation':designation,
            'department' :department,
            'employee': employee,

    }

    return render(request , 'employedepartment_update.html' , context)


def employeattendance_update(request,employeattendance_id):
    HttpResponse("WelCome to the home page")
    employeattendance = get_object_or_404(Employeattendance, id=employeattendance_id)
    designation = Designation.objects.all()
    department = Department.objects.all()
    employee = Employe.objects.all()

    if request.method == "POST":
        employe_id = request.POST.get('employe')
        employeattendance.month = request.POST.get('month') 
        employeattendance.days_worked = request.POST.get('days_worked')
        employeattendance.employee = get_object_or_404(Employe, pk=employe_id)
        



        employeattendance.save()
        return redirect('employe_list')
        
    context = {
            'employeattendance': employeattendance,
            'designation':designation,
            'department' :department,
            'employee': employee,

    }

    return render(request , 'employeattendance_update.html' , context)







