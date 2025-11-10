from typing import Optional
from decimal import Decimal
from src.domain.geonames.country import Country
from src.infrastructure.persistence.models.country_model import CountryModel


class CountryPersistenceMapper:
    
    @staticmethod
    def to_entity(model: Optional[CountryModel]) -> Optional[Country]:
        if model is None:
            return None

        return Country(
            geoname_id=model.geoname_id,
            iso_alpha2=model.iso_alpha2,
            country_name=model.country_name,
            iso_alpha3=model.iso_alpha3,
            iso_numeric=model.iso_numeric,
            fips_code=model.fips_code,
            capital=model.capital,
            area_in_sq_km=float(model.area_in_sq_km) if isinstance(model.area_in_sq_km, Decimal) else model.area_in_sq_km,
            population=model.population,
            continent_code=model.continent_code,
            continent_name=model.continent_name,
            languages=model.languages,
            currency_code=model.currency_code,
            postal_code_format=model.postal_code_format,
            north=float(model.north) if isinstance(model.north, Decimal) else model.north,
            south=float(model.south) if isinstance(model.south, Decimal) else model.south,
            east=float(model.east) if isinstance(model.east, Decimal) else model.east,
            west=float(model.west) if isinstance(model.west, Decimal) else model.west,
        )

    @staticmethod
    def to_model(entity: Country) -> CountryModel:
        return CountryModel(
            geoname_id=entity.geoname_id,
            iso_alpha2=entity.iso_alpha2,
            iso_alpha3=entity.iso_alpha3,
            iso_numeric=entity.iso_numeric,
            fips_code=entity.fips_code,
            country_name=entity.country_name,
            capital=entity.capital,
            area_in_sq_km=entity.area_in_sq_km,
            population=entity.population,
            continent_code=entity.continent_code,
            continent_name=entity.continent_name,
            languages=entity.languages,
            currency_code=entity.currency_code,
            postal_code_format=entity.postal_code_format,
            north=entity.north,
            south=entity.south,
            east=entity.east,
            west=entity.west,
        )
