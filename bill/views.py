from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.contrib import messages
from datetime import date
import plotly.express as px
import plotly
import json
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
        'form': form,
        
     

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
    prod1 = productDetail.objects.filter(customer=customer)
    if request.method=="POST":
        product_name=request.POST['prod_name']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        products =productDetail(customer=customer,prod_name=product_name,
                quantity=quantity,rate=rate,amount = float(quantity) * float(rate))   
        products.save()
        return redirect('customform', id=id)
    context={
        'p1':prod1,
        'customer':customer
    }
    return render(request,'customform.html',context)




def delete_product(request, id):
    prod=productDetail.objects.get(id=id)
    customer = prod.customer.id
    prod.delete()
    return redirect('customform',id=customer)

def update_product(request,id):
    prod1 = productDetail.objects.get(id=id)
    if request.method=='POST':
        prod1 = productDetail.objects.get(id=id)
        customer = prod1.customer.id
        prod1.prod_name=request.POST['prod_name']
        prod1.quantity=request.POST['quantity']
        prod1.rate=request.POST['rate']
        prod1.amount=float(prod1.quantity) *  float(prod1.rate)
        prod1.save()
        return redirect('customform',id=customer)
    return render(request,'update_product.html',{'prod1':prod1})

def delete_customer(request,id):
    customer=Detail.objects.get(id=id)
    customer.delete()
    messages.warning(request,'Deleted Successfully')
    return redirect('/')

def update_customer(request,id):
    customer=Detail.objects.get(id=id)
    form=customerDetailForms(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        messages.success(request,'Update Successfully')
        return redirect('/')
    context={
        'form':form
    }
    return render(request,'update_customer.html',context)


def dashboard(request):
    cust1=Detail.objects.count()
    cust2=productDetail.objects.filter(prod_name='Bike').count()
    cust3=productDetail.objects.filter(prod_name='Car').count()
    todays = date.today()
    cust5=Detail.objects.filter(joined_date=todays)
    cust4=cust5.count()
    detail1 = Detail.objects.all().order_by('-id').values()
    detail2=Detail.objects.all().order_by('-id')[:3]
    data = productDetail.objects.values('prod_name', 'quantity').order_by('quantity')
    fig = px.bar(data, x='prod_name', y='quantity',color="prod_name",title="Bar-Graph")
   
    datapie = productDetail.objects.values('prod_name', 'quantity').order_by('rate')
    fig2 = px.pie(datapie, names='prod_name', values='quantity',color="prod_name",title="Bar-Graph")
   
    context = {
        'd1': detail1,
        'd2': detail2,
        'cust1':cust1,
        'cust2':cust2,
        'cust3':cust3,
        'cust4':cust4,
        'fig': json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder),
        'fig2': json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
     

    }
    return render(request,'dashboard.html',context)


def customer_list(request):
    detail1 = Detail.objects.all().order_by('-id').values()
    detail2=Detail.objects.all().order_by('-id')[:3]
    context = {
          'd1': detail1,
          
    }
    return render(request,'customer_list.html',context)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def bar_graph_view(request):
    data = Detail.objects.values('name', 'joined_date').order_by('joined_date')
    fig = px.bar(data, x='name', y='joined_date',color="joined_date",title="Bar-Graph")
   
    return render(request, 'graph.html', {'fig': json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)})
