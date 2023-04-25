from django import forms
from django.conf import settings
from django.contrib import admin
from .models import Deposit, Work, User, Utilities, Withdraw,Packages,PackageOrder,CompleteTask

# Register your models here.
from solo.admin import SingletonModelAdmin
from myapp.models import Aboutus, PrivacyPolicy, Terms
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.admin.models import LogEntry



class MyModelAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        models = [Aboutus,PrivacyPolicy, Terms,Utilities]
        fields = '__all__'
class MyModelAdminFormt(forms.ModelForm):
    n_text = forms.CharField(widget=CKEditorWidget())
    bkash_guide = forms.CharField(widget=CKEditorWidget())
    nagad_guide = forms.CharField(widget=CKEditorWidget())

    class Meta:
        models = [Utilities]
        fields = '__all__'
              
class AboutusAdmin(SingletonModelAdmin):
    form = MyModelAdminForm
class PrivacyAdmin(SingletonModelAdmin):
    form = MyModelAdminForm
class TermsAdmin(SingletonModelAdmin):
    form = MyModelAdminForm
class UtilitiesAdmin(SingletonModelAdmin):
    form = MyModelAdminFormt
class DepositAdmin(admin.ModelAdmin):
    list_display = ['user','number','payment_method','status']
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['user','number','payment_method','status']
admin.site.register(Deposit,DepositAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Utilities, UtilitiesAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(Withdraw,WithdrawAdmin)
admin.site.register(Packages)
admin.site.register(PackageOrder)
admin.site.register(User)
admin.site.register(Work)
admin.site.register(CompleteTask)