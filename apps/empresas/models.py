from django.db import models

from apps.core.models import BaseModel
from apps.contabilidades.models import Contabilidade


class Empresa(BaseModel):
    contabilidade = models.ForeignKey(Contabilidade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome