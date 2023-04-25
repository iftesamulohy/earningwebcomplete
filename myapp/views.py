from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from myapp.models import User,Deposit,Withdraw,Packages,PackageOrder,Utilities,Work,CompleteTask
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import date, datetime, timedelta
from django.views.generic import ListView, DetailView
from django.db.models import Q,Sum
def store_file(file,folder):
    with open(f"images/{folder}/{file}","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

import logging
logger = logging.getLogger(__name__)
logger = logging.getLogger('django')
logger_myapp = logging.getLogger('myapp')
logger_info = logging.getLogger('info')
# Create your views here.
class LoginPage(TemplateView):
    template_name = "myapp/earningapp/auth-login.html"
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')
class Signup(TemplateView):
    template_name= "myapp/earningapp/auth-register.html"
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        ref = request.POST.get('reffer')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            phone_no = phone,
            refferedby = ref,
            balance = Utilities.objects.all()[0].joining_bonus

            ) 
        user.set_password(password)
        user.save()
        print(username,first_name,last_name,email,phone,ref)
        print(password)
        # Authenticate the user
        user = auth.authenticate(username=username, password=password)

        # Log the user in
        if user is not None:
            auth.login(request,user)
            package = Utilities.objects.all()[0].free_package
            if package:
                PackageOrder.objects.create(
                    user=request.user,
                    package = package,
                    purchase_date = date.today(),
                    expire_date= date.today() + timedelta(days=int(package.plan_validity)),
                    status='Activate'
                    
                    )
            return redirect('index')
        else:
            return redirect('login')
    
class Dashboard(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = "myapp/earningapp/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["util"]=Utilities.objects.all()[0]
        context['deposit']=Deposit.objects.filter(Q(user__username=self.request.user) & Q(status="Complete")).aggregate(Sum('amount'))['amount__sum']
        today= date.today()
        print("date",today)
        context['t_income'] = CompleteTask.objects.filter(Q(user__username=self.request.user) & Q(status="Approved")& Q(date=today)).aggregate(Sum('work__reaward_amount'))['work__reaward_amount__sum']
        context['packages'] = PackageOrder.objects.filter(Q(user__username=self.request.user) & Q(status="Activate"))
        return context

class DepositView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name= "myapp/earningapp/payment.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['util']=Utilities.objects.all()[0]
        return context
    def post(self, request, *args, **kwargs):
        number = request.POST.get('number')
        form_number = request.POST.get('form_number')
        trxid = request.POST.get('trxid')
        amount = request.POST.get('amount')
        Deposit.objects.create(
            user=request.user,
            number= number,
            trx_id = trxid,
            payment_method = form_number,
            date = timezone.now(),
            amount = amount,
            status = 'Pending'
            )
        print(number)
        print(form_number)
        return redirect('index')

class DepositHistory(LoginRequiredMixin,TemplateView):
    template_name=template_name= "myapp/earningapp/history.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dh']=Deposit.objects.filter(user__username=self.request.user)
        return context
    

class WithdrawView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name= "myapp/earningapp/paymentw.html"
    def post(self, request, *args, **kwargs):
        number = request.POST.get('number')
        form_number = request.POST.get('form_number')
    
        amount = request.POST.get('amount')
        Withdraw.objects.create(
            user=request.user,
            number= number,
            payment_method = form_number,
            date = timezone.now(),
            amount = amount,
            status = 'Pending'
            )
        print(number)
        print(form_number)
        return redirect('index')
class WithdrawHistory(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/historyw.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dh']=Withdraw.objects.filter(user__username="admin")
        return context
class TeamView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/team.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['refpack'] = PackageOrder.objects.filter(refferedby =self.request.user )
        return context
class ProfileView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/profile.html"
class PackageView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/packages.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        packs=Packages.objects.all()
        purpack= PackageOrder.objects.filter(user__username=self.request.user)
        for puck in purpack:
            #print("date",date(str(puck.expire_date)))
            print(date(2023,4,16))
        for pack in packs:
            
            pack.status= "none"
            for pur in purpack:
                 print(pur.status)
                 if str(pack)==str(pur) and pur.status=="Activate":
                     pack.status = "active"
                     
   
        context['packs'] = packs
        
        return context
    def post(self, request, *args, **kwargs):
        
        package =request.POST.get('package')
        validity =request.POST.get('validity')
        print(validity)
        package = Packages.objects.get(id=int(package))
        if package.amount>request.user.balance:
            print("insufficiant balance")
            context = self.get_context_data(**kwargs)
            context['error'] = "Insuficiant Balance. Deposit to purchase"

            return self.render_to_response(context)

        else:
            
            PackageOrder.objects.create(
                user=request.user,
                package = package,
                purchase_date = date.today(),
                expire_date= date.today() + timedelta(days=int(validity)),
                refferedby = request.user.refferedby,
                status='Activate'
                
                )
        
        return redirect('package')
    
class WorkView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/worklist.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pack=[]
        packages=PackageOrder.objects.filter(Q(user__username=self.request.user) & Q(status="Activate") )
        for package in packages:
            pack.append(str(package))
        complete_works=CompleteTask.objects.filter(Q(user__username=self.request.user) & ~Q(status="Canceled") )
        print(complete_works)
        work = []
        for com in complete_works:
            print("work",com.pk)
            work.append(str(com.pk))
        current_date = timezone.now().date()
        context['free_tasks'] = Work.objects.filter(Q(package__name__in = pack) & ~Q(pk__in = work) & Q(end_date__gt=current_date))
        return context
class WorkDetails(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/single-work.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id= self.kwargs.get('pk')
        context['details'] = Work.objects.get(pk=id)
        
        return context
    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('imagefile')
        store_file(image_file,"screenshots")
        id=self.kwargs.get('pk')
        CompleteTask.objects.create(
            user = request.user,
            work = Work.objects.get(pk=id),
            image = image_file

        )
        return redirect('works')
class ProfileUpdate(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name=template_name= "myapp/earningapp/profile-update.html"
    def post(self, request, *args, **kwargs):
        fname =request.POST.get('fname')
        lname =request.POST.get('lname')
        phone =request.POST.get('phnumber')
        email =request.POST.get('email')
        profile_picture = request.FILES.get('dp')
        #store_file(profile_picture,"profile")
        data = User.objects.get(username = request.user)
        print(fname,lname,phone,email)
        if fname:
            data.first_name = fname
            data.save()
        if lname:
            data.last_name = lname
            data.save()
        if phone:
            data.phone_no = phone
            data.save()
        if email:
            data.email = email
            data.save()
        if profile_picture:
            store_file(profile_picture,"images/profile")
            data.profile_picture = profile_picture
            data.save()
        return redirect('index')

    

def logout_view(request):
    logout(request)
    return redirect('login')
