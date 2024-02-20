from django.shortcuts import render,redirect,HttpResponse


#from.models import Employee,LoginAuth
from.models import*
from django.db.models import Q
# Create your views here.

def home(Request):
        if(Request.method=="POST"):
         search=Request.POST.get("search")
         data = Employee.objects.filter(Q(name__icontains=search) | Q(email__icontains=search)| Q(phone__icontains=search)| Q(salary__icontains=search)  | Q(city__icontains=search)| Q(state__icontains=search))                                               
        else:
            data = Employee.objects.all()
        return render(Request, "data.html", {'rows': data})
    
    

    
#-----------------------------delete-----------------
def delete(Request,id):
    data=Employee.objects.get(id=id)
    if data:
        data.delete()
       # return redirect("/data/")
        data=Employee.objects.all()
        return render(Request,"data.html",{'rows': data})
    return render(Request,"data.html")

#-----------------------------update=-----------------
def update(Request,id):
    data=Employee.objects.get(id=id)
    if(Request.method=="POST"):
        data.name=Request.POST.get("name")
        data.email=Request.POST.get("email")
        data.phone=Request.POST.get("phone")
        data.salary=Request.POST.get("salary")
        data.city=Request.POST.get("city")
        data.state=Request.POST.get("state")
        data.save()
       # return redirect("/data")
        data=Employee.objects.all()
        return render(Request,"data.html",{'rows': data})
    return render(Request,"update.html",{"d":data})


#-----------------------------login-----------------
# def loginPage(request):
#     return render(request,"login.html")
def login(Request):
    if Request.method=="POST":
            username=Request.POST.get("username")
            password=Request.POST.get("password")
            # queryset=LoginAuth.objects.filter(username=username)|LoginAuth.objects.filter(password=password) #OR operator
            queryset=LoginAuth.objects.filter(username=username,password=password)  #AND operator ---correct
            if len(queryset) !=0:
               # data=Employee.objects.all()
                return redirect('/data/')
              #  return render(Request,"data.html",{'rows': data})
            else:
                return HttpResponse("invalid username and password")
    return render(Request,"login.html")

# def login(Request):
#     if Request.method=="POST":
#             username=Request.POST.get("username")
#             password=Request.POST.get("password")
#             # queryset=LoginAuth.objects.filter(username=username)|LoginAuth.objects.filter(password=password) #OR operator
#             queryset=LoginAuth.objects.filter(username=username,password=password)  #AND operator ---correct
#             if queryset.exists():
#                 return redirect('/data/')
#             else:
#                 return HttpResponse("invalid username and password")
#     return render(Request,"login.html")
         
         
         
       
        

def add(Request):
    if(Request.method=="POST"):
        emp=Employee()
        emp.name=Request.POST.get("name")
        emp.email=Request.POST.get("email")
        emp.phone=Request.POST.get("phone")
        emp.salary=Request.POST.get("salary")
        emp.city=Request.POST.get("city")
        emp.state=Request.POST.get("state")
        emp.save()
        emp=Employee.objects.all() # i have doubt, i think it's line will not come here
      #  return redirect("/data/")
        return render(Request,"data.html",{'rows': emp})
    return render(Request,"add.html")
  
def contact(request):
    return render(request,"contact.html")
