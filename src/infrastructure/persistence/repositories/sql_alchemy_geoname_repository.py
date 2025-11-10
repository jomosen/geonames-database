from typing import List, Optional, Dict
from sqlalchemy.orm import Session
from src.domain.geonames.abstract_geoname_repository import AbstractGeoNameRepository
from src.domain.geonames.geoname import GeoName
from src.infrastructure.persistence.models.geoname_model import GeoNameModel
from src.infrastructure.persistence.mappers.geoname_persistence_mapper import GeoNamePersistenceMapper


class SqlAlchemyGeoNameRepository(AbstractGeoNameRepository):

    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, geoname_id: int) -> Optional[GeoName]:
        record = self.session.get(GeoNameModel, geoname_id)
        return GeoNamePersistenceMapper.to_entity(record) if record else None

    def find_all(self, filters: Optional[Dict] = None) -> List[GeoName]:
        filters = filters or {}
        query = self.session.query(GeoNameModel)

        if "country_code" in filters:
            query = query.filter(GeoNameModel.country_code == filters["country_code"])
        if "admin1_code" in filters:
            query = query.filter(GeoNameModel.admin1_code == filters["admin1_code"])
        if "admin2_code" in filters:
            query = query.filter(GeoNameModel.admin2_code == filters["admin2_code"])
        if "admin3_code" in filters:
            query = query.filter(GeoNameModel.admin3_code == filters["admin3_code"])
        if "admin4_code" in filters:
            query = query.filter(GeoNameModel.admin4_code == filters["admin4_code"])
        if "min_population" in filters:
            query = query.filter(GeoNameModel.population >= filters["min_population"])
        if "max_population" in filters:
            query = query.filter(GeoNameModel.population <= filters["max_population"])
        if "feature_class" in filters:
            query = query.filter(GeoNameModel.feature_class == filters["feature_class"])
        if "feature_code" in filters:
            query = query.filter(GeoNameModel.feature_code == filters["feature_code"])
        if "name_like" in filters:
            query = query.filter(GeoNameModel.name.ilike(f"%{filters['name_like']}%"))
        if "timezone" in filters:
            query = query.filter(GeoNameModel.timezone == filters["timezone"])

        return [GeoNamePersistenceMapper.to_entity(r) for r in query.all()]
    
    def save(self, entity: GeoName) -> None:
        model = GeoNamePersistenceMapper.to_model(entity)
        existing = self.session.get(GeoNameModel, model.geonameid)

        if existing:
            for attr, value in vars(model).items():
                if hasattr(existing, attr):
                    setattr(existing, attr, value)
        else:
            self.session.add(model)

        self.session.commit()

    def count_all(self) -> int:
        count = self.session.query(GeoNameModel).count()
        return count
    
    def bulk_insert(self, entities: List[GeoName]) -> None:
        models = [GeoNamePersistenceMapper.to_model(entity) for entity in entities]
        self.session.bulk_save_objects(models)
        self.session.commit()
