"""Model definition for nautobot_diagrams."""

from django.db import models

from nautobot.core.models import BaseModel

# from utilities.querysets import RestrictedQuerySet #comes from netbox_ui_plugin
from nautobot.utilities.querysets import RestrictedQuerySet


# Create your models here. Models should inherit from BaseModel.


# class SavedTopology(models.Model):
class SavedTopology(BaseModel):

    name = models.CharField(max_length=100, blank=True)
    topology = models.JSONField()
    layout_context = models.JSONField(null=True, blank=True)
    created_by = models.ForeignKey(
        # to="users.AdminUser", #comes from netbox_ui_plugin
        to="users.User",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    timestamp = models.DateTimeField()

    objects = RestrictedQuerySet.as_manager()

    def __str__(self):
        return str(self.name)