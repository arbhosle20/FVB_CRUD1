from django.shortcuts import render,redirect
from .forms import  OrderModelForm
from .models import  Orders

def addorderView(request):
    form = OrderModelForm()
    if request.method =='POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_order')
    context = {'form': form}
    template_name = 'LaptopApp/addorder.html'
    return render(request,template_name,context)
def showordersView(request):
    orders = Orders.objects.all()
    context = {'orders':orders}
    template_name = 'LaptopApp/showorder.html'
    return render(request,template_name,context)

def deleteorderview(request,i):
    order = Orders.objects.get(id=i)
    if request.method == 'POST':
        order.delete()
        return redirect('show_order')
    context = {'order':order}
    template_name = 'Laptopapp/deleteorder.html'
    return render(request,template_name,context)

def updateorderview(request,i):
    order = Orders.objects.get(id=i)
    form = OrderModelForm(instance=order)
    if request.method == 'POST':
        form = OrderModelForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('show_order')
    context = {'form':form}
    template_name = 'LaptopApp/addorder.html'
    return render(request,template_name,context)