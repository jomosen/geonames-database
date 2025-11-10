from src.infrastructure.persistence.models.geoname_model import GeoNameModel
from src.infrastructure.persistence.repositories.sql_alchemy_geoname_repository import SqlAlchemyGeoNameRepository
from src.domain.geonames.abstract_geoname_repository import AbstractGeoNameRepository


class SqlAlchemyCityGeoNameRepository(SqlAlchemyGeoNameRepository, AbstractGeoNameRepository):

    def count_all(self) -> int:
        count = self.session.query(GeoNameModel).where(GeoNameModel.feature_class == "P").count()
        return count
