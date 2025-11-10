from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from src.domain.geonames.geoname import GeoName
from src.infrastructure.persistence.models.geoname_model import GeoNameModel


class GeoNamePersistenceMapper:

    @staticmethod
    def from_entity(entity: GeoName) -> GeoNameModel:

        return GeoNameModel(
            geoname_id=entity.geoname_id,
            name=entity.name,
            asciiname=entity.asciiname,
            alternatenames=entity.alternatenames,
            latitude=entity.latitude,
            longitude=entity.longitude,
            feature_class=entity.feature_class,
            feature_code=entity.feature_code,
            country_code=entity.country_code,
            admin1_code=entity.admin1_code,
            admin2_code=entity.admin2_code,
            population=entity.population,
            timezone=entity.timezone,
            modification_date=entity.modification_date,
        )

    @staticmethod
    def to_entity(model: Optional[GeoNameModel]) -> Optional[GeoName]:
        
        if model is None:
            return None

        return GeoName(
            geoname_id=model.geoname_id,
            name=model.name,
            asciiname=model.asciiname,
            alternatenames=model.alternatenames,
            latitude=float(model.latitude) if isinstance(model.latitude, Decimal) else model.latitude,
            longitude=float(model.longitude) if isinstance(model.longitude, Decimal) else model.longitude,
            feature_class=model.feature_class,
            feature_code=model.feature_code,
            country_code=model.country_code,
            cc2=model.cc2,
            admin1_code=model.admin1_code,
            admin2_code=model.admin2_code,
            admin3_code=model.admin3_code,
            admin4_code=model.admin4_code,
            population=model.population,
            elevation=model.elevation,
            dem=model.dem,
            timezone=model.timezone,
            modification_date=model.modification_date
            if isinstance(model.modification_date, date)
            else None,
            created_at=model.created_at if isinstance(model.created_at, datetime) else None,
            updated_at=model.updated_at if isinstance(model.updated_at, datetime) else None,
        )

    @staticmethod
    def to_model(entity: GeoName) -> GeoNameModel:
        return GeoNameModel(
            geoname_id=entity.geoname_id,
            name=entity.name,
            asciiname=entity.asciiname,
            alternatenames=entity.alternatenames,
            latitude=entity.latitude,
            longitude=entity.longitude,
            feature_class=entity.feature_class,
            feature_code=entity.feature_code,
            country_code=entity.country_code,
            cc2=entity.cc2,
            admin1_code=entity.admin1_code,
            admin2_code=entity.admin2_code,
            admin3_code=entity.admin3_code,
            admin4_code=entity.admin4_code,
            population=entity.population,
            elevation=entity.elevation,
            dem=entity.dem,
            timezone=entity.timezone,
            modification_date=entity.modification_date,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )