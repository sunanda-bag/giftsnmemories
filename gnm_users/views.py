from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import *
from .forms import *
from order.models import Order


# Create your views here.


class SigninView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'gnm_users/signin.html')

    def post(self, *args, **kwargs):
        username = self.request.POST.get('singin-email')
        password = self.request.POST.get('signin-pass')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(self.request, user)

                return HttpResponseRedirect(reverse('home'))
                # return HttpResponseRedirect(reverse('gnm_users:cust-account'))
            else:
                messages.error(self.request, 'Your account has been deactivated')
                return HttpResponseRedirect(reverse('gnm_users:signin'))
        else:
            messages.error(self.request, 'Please use correct email and password combination')
            return HttpResponseRedirect(reverse('gnm_users:signin'))



class SignupView(generic.View):
    def get(self, *args, **kwargs):
        context = {
            'user_creation_form': CreateUserForm(),
            'appuserform': AppUserForm()
        }
        return render(self.request, 'gnm_users/signup.html', context)

    def post(self, *args, **kwargs):
        userForm = CreateUserForm(data=self.request.POST)
        appUserForm = AppUserForm(data=self.request.POST)
        
        if userForm.is_valid() and appUserForm.is_valid():
            user = userForm.save(commit=False)
            # checking if the email already exists
            email_check = User.objects.filter(email=user.email)
            if email_check.count():
                messages.error(self.request, 'This email already exists. signin using the same email or choose another email.')
                return render(self.request, 'gnm_users/signup.html', {'user_creation_form': userForm,
                                                                 'appuserform':AppUserForm})
            else:
                user.username = user.email
                name = user.first_name
                user.first_name = name.split(' ')[0]
                user.last_name = name.split(' ')[-1]
                user.save()

                appuser = appUserForm.save(commit=False)
                appuser.user = user
                appuser.save()

                messages.success(self.request, 'Your profile was created. Login to enter into store.')
                
                return HttpResponseRedirect(reverse('gnm_users:signin'))
        else:
            messages.error(self.request, 'Something went wrong. Try again')
            return render(self.request, 'gnm_users/signup.html', {'user_creation_form': userForm,
                                                                 'appuserform':AppUserForm})
        



@login_required()
def signoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



class AccountView(LoginRequiredMixin,generic.View):
    login_url = '/user/signin'
    redirect_field_name = '/user/cust-account/'
    
    def get(self, *args, **kwargs):
        context = {
        'orders':Order.objects.filter(user=self.request.user, ordered=True).order_by('-id')
        }
        return render(self.request, 'gnm_users/cust-account.html', context)



class CustomerOrdersListView(LoginRequiredMixin,generic.ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'gnm_users/cust-order-list.html'
    paginate_by = 12

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, ordered=True).order_by('-id')
    

class CustomerOrdersDetailView(LoginRequiredMixin,generic.DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'gnm_users/cust-order-detail.html'
    
class CustomerProfileUpdateView(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    model = GnmUser
    fields			= ['gender', 'mobile', 'address', 'city', 'pincode']
    template_name	= 'gnm_users/cust-profile-update.html'
    success_url		= reverse_lazy('gnm_users:cust-account')
    success_message = "Profile Updated successfully"