from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AdditionalInformation(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class League(TimeStampModel, AdditionalInformation):
    logo = models.ImageField(upload_to='club/')
    country = models.CharField(max_length=30)


class Club(TimeStampModel, AdditionalInformation):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='leagues')
    stadium_name = models.CharField(max_length=30)
    club_logo = models.ImageField(upload_to='club_logo/')
