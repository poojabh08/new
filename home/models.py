from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator

class report(models.Model):
    Date=models.DateField('Date',null=True)
    patient=models.ForeignKey('patient',on_delete=models.SET_NULL,null=True)
    Hemoglobin=models.IntegerField('Hemoglobin',default=1,validators=[MaxValueValidator(60),MinValueValidator(0)])
    Neutrophils=models.IntegerField('Neutrophil',default=1,validators=[MaxValueValidator(80),MinValueValidator(0)])
    lymphocytes=models.IntegerField('lymphocytes',default=1,validators=[MaxValueValidator(60),MinValueValidator(0)])
    monocytes=models.IntegerField('monocytes',default=1,validators=[MaxValueValidator(10),MinValueValidator(0)])
    basophils=models.IntegerField('basophils',default=1,validators=[MaxValueValidator(1),MinValueValidator(0)])
    eosinophils=models.IntegerField('eosinophils',default=1,validators=[MaxValueValidator(10),MinValueValidator(0)])
    rbc=models.IntegerField('rbc',default=1,validators=[MaxValueValidator(7),MinValueValidator(0)])
    platelets=models.IntegerField('rbc',default=1,validators=[MaxValueValidator(400000),MinValueValidator(0)])

class patient(models.Model):
    patient_name=models.CharField('Patient name',max_length=30,null=True)
    sex=(('Male','male'),('Female','female'),('Others','others'))
    Sex=models.CharField('sex',choices=sex,blank=True,null=True,max_length=10)
    Dob=models.DateField('Date of Birth',null=True,blank=True)
    Age=models.IntegerField()
    Contact=PhoneNumberField('Contact',null=True)
    Address=models.CharField('Address',max_length=200,null=True)
    Email=models.EmailField('Email',blank=False,null=True)#unique=true
    blood_group=(('ab+','AB+'),('ab-','AB-'),('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('o-','O-'),('o+','O+'))
    Blood_group=models.CharField('blood group',max_length=4,choices=blood_group,blank=True)
    Password=models.CharField('password',max_length=20,null=True,blank=True)
    def __str__(self):
        return self.patient_name

class token(models.Model):
    Date=models.DateField('Date',null=True)
    doc=(
        ('dm','mahesh'),
        ('dh','rohit'),
        ('dr','rekha')
    )
    identity=models.IntegerField( null=True,blank=True)
    Doctor=models.ForeignKey('doctor',on_delete=models.SET_NULL,null=True)
    name=models.CharField('name',max_length=30,null=True)
    def __str__(self):
        return self.name

class doctor(models.Model):
    doctor_name=models.CharField('doctor name',max_length=30,null=True)
    token_number=models.IntegerField('Token number',blank=True,null=True)
    sex=(('male','male'),('female','female'),('others','others'))
    Sex=models.CharField('sex',choices=sex,blank=True,null=True,max_length=10)
    Contact=PhoneNumberField('Contact',null=True)
    Email=models.EmailField('Email',blank=False,unique=True,null=True)
    s=(('physician','physician'),('orthopedic','orthopedic'),('cardiologist','cardiologist'),('pediatrician','pediatrician'))
    Spec=models.CharField('specification',choices=s,blank=True,null=True,max_length=15)
    #av=models.BooleanField('Avaialable',default=True)
    pa=models.CharField('Password',blank=True,null=True,max_length=10)
    def __str__(self):
        return self.doctor_name

class bill(models.Model):
    Date=models.DateField('Date',null=True)
    ndays=models.IntegerField('ndays',blank=True,null=True)
    patient=models.ForeignKey('patient',on_delete=models.SET_NULL,null=True)
    ward=((500,'general'),(1000,'icu'))
    room=models.IntegerField('room',choices=ward,blank=True,null=True)
    report=models.IntegerField('report',blank=True,null=True)
    fee=models.IntegerField('fee',blank=True,null=True)
    operation=models.IntegerField('operation',blank=True,null=True,default=0)
    #med=((30,'dolo650'),(12,'saridon'),(9,'crocin'))
    #medicine=MultiSelectField('medicine',blank=True,null=True,choices=med)
    #medicine=models.IntegerField('medicine',blank=True,null=True)
    tot=models.IntegerField('total',default=0,blank=True,null=True)

class receptionist(models.Model):
    recp_name=models.CharField('Receiptionist name',max_length=30,null=True)
    sex=(('m','male'),('f','female'),('o','others'))
    Sex=models.CharField('sex',choices=sex,blank=True,null=True,max_length=10)
    Contact=PhoneNumberField('Contact',null=True)
    Email=models.EmailField('Email',blank=False,unique=True,null=True)
    pa=models.CharField('Password',blank=True,null=True,max_length=10)
    def __str__(self):
        return self.recp_name

class ambulance(models.Model):
    Name=models.CharField("Name",max_length=50,null=True)
    Contact=PhoneNumberField('Contact',null=True)
    Address=models.CharField('Address',null=True,max_length=200)