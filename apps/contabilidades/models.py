from apps.core.models import BaseModel


class Contabilidade(BaseModel):
    def __str__(self):
        return self.nome