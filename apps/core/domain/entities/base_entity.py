import uuid
from datetime import datetime
from dataclasses import dataclass
from typing import Any, TypeVar, Optional


@dataclass(kw_only=True)
class EntityBase:
    id: Optional[uuid.UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, type(self)):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)

EntityType = TypeVar("EntityType", bound=EntityBase)