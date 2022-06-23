from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Management
# Create your views here

def new_hotel(request):
    if request.method == "POST":
        username= request.POST.get("username")
        email= request.POST.get("email")
        fname= request.POST.get("fname")
        lname= request.POST.get("lname")
        password1= request.POST.get("password1")
        password2= request.POST.get("password2")
        
        if password2 == password1:
            new_user = User.objects.create_user(username=username, password=password1, email=email, first_name=fname, last_name=lname)
            new_user.save()
            return redirect("new_hotel:login")
    return render(request, "new_hotel/register.html") #{"Room":"No 15"})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate (request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("new_hotel:login")
    return render(request, "new_hotel/login.html") #{"Room":"No 15"})

def logout_view(request):
    logout(request)
    return render(request, "new_hotel/logout.html") #{"Room":"No 15"})



def managementrecords(request):
    if request.method == "POST":
        room_number=request.POST.get("rnumber")
        amount = request.POST.get("amount")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        occupation = request.POST.get("occupation")
        nights = request.POST.get("nights")
        sdate = request.POST.get("sdate")
        edate = request.POST.get("edate")
        
        new_customer = Management(Room_Number=room_number, Amount_Paid=amount, Occupant_First_Name=fname, Occupant_Last_Name=lname, Occupant_Email=email, Occupant_Occupation=occupation,Number_Of_Nights=nights, Start_Date=sdate, End_Date=edate )
        new_customer.save()
        return redirect("new_hotel:managementrecords")
    return render (request, "new_hotel/managementrecords.html")