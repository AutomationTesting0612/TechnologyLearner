from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]

    project_name = models.CharField(max_length=255)
    leader_name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255,blank=True, null=True)
    num_students = models.PositiveIntegerField(blank=True, null=True)
    grade = models.CharField(max_length=20,blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    payment = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    payment_date = models.DateField(null=True, blank=True)
    pending_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

    def __str__(self):
        return self.project_name
