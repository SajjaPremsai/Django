from django.shortcuts import redirect, render
from django.http import HttpResponse

def login(request):
    return render(request,"Student/Login.html")

def dashboard(request):
    return render(request,"Student/base.html")

def login_request(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        if username == "Prem@8938" and password == "12345":
            return redirect("dashboard/")
        else:
            return render(request,"Student/Login.html")
    else:
        return HttpResponse("Invalid Method mapping for url")
