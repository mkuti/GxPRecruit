from django.db import models


# Create your models here.
class Location(models.Model):
    '''
    Setting all locations which are related to the Job model.
    '''
    class Meta:
        verbose_name_plural = 'Locations'

    locations = [
        ('Remote', 'remote'),
        ('Overseas', 'overseas'),
        ('Cork', 'cork'),
        ('Galway', 'galway'),
        ('Dublin', 'dublin'),
    ]

    name = models.CharField(max_length=15, choices=locations, null=False)

    def __str__(self):
        return self.name

class Contract(models.Model):
    '''
    Setting all type of contracts which are related to the Job model.
    '''
    class Meta:
        verbose_name_plural = 'Contracts'

    contracts = [
        ('Permanent', 'permanent'),
        ('6 Months', '6 months'),
        ('1 Year', '1 year'),
    ]

    name = models.CharField(max_length=15, choices=contracts, null=False)

    def __str__(self):
        return self.name
        
class Schedule(models.Model):
    '''
    Setting all type of schedules which are related to the Job model.
    '''
    class Meta:
        verbose_name_plural = 'Schedules'

    schedules = [
        ('Full Time', 'full time'),
        ('Part Time', 'part time'),
        ('20 Hours', '20 hours'),
    ]

    name = models.CharField(max_length=15, choices=schedules, null=False)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    job_contract = models.ForeignKey(
        Contract,
        on_delete=models.SET_NULL,
        null=True)
    job_location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True)
    job_schedule = models.ForeignKey(
        Schedule,
        on_delete=models.SET_NULL,
        null=True)

    def __str__(self):
        return self.title
