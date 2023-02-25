from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.models import *
from .models import *
# Create your views here.

def index(request):
    categorys = Category.objects.all()
    yeni_urun = Product.objects.all().order_by('-date_now')[:3]
    begenilen = Product.objects.all().order_by('?')[:3]
    prodacts = Product.objects.all()
    context = {
        'categorys':categorys,
        'prodacts':prodacts,
        'yeni_urun':yeni_urun,
        'begenilen':begenilen,
    }
    return render(request, 'index.html',context)

def detay(request,id):
    product = Product.objects.get(id=id)
    commnets = Comment.objects.filter(product = product)
    context = {
       'product':product,
       'commnets':commnets,
    }
    if request.method == 'POST':
        like = request.POST['like']
        title = request.POST['title']
        text = request.POST['text']
        if like != 'puan':
            comm = Comment(like=like,title= title,text = text, product=product)
            comm.save()
            return HttpResponseRedirect("/detay/"+id+"/")
        else:
            context.update({'hata':'Puanlamayı yapmadınız!!'})

    return render(request, "detay.html",context)

def urunler(request,categotyid = 'all'):
    if categotyid =='all':
        prodacts = Product.objects.all()
    else:
        prodacts = Product.objects.filter(category = categotyid)
    categorys = Category.objects.all()
    context = {
       'prodacts':prodacts,
       'categorys':categorys,
    }

    return render(request, 'urunler.html',context)

def girisYap(request):
    context= {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context.update({'hata':'Kullanıcı adı veya şifre hatalı!!'})
    return render(request, 'user/giris.html',context)


def kayitOl(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(email=email,
                                                    username=username,
                                                    password=password1,
                                                    first_name = name,
                                                    last_name = name)
                    user.save()
                    return redirect('girisYap')
                else:
                    context.update({'hata':'Bu email zaten kullanılıyor!!'})
            else:
                context.update({'hata':'Bu kullanıcı adı zaten kullanılıyor!!'}) 
        else:
            context.update({'hata':'Şifreler aynı değil!!'})


    return render(request, 'user/kayit.html',context)

def cikisYap(request):
    logout(request)
    return redirect('index')


