from django.db import models

# Create your models here.


class Enquiry(models.Model):
    """
    Model for enquiries
    """

    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    class Meta:
        """
        Ordering of enquiries
        in admin panel
        """

        verbose_name_plural = "Enquiries"
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.subject} ({self.email})"
