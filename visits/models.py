from django.db import models

class Visit(models.Model):
    page = models.CharField(max_length = 255)
    username  = models.CharField(max_length = 255, default = 'Anonymous')
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f" Visit {self.pk}"

v = Visit()
print(v)