from django import forms
from django.forms import ModelForm
from .models import Applicant, Cycle, TreatmentFacility, ProcessingCenter
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create form
class PcForm(ModelForm):
    class Meta:
        model = ProcessingCenter
        fields=('pcCode','pcName',)

class MtfForm(ModelForm):
    class Meta:
        model = TreatmentFacility
        fields=('mtfCode','mtfName',)


class CycleForm(ModelForm):
    class Meta:
        model = Cycle
        fields=('cycle',)
        labels = {
            'cycle':'',
            }
        widgets = {
            'cycle':forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Cycle Code'}),
            }


class RegistrationForm(ModelForm):
    class Meta:
        model = Applicant
        fields = ('purpose','cycle','pc','mtf','lastName', 'firstName', 'middleName', 'suffix', 'age', 'birthDate', 'sex', 'contactNumber', 'completeAddress', 'region', 'course', 'educAttainment', 'eligibility', 'schoolAddress', 'tesdaCert', 'ncipTribe', 'height', 'weight', 'religion', 'milTraining', 'skill',)
        labels = {
            'purpose':'Purpose',
            'cycle':'Cycle',
            'pc':'Processing Center',
            'mtf':'Treatment Facility',
            'lastName':'Last Name',
            'firstName':'First Name',
            'middleName':'Middle Name',
            'suffix':'Suffix',
            'age':'Age',
            'birthDate':'Birth Date',
            'sex':'Sex',
            'contactNumber':'Contact Number',
            'completeAddress':'Complete Address',
            'region':'Region',
            'course':'Course',
            'educAttainment':'Educational Attainment',
            'eligibility':'Eligibility',
            'schoolAddress':'School Address',
            'tesdaCert':'Tesda Cetificates',
            'ncipTribe':'NCIP Tribe',
            'height':'Height',
            'weight':'Weight',
            'religion':'Religion',
            'milTraining':'Military Training',
            'skill':'Skills',
            }
        widgets = {
            'purpose':forms.Select(attrs={'class':'form-control','type': 'select'}),
            'cycle':forms.Select(attrs={'class':'form-control','type': 'select'}),
            'pc':forms.Select(attrs={'class':'form-control','type': 'select'}),
            'mtf':forms.Select(attrs={'class':'form-control','type': 'select'}),
            'lastName':forms.TextInput(attrs={'class':'form-control'}),
            'firstName':forms.TextInput(attrs={'class':'form-control'}),
            'middleName':forms.TextInput(attrs={'class':'form-control'}),
            'suffix':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'birthDate':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'sex':forms.Select(attrs={'class':'form-control','type': 'select'}),
            'contactNumber':forms.TextInput(attrs={'class':'form-control'}),
            'completeAddress':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.TextInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'educAttainment':forms.TextInput(attrs={'class':'form-control'}),
            'eligibility':forms.TextInput(attrs={'class':'form-control'}),
            'schoolAddress':forms.TextInput(attrs={'class':'form-control'}),
            'tesdaCert':forms.TextInput(attrs={'class':'form-control'}),
            'ncipTribe':forms.TextInput(attrs={'class':'form-control'}),
            'height':forms.TextInput(attrs={'class':'form-control'}),
            'weight':forms.TextInput(attrs={'class':'form-control'}),
            'religion':forms.TextInput(attrs={'class':'form-control'}),
            'milTraining':forms.TextInput(attrs={'class':'form-control'}),
            'skill':forms.TextInput(attrs={'class':'form-control'}),
        }

#Signup Form
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'