from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from complaint_app.models import UserProfile, Complaint, ComplaintDocument


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'phone_number',
            'address1',
            'address2',
            'city',
            'profile_photo',
            'user_type',
        )


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = (
            'title',
            'description',
        )


class DocumentForm(forms.ModelForm):
    class Meta:
        model = ComplaintDocument
        fields = (
            'files',
        )


DocumentFormset = inlineformset_factory(Complaint, ComplaintDocument, DocumentForm, extra=1, can_delete=False)
