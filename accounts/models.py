from django.db import models
import uuid
# Create your models here

class SIP(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nameofSIP=models.CharField(max_length=1024)
    holderName=models.CharField(max_length=1024,choices=(('Rajesh','Rajesh'),('Rupesh','Rupesh'),('Ranjana','Ranjana'),('Ritesh','Ritesh')))
    sipAmount=models.FloatField()
    dateOfRenewel=models.DateField()
    def __str__(self) -> str:
        return self.nameofSIP
