from django.shortcuts import render
from .models import Seller, Car, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CarForm, CommentForm
from django.contrib import messages


def home(request):
    cars = Car.objects.all()
    return render(request, "home.html", {"cars": cars})


def cars(request):
    cars = Car.objects.all()
    return render(request, "cars.html", {"cars": cars})


def sellers(requests):
    sellers = Seller.objects.all()
    return render(requests, "sellers.html", {"sellers": sellers})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Seller.objects.create(user=user)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("username")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return  redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.info(request, "Please log in to add a car.")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.seller = request.user.seller
            car.save()
            return redirect("cars")
    else:
        form = CarForm()
    return render(request, "create_car.html", {"form": form})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    comments = Comment.objects.filter(car=car)
    form = CommentForm()

    return render(request, "car_detail.html", {'car': car, 'comments': comments, 'form': form})


@login_required
def add_comment(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.car = car
            comment.save()
            return redirect("car_detail", pk=car.pk)
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {"form": form})






