import uuid
from abc import ABC
from typing import Any, TypeVar
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class EntityBase(ABC):
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

EntityType = TypeVar("EntityType", bound=EntityBase)