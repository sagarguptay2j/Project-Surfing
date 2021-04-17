from django.shortcuts import render,get_object_or_404
#from django.contrib.auth import redirect_field_name
from django.utils import timezone
from .models import Project,Comment
from .forms import ProjectForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_all'

    def project_list(self):
        return Project.objects.all()

class ProjetDetailView(DetailView):
    model = Project

    def comments_list(self):
        project = get_object_or_404(Project,pk=self.pk)
        return project.comments.all()

class CreateProjectView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'projects/single.html'
    form_class = ProjectForm
    model = Project

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

class CreateCommentView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'projects/single.html'
    form_class = CommentForm
    model = Comment


class ProjectDeleteView(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model = Project
    select_related = ('owner')
    success_url = reverse_lazy('projects:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

class UserProjectList(ListView):
    model = Project
    referenced_user = None
    template_name = 'projects/user_project_list.html'
    #def user_project(self):
    def get_queryset(self):
        try:
            self.referenced_user = self.kwargs.get('username')
            #self.post_user = User.objects.prefetch_related('posts').get(username__iexact = self.kwargs.get('username'))
        except :
            raise Http404
        else:
            return Project.objects.filter(owner__username__iexact = self.referenced_user)


    def user_project(self):
        return   Project.objects.filter(owner__username__iexact = self.referenced_user.username)


'''    def delete(self,*args,**kwargs):
        messages.success(self.request,'Project Deleted')
        return super().delete(*args,**kwargs)'''
