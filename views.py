from django.shortcuts import render, redirect,get_object_or_404
from .models import Product,Category,CartItem
import jdatetime
from django.utils import timezone

def product(request):
    product = Product.objects.all()
    return render(request, 'list.html', {'product': product})

def add_cat(request):
    if request.method=='POST':
        name=request.POST.get('name')
        cat=Category.objects.all()
        if name:
            Category.objects.create(name=name)
            return redirect('product')
    return render(request,'cat.html',{'cat':cat})
        

        

def creat(request):
    categories = Category.objects.all()  # گرفتن لیست دسته‌بندی‌ها

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('cat')

        if name and price and category:
                category = Category.objects.get(id=category)
                Product.objects.create(name=name, price=price, category=category)
                return redirect('cart_view') 
    return render(request, 'creat.html', {'categories': categories,'error':'همه فیلد هارو پر کن'})


def delete(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        product.delete() 
        return redirect('cart_view')
    

def search(request):
        query=request.GET.get('q')
        results=[]

        if query and query.strip():
            results=Product.objects.filter(name__icontains=query.strip())
        return render(request,'search.html',{'results':results,'query':query})


def add_pro(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item,created=CartItem.objects.get_or_create(user=request.user,product=product)
    if not created:
        cart_item.quantity +=1
        cart_item.save()
    return redirect('cart_view')

    

def cart_view(request):
    product=Product.objects.all()
    cart=CartItem.objects.all()
    category=Category.objects.all()
    
    items=CartItem.objects.filter(user=request.user)
    total=sum(item.total_price()for item in items)
    total_quantity=sum(item.quantity for item in items)
    return render(request,'list.html',{
        'items':items,
        'total':total,
        'total_quantity':total_quantity,
        'products':product,
        'cart_items':cart,
        'categories':category,
    })

def remove_cart(request,item_id):
    remove=get_object_or_404(CartItem,id=item_id,user=request.user)
    remove.delete()
    return redirect('cart_view')

def increase(request,item_id):
    inc=get_object_or_404(CartItem,id=item_id,user=request.user)
    inc.quantity +=1
    inc.save()
    return redirect('cart_view')
def decrease(request,item_id):
    dec=get_object_or_404(CartItem,id=item_id,user=request.user)
    if dec.quantity > 1:
        dec.quantity -=1
        dec.save()
    else:
        dec.delete()
    return redirect('cart_view')

def category(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    product=Product.objects.filter(category=category)
    return render(request,'category.html',{'category':category,'products':product})

def invoice(request):
    items = CartItem.objects.all()
    total = sum(item.total_price() for item in items)
    total_quantity = sum(item.quantity for item in items)

    # زمان دقیق با در نظر گرفتن منطقه زمانی
    now_gregorian = timezone.localtime(timezone.now())
    now_jalali = jdatetime.datetime.fromgregorian(datetime=now_gregorian)

    date = now_jalali.strftime('%Y/%m/%d')
    time = now_jalali.strftime('%H:%M:%S')

    return render(request, 'invoice.html', {
        'items': items,
        'total': total,
        'total_quantity': total_quantity,
        'date': date,
        'time': time,
    })





    

             





 
    
