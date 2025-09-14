from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
        else: 
            print("Form with error",form )
            return render(request,'auth/register.html',{'form':form})

    else:
        initial_form = {
            'username':'',
            'password1':'',
            'password2':''
        }
        
        form = UserCreationForm(initial=initial_form)
    return render(request,'auth/register.html',{'form':form})
    
    

def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("dashboard")  # Redirect to home page after login
      
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    else:
        inital_form = {
            'username':'',
            'password':''
        }
        form =  AuthenticationForm(inital_form)
        print("form",form)
    return render(request,'auth/login.html',{'form':form})


def home(request):
    return render(request,'layouts/app.html')



def logout_view(request):
    logout(request)
    return redirect('login')
# Create your views here.


@api_view(['POST'])
def register_api(request):
    pass
    username = request.data.get('username')
    password = request.data.get('password')
    email    = request.data.get('email')

    if not username or not password:
        return Response({
            "error": "Username and password are required"            
        }) 
    
    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    
    user = User.objects.create(
        username=username,
        email=email,
        password=make_password(password)
    )
    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        print(request.data)
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()  # requires Blacklist app
        return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        print(e)
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)







@api_view(['POST'])
def product_save(request):
    pass


@api_view(['POST'])
def product_list(request):
    pass

@api_view(['POST'])
def product_remove(request):
    pass




