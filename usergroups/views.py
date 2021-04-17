from django.shortcuts import render
from django.urls import reverse
from  usergroups.models import Usergroup,GroupMember
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import UsergroupForm
# Create your views here.
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin



class UsergroupList(generic.ListView):
    model = Usergroup
    context_object_name = 'object_list'

class UsergroupDetail(generic.DetailView):
    model = Usergroup

    def check(self):
        #group = get_object_or_404(Usergroup,slug=self.kwargs.get('slug'))
        for oneuser in self.object.users.all():
            if oneuser.username == self.request.user.username:
                return True
        else:
            return False




class CreateUsergroup(LoginRequiredMixin,generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'usergroups/single.html'
    form_class = UsergroupForm
    model = Usergroup
'''
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.groupadmin = self.request.user
        self.object.save()
        return super().form_valid(form)

'''
class JoinUsergroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('usergroups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Usergroup,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except:
            messages.warning(self.request,'Already a user')
        else:
            messages.success(self.request,'Successfully joined')

        return super().get(request,*args,**kwargs)

class LeaveUsergroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('usergroups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug'))
        except:
            messages.warning(self.request,'You are not a member of this group')
        else:
            membership.delete()
            messages.success(self.request,'Successfully left the group')

        return super().get(request,*args,**kwargs)
