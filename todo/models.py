from django.db import models
from user.models import User


class Todo(models.Model):
    class Priority_status(models.IntegerChoices):
        LOW = 1 , "LOW"
        MEDIUM = 2 , "MEDIUM"
        HIGH = 3 , "HIGH"
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todo")
    title = models.CharField(max_length=100)
    priority = models.IntegerField(choices=Priority_status.choices,default=Priority_status.LOW)
    is_finished = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True,blank=True)
    
    
    class Meta:
        db_table = "Todo"
    
    def __str__(self):
        return str(self.title)
    