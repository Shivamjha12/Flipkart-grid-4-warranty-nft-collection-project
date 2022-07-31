from asyncio.windows_events import NULL
from pydoc import plain
from django.forms.forms import Form
from django.core.paginator import *
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.db.models import Q
from django.conf import settings
from .urls import *
from django.urls import reverse
from .nft_collection import nft_collection
from thirdweb.types.nft import NFTMetadataInput
# Create your views here.

def profile(request):
    p = orders.objects.filter(user=request.user)
    l=len(p)
    print(l,",,,,,,,,,,,,,,,,,,,,,,,,,<<<<<<<<<<<<<<<<<<<<")
    if(l==0):
        ord = orders.objects.filter(user=request.user)
    else:
        ord = orders.objects.filter(user=request.user)[l-1]
    print(ord)
    return render(request, 'user_page.html',{'ord':ord})
def nftinfo(request):
    x=  nfts.objects.filter(user=request.user)
    # nt = x.values_list('token_id', flat=True)    
    return render(request, "nfts.html",{'x':x})

def nftdetails(request,tokenid):
    nft = nft_collection.get(tokenid)
    plain_data = str(nft)[38:-54]
    nfte = plain_data.split(',') 
    print(nfte)
    context = {
        
    }
    for i in range(len(nfte)):
        print(nfte[i]," <-----")
        context[i]=nfte[i]
    print(context)
    return render(request, "nfts_details.html",{'context':context})

def home(request):
    products_list = products.objects.all()
    context ={
        'products_list': products_list
    }
    return render(request,"home.html",context)

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request,'congratulations ' + user + ' Your account is created you can login now!')
            return redirect('login')
    context = {'form': form, 'signupsucess': 'Congratulation you are logged in with successful signup process'}
    return render (request, 'registration.html', context )

def login(request):
    
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           auth_login(request, user)
           return redirect('home')
       else:
           messages.info(request, 'Username or password are not correct')
    
    context = {}
    return render (request, 'login.html', context)

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('home')
def order(request,username):
    u = User.objects.get(username=username)
    x = User.objects.values('id').filter(username=username).first()
    p = orders.objects.filter(user=x['id'])
    # print("xxxxxxxxxxxxxxxxx", p)
    return render(request, 'orders_page.html',{'p':p})

def product_page(request,product_id):
    product = products.objects.get(product_id=product_id)
    # print("xxxxxxxxxxxxxxxxx", product.title)
    if request.method=="POST":
        product_buy=orders.objects.create(user=request.user, product_buyed=product)
        product_buy.save()
        date = str(product_buy.ordered_date)
        datee = date[0:10]
        p_id = product_buy.order_id
        name_nft = str(request.user.first_name) + " " + str(request.user.last_name)
        description_nft = " The Prdouct is "+ str(product.title) + " and order id is " + str(p_id) + " with " + str(product.warranty_in_months) + " months warranty" 
        image_nft = product.img
        prop = "Warranty of " + str(product.warranty_in_months) + " Months" + " Buyed on " + datee
        metadata = NFTMetadataInput.from_json({
            'name': name_nft,
            'description': description_nft,
            'image': image_nft,
            'properties':prop
        })
        tx = nft_collection.mint_to("0xF1226E9751773806993fb597498a04714e717dFD", metadata)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        nfts.objects.create(user=request.user,product_buy=product,token_id=token_id,nft=nft)
        print(nft, " <----xx^^^^^^^^^^^^^^^^^^^^^^^^^xxxxnnnnnnnnnnn^^^^^^^^^^^^^^^^^^^^^^^^^^xxxxxxxxxxxxxxxxx-----> ")
        return redirect(reverse('order', kwargs={'username': request.user.username}))
    return render(request, 'product_page.html',{'product':product})