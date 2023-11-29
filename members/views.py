from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForms,EditProfileForms
from  django.contrib.auth.views import PasswordChangeView
from theblog.models import profile



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
def password_success(request):
    return render("registration/password_success.html",{})
class UserRegisterView(generic.CreateView):
    form_class = SignUpForms
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForms
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
class ShowProfileView(generic.DetailView):
    model = profile
    template_name = 'registration/user_profile.html'
    def get_context_data(self, *args, **kwargs):  # the get the data to the html page
        user = profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        pageuser=get_object_or_404(profile,id=self.kwargs['pk'])
        context["pageuser"] = pageuser
        return context
class EditProfileView(generic.UpdateView):
    model = profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio','profile_image','website_url','facebook_url','instagram_url','twitter_url']
    success_url = reverse_lazy('home')
class CreateProfileView(generic.CreateView):
    model = profile
    template_name = 'registration/create_profile.html'
    fields = '__all__'
    success_url = reverse_lazy('home')




    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
