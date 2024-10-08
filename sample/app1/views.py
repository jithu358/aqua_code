from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

from.models import users
from.models import drivers
from.models import collab
from.models import shop
from.models import *
import razorpay
def about1(request):
    return render(request,"about.html")

def index1(request):
    return render(request,"index.html")

def register1(request):
    if request.method=="POST":
        x=request.POST['n1']
        y=request.POST['n2']
        z=int(request.POST['n3'])
        t=request.POST['n4']
        s= request.POST['n5']
        r= request.POST['n6']
        j=request.POST['n7']
        l=1
        p1 = users.objects.filter(username=s)
        p2 = users.objects.filter(email=y)
        if j==t:
            if list(p1) == []:
                if list(p2) == []:
                    d1 = users.objects.create(username=s, email=y, phone=z, password=t, name=s, address=r)
                    d1.save()
                    d2 = collab.objects.create(usernames=s, status=l, password=t)
                    d2.save()
                    return render(request, "login.html")
                else:
                    url = 'pro3'
                    msg = '''<script>alert('email already exist')
                                                        window.location='%s'</script>''' % (url)
                    return HttpResponse(msg)
                    return redirect(register1)

            else:
                url = 'pro3'
                msg = '''<script>alert('username already exist')
                                    window.location='%s'</script>''' % (url)
                return HttpResponse(msg)
                return redirect(register1)

        else:

            url = 'pro3'
            msg = '''<script>alert('the confirmation password do not match')
                                                window.location='%s'</script>''' % (url)
            return HttpResponse(msg)
            return redirect(register1)
    else:

        return render(request,"register.html")


def option1(request):
    return render(request,"option(register).html")

def login1(request):
    return render(request,"login.html")

def option2(request):
    return render(request,"option.html")

def user_profile(request):
    return render(request,'shop.html')

def waitdriver(request):
    return render(request,'waitingconf.html')


def loginmain(request):
    if request.method=="POST":
        x=request.POST['text1']
        y=request.POST['password']

        try:
            d = collab.objects.get(usernames=x)
            if d.password == y:
                if d.status==1:
                    request.session['u_id'] = x
                    return redirect(showp)
                elif d.status==2:
                    f = drivers.objects.get(username=x)
                    if f.action == 'confirm':
                        request.session['u1_id'] = x
                        return redirect(delivery1)
                    else:
                        return render(request, 'waitingconf.html')
                else:
                    request.session['u2_id'] = x
                    return redirect(admin1)

            else:
                url = 'pro7'
                msg = '''<script>alert('incorrect password')
                                                        window.location='%s'</script>''' % (url)
                return HttpResponse(msg)
                return redirect(loginmain)

        except Exception:
            url = 'pro7'
            msg = '''<script>alert('incorrect username')
                                                        window.location='%s'</script>''' % (url)
            return HttpResponse(msg)
            return redirect(loginmain)
    else:
        return render(request, 'login.html')



def shop1(request):
    return render(request,"shop.html")


def single1(request):
    return render(request,"single.html")

def regdrive(request):
    if request.method=="POST":
        x=request.POST['n1']
        y=request.POST['n2']
        z=int(request.POST['n3'])
        t=request.POST['n4']
        s= request.POST['n5']
        r= request.FILES['n6']
        j = request.POST['n7']
        l=2
        p1 = drivers.objects.filter(username=s)
        p2 = drivers.objects.filter(email=y)
        if j==t:
            if list(p1) == []:
                if list(p2) == []:
                        d1=drivers.objects.create(username=x,email=y,phone=z,password=t,name=s,images=r,action="pending")
                        d1.save()
                        m1=collab.objects.create(usernames=x,status=l,password=t)
                        m1.save()
                        return render(request, "login.html")
                else:
                    url = 'pro10'
                    msg = '''<script>alert('email already exist')
                                                        window.location='%s'</script>''' % (url)
                    return HttpResponse(msg)
                    return redirect(regdrive)

            else:
                url = 'pro10'
                msg = '''<script>alert('username already exist')
                        window.location='%s'</script>''' % (url)
                return HttpResponse(msg)
                return redirect(regdrive)
        else:
            url = 'pro10'
            msg = '''<script>alert('the confirmation password do not match')
                                    window.location='%s'</script>''' % (url)
            return HttpResponse(msg)
            return redirect(regdrive)
    else:

        return render(request,"register_drivers.html")

def admin1(request):
    return render(request,"admin.html")

def request1(request):
    if request.method=='GET':
         d=drivers.objects.filter(action='pending')
         return render(request,'request.html',{'r':d})
    else:
        return render(request,'admin.html')

#admin reject
def delete(request):
    if request.method=='POST':
        a = request.POST['b2']
        d = drivers.objects.filter(name=a)
        d.delete()
        return redirect(loginmain)
    else:
        return render(request,'request.html')

#admin confirm
def update(request):
    if request.method=='POST':
        a = request.POST['b1']
        d = drivers.objects.filter(name=a)
        d.update(action='confirm')
        return redirect(admin1)
    else:
        return render(request,'request.html')

def profile2(request):
    if 'aid' in request.session:
        a=request.session['aid']
        d = drivers.objects.filter(username=a)
        return render(request, 'admin.html')
    else:
        return render(request,'login.html')


def profile1(request):
    if 'u_id' in request.session:
        x = request.session['u_id']

        data1 = collab.objects.get(usernames=x)
        return render(request,"details.html",{'r':data1})
    else:
        return render(request,'index.html')
def contact1(request):
    return render(request,"contact.html")

def delivery1(request):
    return render(request,"delievery.html")

def show1(request):
    return render(request,"store_sample.html")

def userdetails(request):
    return render(request,"details.html")

def userprof(request):
    if request.method=='GET':
        a = request.session['u_id']
        d = users.objects.filter(username=a)
        return render(request, 'details.html', {'r': d})
    else:
        return render(request,'shop.html')

def changepass(request):
    if request.method=='POST':
        x=request.POST['n']
        y=request.POST['n1']
        z=request.POST['n2']
        d=collab.objects.filter(usernames=x)
        d.update(password=z)
        return render(request,'login.html')
    else:
        return render(request,'changepass.html')

def upuser(request):
    if request.method=='POST':
        x=request.POST['c1']
        d=users.objects.filter(username=x)
        return render(request,'updateuser.html',{'r':d})
    else:
        return render(request,'updateuser.html')

def upuser(request):
    if request.method=='POST':
        x=request.POST['c1']
        d=users.objects.filter(username=x)
        return render(request,'updateuser.html',{'r':d})
    else:
        return render(request,'updateuser.html')

def userupdate(request):
    if request.method=='POST':
        a = request.POST['w']
        b = request.POST['a1']
        c = request.POST['a2']
        g = int(request.POST['a3'])
        e = request.POST['a4']
        d = users.objects.filter(username=a)
        d.update(name=b,address=c,phone=g,email=e)
        return redirect(userprof)
    else:
        return render(request,'updateuser.html')

def deliupdate1(request):
    if request.method=='POST':
        a = request.POST['w']
        b = request.POST['a1']
        g = int(request.POST['a3'])
        e = request.POST['a4']
        d = drivers.objects.filter(username=a)
        d.update(name=b,phone=g,email=e)
        return redirect(deliverprof)
    else:
        return render(request,'updatedeli.html')

def addproduct(request):
    if request.method=='POST':
        x=request.POST['n1']
        z = request.POST['n2']
        a = request.POST['n5']
        y=request.FILES['n4']
        d1 = shop.objects.create(pname=x, product=y, price=z,quantity=a)
        d1.save()
        d2 = shop.objects.all()
        return render(request, "admin.html")

    else:
        return render(request, "addproducts.html")

def showp(request):
    d2 = shop.objects.all()
    return render(request, "shop1.html", {'r': d2})

def sampleshopp(request):
    d2 = shop.objects.all()
    return render(request, "sampleshop.html", {'r': d2})



def logout(request):
    if 'u_id' in request.session:
        request.session.flush()
        return render(request,'about.html')
    elif 'u1_id' in request.session:
        request.session.flush()
        return render(request,'about.html')
    elif 'u2_id' in request.session:
        request.session.flush()
        return render(request,'about.html')
    else:
        return render(request,'about.html')

def deliverprof(request):
    if request.method=='GET':
        a = request.session['u1_id']
        d = drivers.objects.filter(username=a)
        return render(request, 'delieverydetails.html', {'r': d})
    else:
        return render(request,'delievery.html')

def deliupdate(request):
    if request.method=='POST':
        x=request.POST['c1']
        d=drivers.objects.filter(username=x)
        return render(request,'updatedeli.html',{'r':d})
    else:
        return render(request,'updatedeli.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import cart

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cart, shop  # Adjust imports based on your project


def addcart(request):
    if 'u_id' in request.session:
        a = request.session['u_id']
        if request.method == 'POST':
            x = request.POST['n1']
            r = request.POST['n2']
            y = request.POST['n3']
            c = request.POST['n4']
            z = int(r) * int(c)

            # Get the shop item based on pname
            d4 = shop.objects.filter(pname=x).first()

            if d4 is None:
                # Item not found in shop, handle the error as needed
                url = 'carty'
                msg = '''<script>alert('Product not found')
                          window.location='%s'</script>''' % (url)
                return HttpResponse(msg)

            # Check if the quantity in shop is sufficient
            if d4.quantity >= int(c):
                d2 = list(cart.objects.filter(usernames=a))
                item_exists = any(cart_item.pname == x for cart_item in d2)
                if item_exists:
                    d3 = cart.objects.get(usernames=a, pname=x)
                    j = d3.quantity
                    q = int(j) + int(c)
                    d3.quantity = q
                    d3.price = int(q) * int(r)  # Updated to use r instead of z
                    d3.save()
                    messages.info(request, 'Cart updated...')
                else:
                    d1 = cart.objects.create(usernames=a, pname=x, product=y, price=z, quantity=c)
                    d1.save()
                    messages.info(request, 'Added to cart...')
            else:
                url = 'carty'
                msg = '''<script>alert('Insufficient stock')
                          window.location='%s'</script>''' % (url)
                return HttpResponse(msg)

            return redirect(showp)
        else:
            return redirect(showp)

    else:
        return render(request, "login.html")


def addcart1(request):
    if 'u_id' in request.session:
        a=request.session['u_id']
        d = cart.objects.filter(usernames=a)
        s=int(sum(int(cart.price) for cart in d))
        return render(request, 'delulu.html', {'r': d,'sum':s})
    else:
        return render(request, "login.html")

def removecart1(request):
    if 'u_id' in request.session:
        a=request.session['u_id']
        if request.method=='POST':
            x=request.POST['n1']
            q = request.POST['n2']
            d = cart.objects.filter(usernames=a,pname=x,quantity=q)
            d.delete()
            return redirect(addcart1)
        else:
            return render(request, "delulu.html")
    else:
        return render(request, "login.html")


#user-paying payment
def pay(request, id):
    if 'u_id' in request.session:
        a = request.session['u_id']
        d1 = users.objects.get(username=a)
        amount = (id*100)
        m=id
        request.session['amount']=id
        order_currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

        return render(request, "pay.html",{'r':amount,'l':m,'g':d1})
    else:
        return render(request, "login.html")
def success11(request):
    if 'u_id' in request.session:
        a = request.session['u_id']
        if request.method=='POST':
            x=request.POST['n1']
            y = request.POST['n2']
            d3 = shop.objects.all()
            data = cart.objects.all()
            d = cart.objects.filter(usernames=a)
            s = int(sum(int(cart.price) for cart in d))
            z = request.POST['n3']
            d1 = orders.objects.create(usernameu=a, name=x, address=y, uphone=z, status="Packing",totalamount=s,dusername="name")
            d1.save()
            d2 = payments.objects.create(usernameu=a, totalamount=s,dusername="Not Yet Assigned")
            d2.save()
            for i in d3:
                for j in data:
                    if i.pname==j.pname:
                        sum1=i.quantity-j.quantity
                        dat=shop.objects.filter(pname=j.pname).update(quantity=sum1)
            d.delete()

            return render(request, 'success1.html', {'r': s})
        else:
            return render(request, 'success1.html')

    else:
        return render(request, "login.html")

def ordersdisp(request):
    if 'u_id' in request.session:
        a=request.session['u_id']
        d = orders.objects.filter(usernameu=a)
        return render(request, 'myorders.html', {'r': d})

    else:
        return render(request, "login.html")

def deliveryshow(request):
    if 'u1_id' in request.session:
        a = request.session['u1_id']
        d = orders.objects.filter(status="Packing")
        return render(request, 'deliverytable.html', {'r': d})
    else:
        return render(request, "login.html")

def deliveryaccept(request):
    if 'u1_id' in request.session:
        a = request.session['u1_id']
        if request.method == 'POST':
            x = request.POST['b2']
            d = orders.objects.filter(status="Packing",usernameu=x)
            d.update(status="Out For Delivery",dusername=a)
            d1=payments.objects.filter(usernameu=x,dusername="Not Yet Assigned")
            d1.update(dusername=a)
            return render(request, 'deliverytable.html')

        else:
            return render(request, 'deliverytable.html')

    else:
        return render(request, "login.html")

def deliveryonway(request):
    if 'u1_id' in request.session:
        a = request.session['u1_id']
        d = orders.objects.filter(status="Out For Delivery",dusername=a)
        return render(request, 'deliveryonway.html', {'r': d})
    else:
        return render(request, "login.html")

def delivered1(request):
    if 'u1_id' in request.session:
        a = request.session['u1_id']
        if request.method == 'POST':
            x = request.POST['b2']
            d = orders.objects.filter(status="Out For Delivery",usernameu=x)
            d.update(status="Delivered")
            return redirect(deliveryonway)
        else:
            return render(request, 'deliverytable.html')
    else:
        return render(request, "login.html")

def paymentadmin(request):
    if 'u2_id' in request.session:
        d = payments.objects.all()
        return render(request, 'adminpayments.html', {'r': d})

    else:
        return render(request, "login.html")

def editproduct(request):
    if 'u2_id' in request.session:
        d = shop.objects.all()
        return render(request, 'edit_products.html', {'r': d})

    else:
        return render(request, "login.html")

def upproduct(request):
    if request.method=='POST':
        x=request.POST['b1']
        d=shop.objects.filter(pname=x)
        return render(request,'update_shop.html',{'r':d})
    else:
        return render(request,'update_shop.html')

def productsupdate(request):
    if request.method=='POST':
        b = request.POST['a1']
        c = int(request.POST['a2'])
        g = int(request.POST['a3'])
        d = shop.objects.filter(pname=b)
        d.update(pname=b,price=c,quantity=g)
        return redirect(editproduct)
    else:
        return render(request,'update_shop.html')

#user-send-complaint
def comp(request):
    if request.method == 'POST':
        v = request.POST['p1']
        w = request.POST['p2']
        x = request.POST['p3']
        y = request.POST['p4']
        z = request.POST['p5']
        data=complaint.objects.create(username=v,name=w,mobile=x,email=y,complaint=z)
        data.save()
        return render(request, 'complaint.html')
    else:
        a1 = request.session['u_id']
        return render(request, 'complaint.html',{'r':a1})



#admin-view-complaint
def advicomp(request):
        d = complaint.objects.all()
        return render(request, 'adviewcomp.html', {'r': d})











