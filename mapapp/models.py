from django.contrib.gis.db import models


class ClickLocation(models.Model):
    point = models.PointField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Point ({self.point.x}, {self.point.y}) at {self.created_at}"

