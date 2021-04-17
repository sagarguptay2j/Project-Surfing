
from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.shortcuts import render,get_object_or_404,redirect_field_name
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreateForm,UserProfileForm
from . import forms
from .models import Profile
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class NewUserCreation(CreateView):
    login_url = '/login/'
    form_class = forms.UserProfileForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/new_user.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class UserProfileUpdation(LoginRequiredMixin,UpdateView):

    login_url = '/login/'
    success_url = reverse_lazy('home')
    model = Profile
    form_class = UserProfileForm
    template_name = 'accounts/new_user.html'
'''
def registration(request):
    registered = False

    if request.method == 'POST':
        userForm = UserCreateForm(request.POST)
        profileForm = UserProfileForm(request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user

            #if 'profilePic' in request.FILES:
            #    profile.profilePic = request.FILES['profilePic']

            profile.save()

            registered = True
            return redirect('login')

        else:
            print(userForm.errors,profileForm.errors)
    else:
        userForm = UserCreateForm
        profileForm = UserProfileForm

    return render(request,'accounts/signup.html',{'userForm':userForm,'profileForm':profileForm,'registered':registered})



@login_required
def profile(request):
    if request.method == 'POST':
        p_form = forms.UserProfileForm(request.POST,
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        p_form = forms.UserProfileForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'accounts/new_user.html', context)
'''
