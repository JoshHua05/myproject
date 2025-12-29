from django.db import models

# Create your models here.
class Purpose(models.Model):

    class Meta:
        verbose_name_plural = "Purpose" 

    purpose = models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return f"{self.purpose}"
   
class Cycle(models.Model):

    class Meta:
        verbose_name_plural = "Cycle" 

    cycle = models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return f"{self.cycle}"
    
class ProcessingCenter(models.Model):
    class Meta:
        verbose_name_plural = "Processing Center" 

    pcCode = models.CharField(max_length=20, null=True,blank=True)
    pcName = models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return self.pcName
    
class TreatmentFacility(models.Model):

    class Meta:
        verbose_name_plural = "Treatment Facility"

    mtfCode = models.IntegerField(max_length=20, null=True,blank=True)
    mtfName = models.CharField(max_length=20, null=True,blank=True)
    
    def __str__(self):
        return self.mtfName
    
class Applicant(models.Model):

    class Meta:
        verbose_name_plural = "Applicant" 

    SEX_CHOICES = [
        ("Male","Male"),
        ("Female","Female"),
    ]

    purpose = models.ForeignKey(Purpose, null=True,blank=True, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, null=True,blank=True, on_delete=models.CASCADE)
    pc = models.ForeignKey(ProcessingCenter, null=True,blank=True, on_delete=models.CASCADE)
    mtf = models.ForeignKey(TreatmentFacility, null=True,blank=True, on_delete=models.CASCADE)
    lastName = models.CharField(max_length=200,null=False,blank=False)
    firstName = models.CharField(max_length=200,null=False,blank=False)
    middleName = models.CharField(max_length=200, null=True,blank=True)
    suffix = models.CharField(max_length=20, null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    birthDate = models.CharField(max_length=50, null=True,blank=True)
    sex = models.CharField(max_length=10,choices=SEX_CHOICES, null=True,blank=True)
    contactNumber = models.CharField(max_length=50, null=True,blank=True)
    completeAddress = models.CharField(max_length=200, null=True,blank=True)
    region = models.CharField(max_length=50, null=True,blank=True)
    course = models.CharField(max_length=100, null=True,blank=True)
    educAttainment = models.CharField(max_length=200, null=True,blank=True)
    schoolAddress = models.CharField(max_length=200, null=True,blank=True)
    eligibility = models.CharField(max_length=100, null=True,blank=True)
    tesdaCert = models.CharField(max_length=200, null=True,blank=True)
    ncipTribe = models.CharField(max_length=200, null=True,blank=True)
    height = models.CharField(max_length=50, null=True,blank=True)
    weight = models.CharField(max_length=50, null=True,blank=True)
    religion = models.CharField(max_length=100, null=True,blank=True)
    milTraining = models.CharField(max_length=100, null=True,blank=True)
    skill = models.CharField(max_length=100, null=True,blank=True)


    def __str__(self):
        return f"{self.lastName} {self.firstName}"