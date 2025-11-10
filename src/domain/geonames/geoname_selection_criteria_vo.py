from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GeoNameSelectionCriteriaVO:

    scope: Optional[str] = None
    geoname_id: Optional[int] = None
    depth_level: Optional[str] = None
    min_population: Optional[int] = None

    country_code: Optional[str] = None
    feature_class: Optional[str] = None
    feature_code: Optional[str] = None
