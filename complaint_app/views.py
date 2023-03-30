from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django_tables2 import SingleTableView

from complaint_app.forms import UserForm, UserProfileForm, ComplaintForm, DocumentFormset
from complaint_app.models import Complaint
from complaint_app.table import ComplaintTable


# Create your views here.
class Register(CreateView):
    model = User
    form_class = UserForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data()
        user_profile_form = UserProfileForm(prefix='user_profile_form')
        if self.request.POST:
            user_profile_form = UserProfileForm(self.request.POST, prefix='user_profile_form')
        context['user_profile_form'] = user_profile_form
        return context

    @transaction.atomic
    def form_valid(self, form):
        context = self.get_context_data()
        self.object = form.save()
        user_profile_form = context['user_profile_form']
        if user_profile_form.is_valid():
            user_profile_form.instance.user = self.object
            user_profile_form.save()
        return super(Register, self).form_valid(form)

    def form_invalid(self, form):
        return super(Register, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('complaint_app:login')

class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('complaint_app:home')

    def form_invalid(self, form):
        return reverse_lazy('complaint_app:login')

class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('complaint_app:login')

class Home(TemplateView):
    template_name = "home.html"

class CreateComplaint(CreateView):
    template_name = 'create_complaint.html'
    model = Complaint
    form_class = ComplaintForm

    def get_context_data(self, **kwargs):
        context = super(CreateComplaint, self).get_context_data()
        document_formset = DocumentFormset(prefix='document_formset')
        if self.request.POST:
            document_formset = DocumentFormset(self.request.POST, self.request.FILES, prefix='document_formset')
        context['document_formset'] = document_formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        document_formset = context['document_formset']
        form.instance.created_by = self.request.user
        self.object = form.save()
        if document_formset.is_valid():
            for doc in document_formset:
                doc.instance.complaint = self.object
                doc.save()
        return super(CreateComplaint, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('complaint_app:complaint_list')

class ComplaintList(SingleTableView):
    template_name = 'complaint_list.html'
    model = Complaint
    table_class = ComplaintTable


