from django import forms
from .models import patient,token,doctor,bill


class patientaccountform(forms.Form):
    pass

class Token(forms.Form):
    #name=forms.ModelChoiceField(queryset=patient.objects.all())
    #doc=doctor.objects.all()[:]
    #identity=forms.IntegerField()
    Doctor=forms.ModelChoiceField(queryset=doctor.objects.all())
    Date=forms.DateField(label='')

class SearchForm(forms.Form):
    q=forms.CharField(label="Search:",widget=forms.TextInput(attrs={'class':'form-control',
    'max_length':'30','placeholder':'Search'}))

class SearchFormD(forms.Form):
    r=forms.CharField(label="Search Doctor",widget=forms.TextInput(attrs={'class':'form-control',
    'max_length':'30','placeholder':'Search'}))

class patientcreateform(forms.Form):
    patient_name=forms.CharField(label="",widget=forms.TextInput(attrs={
        'class':'form-control','maxlength':'50','placeholder':'patient_name'}))
    sex=(('male','male'),('female','female'),('others','others'))
    Sex=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=sex))
    Dob=forms.DateField(label="",widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Date of birth'}))
    Age=forms.IntegerField(label="",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'age'}))
    Contact=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'contact','class':'form-control'}))
    Address=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'address'}))
    #Contact=PhoneNumberField(label='',widgets=PhoneNumberField(attrs={'class':'form-control','placeholder':''}))
    Email=forms.EmailField(label="",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    blood_group=(('AB+','AB+'),('AB-','AB-'),('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O-','O-'),('O+','O+'))
    Blood_group=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=blood_group))
    Password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-control'}))

class billform(forms.ModelForm):
    class Meta:
        model=bill
        fields=('patient','id','room','report','fee','operation','Date','ndays')
        Date=forms.DateField(label='')
        ndays=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'number of days'}))
        patient=forms.ModelChoiceField(queryset=patient.objects.all())
        ward=((500,'general'),(1000,'icu'))
        room=forms.IntegerField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=ward))
        report=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'report charges'}))
        fee=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'doctor fee'}))
        operation=forms.IntegerField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'operation charges'}))
        #med=((30,'dolo650'),(12,'saridon'),(9,'crocin'))


class UserRegisterForm(forms.Form):
    Name=forms.CharField(label="",widget=forms.TextInput(attrs={
        'class':'form-control','maxlength':'50','placeholder':'Name'}))
    Contact=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Contact','class':'form-control'}))
    Address=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control','max_length':'50','placeholder':'Address'}))