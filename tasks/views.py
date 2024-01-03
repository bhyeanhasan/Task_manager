from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth, User
from django.contrib import messages
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task, TaskImages
from rest_framework.views import APIView
from .serializers import TaskSerializer


# Create your views here.
@login_required(login_url='login')
def home(request):
    tasks = Task.objects.filter(user=request.user)
    images = TaskImages.objects.all()
    return render(request, 'homepage.html', {'tasks': tasks, 'images': images})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User not found')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken!!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken!!')
            return redirect('register')
        if pass1 == pass2:
            User.objects.create_user(username=username, email=email, password=pass1)
            return redirect('login')

        messages.info(request, 'Can not create')

    return render(request, 'register.html')


@login_required(login_url='login')
def createTask(request):
    if request.method == "POST":
        files = request.FILES.getlist('images')
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        due_date = request.POST['due_date']

        task = Task.objects.create(user=request.user, title=title, description=description, priority=priority,
                                   due_date=due_date, creation_time=datetime.now())
        for f in files:
            TaskImages.objects.create(task=task, images=f)

        return redirect('home')

    return render(request, 'task_create.html')


def editTask(request, id):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        due_date = request.POST['due_date']
        task = Task.objects.get(id=id)
        task.title = title
        task.description = description
        task.priority = priority
        task.due_date = due_date
        task.save()
        return redirect('home')

    task = Task.objects.get(id=id)
    return render(request, 'task_edit.html', {'task': task})


def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')


class ManageTask(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        profile = Task.objects.all()
        serializer = TaskSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        data = request.data
        data['user'] = request.user.pk
        old_profile = Task.objects.get(user=request.user.pk)
        print(data)
        serializer = TaskSerializer(old_profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            task = Task.objects.get(id=id)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
