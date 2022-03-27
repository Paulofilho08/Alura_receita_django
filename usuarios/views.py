from multiprocessing.reduction import send_handle
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print("existe")
            return redirect('cadastro')
        if not email.strip():
            print("tire os espaços em branco")
            return redirect('cadastro')
        if password != password2:
            print("Opa senhas não correspodem")
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print("Já tem ")
            return redirect('cadastro')
        user = User.objects.create_user(username=nome,email=email,password=password)      
        user.save()
        print("cadastrato") 
        print(nome,email,password,password2)     
        return redirect('login')
    else:    
        return render(request, 'usuarios/cadastro.html')
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    return render(request,'usuarios/dashboard.html')