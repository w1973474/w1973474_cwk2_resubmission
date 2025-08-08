from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Vote
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from collections import Counter
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .forms import AddUserForm


# Create your views here.

def Login(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        messages.error(request, "Sorry, your username or password is incorrect.")
    return render(request, 'health_check/login.html', {'form': form})



def Signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'health_check/signup.html', {'form': form})


def Dashboard(request):
    print(f"[DEBUG] Authenticated: {request.user.is_authenticated}, Username: {request.user.username}")

    labels = ['red', 'Orange', 'Green']
    votes = Vote.objects.all()
    count_by_type = Counter(v.vote_type.upper() for v in votes)

    data = [
        count_by_type.get('RED', 0),
        count_by_type.get('ORANGE', 0),
        count_by_type.get('GREEN', 0)
    ]

    vote_data = {
        'labels': labels,
        'data1': data,
    }
    return render(request, 'health_check/dashboard.html', {'vote_data':vote_data})


def HealthCheckVoting(request):
    if request.method == 'POST':
        codebase_vote = request.POST.get('codebase_quality')
        balance_vote = request.POST.get('work-life_balance')

        if codebase_vote:
            Vote.objects.create(
                vote_type=codebase_vote.upper(),
                question='codebase-quality',
                user=request.user,
                created_at=timezone.now()
            )

        if balance_vote:
            Vote.objects.create(
                vote_type=balance_vote.upper(),
                question='work-life_balance',
                user=request.user,
                created_at=timezone.now()
            )

        return redirect('dashboard')
    
    return render(request, 'health_check/health_check_voting.html')
        


#def TeamSummary(request):
#    if request.method ==


#def DepartmentSummary(request):
#    if request.method ==


#def AddUser(request):
#    if request.method == 'POST':
#        name = request.POST.get("name")
#        role = request.POST.get("role")
#        addUser = authenticate

User = get_user_model()

def AdminUserManagement(request):
    users = User.objects.all()
    form = AddUserForm()

    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
        
    return render(request, "health_check/user_management.html", {
        'users': users,
        'form': form,
    })

def DeleteUser(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('user_management')


#def AdminDepartmentManagement(request):
#    if request.method ==