from django.db import models

class TodoItem(models.Model):  #This Django model defines a 'TodoItem' class with several fields. 
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):  #The '__str__' method ensures that instances of this class are represented by their titles. 
        return self.title


