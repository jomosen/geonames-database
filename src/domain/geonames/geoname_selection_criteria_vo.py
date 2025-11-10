from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GeonameSelectionCriteriaVO:

    scope: str
    geoname_id: Optional[int] = None
    depth_level: Optional[str] = None
    min_population: Optional[int] = None
