from django.db import models

class ActiveInactive(models.Model):
    visible = models.BooleanField(default=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self):
        self.visible = False
        self.deleted_at = timezone.now()
        self.save()
