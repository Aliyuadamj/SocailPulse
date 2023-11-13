from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from login.models import Login

from .forms import LoginForm


def logins(request):
    log_info = Login.objects.all()
    return render(request, "login/login.html", context={
        "login": login
    })


def login(request, pk):
    login = Login.objects.get(pk=pk)
    return render(request, "login/login.html", context={
            "login": login
        })


def create_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("logins")
        else:
            return render(request, "login/create_login.html", context={
                "login_form": form
            })
    else:
        return render(request, "login/create_login.html", context={
                "login_form": LoginForm(),
            })



def update_login(request, pk):
    login = Login.objects.get(pk=pk)
    form = LoginForm(instance=login)
    if request.method == "POST":
        form = LoginForm(request.POST, files=request.FILES, instance=login)
        form.save()
        return redirect("logins")
    else:
        return render(request, "login/update_login.html", context={
                "Login_Form": form,
                "pk": pk
            })

    
def login_delete(request, pk):
    login = Login.objects.get(pk=pk)
    login.delete()
    return redirect("logins")

