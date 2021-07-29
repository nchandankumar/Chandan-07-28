from django.db import models
from datetime import datetime
# Create your models here.
class Todo(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    date_created=models.DateTimeField(default=datetime.now(), blank=True)

    def str(self):
        return self.sno+ " "+ self.title
