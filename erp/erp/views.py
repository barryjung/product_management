from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, InboundForm, OutboundForm
from .models import Product, Inbound, Outbound, Invetory

# Create your views here.
def home(request):
    return redirect('/product_list')


def product_list(request):
    if request.method == 'GET':
        all_products = Product.objects.all()
        return render(request, 'erp/product_list.html', {'products':all_products})


@login_required
def product_create(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'erp/product_create.html',{'form':form})
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
            return redirect('/')
        else:
            form = ProductForm()
            return render(request, 'erp/product_create.html',{'form':form})


@login_required
def inbound_create(request):
    if request.method == 'GET':
        form = InboundForm()
        return render(request, 'erp/inbound_create.html',{'form':form})
    else:
        inbound = InboundForm(request.POST)
        if inbound.is_valid():
            code = inbound.cleaned_data.get('code')
            quantity = inbound.cleaned_data.get('quantity')
            product = Product.objects.get(code = code)

            inbound.save()
            product.inbound_quantity += quantity
            product.stock_quantity += quantity
            product.save()
            return redirect('/')
        else:
            form = InboundForm()
            return render(request, 'erp/inbound_create.html',{'form':form})


@login_required
def outbound_create(request):
    if request.method == 'GET':
        form = OutboundForm()
        return render(request, 'erp/outbound_create.html',{'form':form})
    else:
        outbound = OutboundForm(request.POST)
        if outbound.is_valid():
            code = outbound.cleaned_data.get('code')
            quantity = outbound.cleaned_data.get('quantity')
            product = Product.objects.get(code = code)

            if product.stock_quantity >= quantity:
                outbound.save()
                product.outbound_quantity -= quantity
                product.stock_quantity -= quantity
                product.save()
                return redirect('/')
            else:
                form = OutboundForm()
                return render(request, 'erp/outbound_create.html',{'error':'재고가 부족합니다.','form':form})
        else:
            form = OutboundForm()
            return render(request, 'erp/outbound_create.html',{'form':form})


@login_required
def inventory(request):
    products = Product.objects.all()
    for product in products:

        inbounds = Inbound.objects.filter(code=product)
        inbound_q_sum = sum([x.quantity for x in inbounds])
        inbound_a_sum = sum([x.ammount for x in inbounds])

        outbounds = Outbound.objects.filter(code=product)
        outbound_q_sum = sum([x.quantity for x in outbounds])
        outbound_a_sum = sum([x.ammount for x in outbounds])

        if not Invetory.objects.filter(code=product).exists():
            inventory = Invetory(code=product)
            inventory.total_inbound_quantity = inbound_q_sum
            inventory.total_inbound_ammount = inbound_a_sum
            inventory.total_outbound_quantity = outbound_q_sum
            inventory.total_outbound_ammount = outbound_a_sum
            inventory.save()
        else:
            inventory = Invetory.objects.get(code=product)
            inventory.total_inbound_quantity = inbound_q_sum
            inventory.total_inbound_ammount = inbound_a_sum
            inventory.total_outbound_quantity = outbound_q_sum
            inventory.total_outbound_ammount = outbound_a_sum
            inventory.save()
    
    inventories = Invetory.objects.all()
    return render(request, 'erp/inventory.html', {'inventories':inventories})
