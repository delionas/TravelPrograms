from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from api.forms import UserLoginForm, ProblemForm, SolutionForm
from api.models import Problem


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if username == '123':
                return render(request, 'problem_create.html')
            if user:
                login(request, user)
                # return redirect('problem_list')
                return render(request, 'problem_list.html')
            else:
                redirect('problem_create')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def problem_list(request):
    user = request.user
    problems = Problem.objects.filter(assigned_user=user) #фильтурет проблемы, чтобы получить только те, которые связаны именно с определенным пользоватлем
    return render(request, 'problem_list.html', {'problems': problems,'user':user})


def problem_create(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'problem_create.html', {'form':form})




def problem_details(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    if request.method == "POST":
        form = SolutionForm(request.POST)
        if form.is_valid(): #для проверки валидации
            solution = form.cleaned_data['solution']
            problem.solution = solution
            problem.resolved_user = request.user
            problem.status = "completed"
            problem.save()
            redirect('problem_list')
    else:
        form = SolutionForm()
    return render(request, 'problem_details.html', {'problem': problem, 'form':form})

def home(request):
    return render(request, 'home.html')