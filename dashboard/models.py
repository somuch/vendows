from django.db import models

# Create your models here.
class Job(models.Model):
    STATUS_CHOICES = [
        (0, ''),
        (1, 'Passed'),
        (2, 'Failed'),
        (3, 'Running'),
    ]
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField('start at', default=None)
    complete_at = models.DateTimeField('complete_at', default=None, blank=True, null=True)
    status = models.SmallIntegerField(default=0, choices=STATUS_CHOICES)
    test_report = models.TextField(null=True, blank=True)

