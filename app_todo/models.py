from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

#"This Django model defines a 'TodoItem' class with fields for title, description, completion status, creation date, and due date. 
#The '__str__' method ensures that instances of this class are represented by their titles. Clean and concise implementation for managing todo items. 