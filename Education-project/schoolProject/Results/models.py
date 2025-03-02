from django.db import models

class StudentResult(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    year_sem = models.CharField(max_length=10)  # Example: "3"
    exam_month = models.CharField(max_length=20)  # Example: "December"
    exam_year = models.IntegerField()  # Example: 2024
    exam_type = models.CharField(max_length=20)  # Example: "Regular"
    subject_details = models.JSONField()  # For storing detailed subject data
    percentage = models.FloatField(null=True, blank=True)
    result_status = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.roll_no}"

    
