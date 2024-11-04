from django.db import models
from django.utils.crypto import get_random_string
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.text import slugify


class Incoming(models.Model):
    ref = models.CharField(
        max_length=10, unique=True, default=get_random_string(length=10)
    )
    slug = models.SlugField(max_length=10, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    received_on = models.DateField(blank=True, null=True)
    conf = models.BooleanField('confidential',default=False)
    urgent = models.BooleanField(default=False)
    received_from = models.CharField("from", max_length=100, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    originally_from = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    letter_dated = models.DateField(blank=True, null=True,  default=timezone.now)
    subject = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="incoming_files/", blank=True, null=True)

    class Meta:
        ordering = ["-received_on"]
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.ref)
        super(Incoming, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.subject


class ChangeStatus(models.Model):
    STATUS_CHOICE_LIST = [
        ("received", "Received"),
        ("forwarded", "Forwarded"),
        ("responded", "Responded"),
        ("closed", "Closed"),
    ]
    incoming = models.ForeignKey(Incoming, on_delete=models.CASCADE, related_name="statuses")
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICE_LIST, default="received"
    )
    note = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="updated_files/", blank=True, null=True)
    date = models.DateField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date",]
        verbose_name_plural = "Change Statuses"

    def __str__(self):
        return f"{self.incoming.subject}"
