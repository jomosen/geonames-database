from dataclasses import dataclass
from typing import Optional


@dataclass
class Country:

    geoname_id: int
    iso_alpha2: str
    country_name: str
    iso_alpha3: Optional[str] = None
    iso_numeric: Optional[int] = None
    fips_code: Optional[str] = None
    capital: Optional[str] = None
    area_in_sq_km: Optional[float] = None
    population: Optional[int] = None
    continent_code: Optional[str] = None
    continent_name: Optional[str] = None
    languages: Optional[str] = None
    currency_code: Optional[str] = None
    postal_code_format: Optional[str] = None
    north: Optional[float] = None
    south: Optional[float] = None
    east: Optional[float] = None
    west: Optional[float] = None
    has_geonames: Optional[bool] = None
