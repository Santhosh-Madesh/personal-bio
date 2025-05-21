from django.shortcuts import render

def profile(request):
    return render(request,"personal_bio/profile.html")
