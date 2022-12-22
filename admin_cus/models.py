from django.db import models

class sample(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    is_sample = models.BooleanField()
    class Meta:
        verbose_name_plural = "Simple"

    # def name_count(self,):
    #     return self.email.count()

    def is_name_starting_with_k(self,):
        if self.phone > 7:
            print("Hello")
        
# Create your models here.
