from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Sum


# Create your views here.


def index(request):
    detail1 = Detail.objects.all().order_by('-id').values()
    if request.method == "POST":
        form = customerDetailForms(request.POST)
        if form.is_valid():
            form.save()
            print('Added Successfully')
            return redirect('/')
    else:
        form = customerDetailForms()
    context = {
        'd1': detail1,
        'form': form
    }
    return render(request, 'index.html', context)


def customer(request, id):
    cust1 = Detail.objects.get(id=id)
    prod1 = productDetail.objects.filter(customer=cust1)
    total_price = productDetail.objects.filter(customer=cust1).aggregate(total_price=Sum('amount'))
    if request.method == "POST":
        form = productDetaillForms(request.POST)
        if form.is_valid():
            form.save()
            form = productDetaillForms()
            print('Product Added Successfully')
            return redirect('customer', id=id)
        else:
            print('Product UnSuccessfully')
    else:
        form = productDetaillForms()
    

    context = {
        'p1': prod1,
        'form': form,
        'c2': cust1,
        'p2': total_price,

    }
    return render(request, 'product.html', context)


def prod_update(request):
    return render(request,'product.html')

def bills(request,id):
    cust1=Detail.objects.get(id=id)
    prod1=productDetail.objects.filter(customer=cust1)
    total_price = productDetail.objects.filter(customer=cust1).aggregate(total_price=Sum('amount'))
    context={
        'p1':prod1,
        'p2': total_price,
        'c2':cust1
    }
    return render(request,'bills.html',context)


def customform(request, id):
    customer=Detail.objects.get(id=id)

    if request.method=="POST":
        product_name=request.POST['prod_name']
       
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        products =productDetail(customer=customer,prod_name=product_name,
                quantity=quantity,rate=rate)   
        products.save()
    return render(request,'customform.html',{"customer":customer})

def delete_product(request, id):
    cust1 = Detail.objects.get(id=id)
    prod=productDetail.objects.get(id=id)
    prod.delete()
    return redirect('customer', id=cust1)