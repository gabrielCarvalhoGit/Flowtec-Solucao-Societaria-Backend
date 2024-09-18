import uuid
from django.db import models
from apps.core.models import BaseModel


class Empresa(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.nome