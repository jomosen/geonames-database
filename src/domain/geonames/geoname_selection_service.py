from typing import List, Dict, Any
from src.domain.geonames.geoname import GeoName
from src.domain.geonames.abstract_geoname_repository import AbstractGeoNameRepository
from src.domain.geonames.abstract_country_geoname_repository import AbstractCountryGeoNameRepository
from src.domain.geonames.geoname_selection_criteria_vo import GeonameSelectionCriteriaVO


class GeoNameSelectionService:
    
    def __init__(self, 
                 geoname_repository: AbstractGeoNameRepository, 
                 country_repository: AbstractCountryGeoNameRepository):
        
        self.geoname_repository = geoname_repository
        self.country_repository = country_repository

    def select(self, config: GeonameSelectionCriteriaVO) -> List[GeoName]:

        filters = self._build_filters(config)
        if not filters:
            return [] 

        geonames = self.geoname_repository.find_all(filters)
        
        return geonames
    
    def _build_filters(self, config: GeonameSelectionCriteriaVO) -> Dict[str, Any]:

        filters: Dict[str, Any] = {}
        
        if config.scope == "country":
            country = self.country_repository.find_by_id(config.geoname_id)
            if not country:
                return {}

            filters["country_code"] = country.iso_alpha2

            if config.depth_level == "admin1":
                filters["feature_code"] = "ADM1"
            elif config.depth_level == "admin2":
                filters["feature_code"] = "ADM2"
            elif config.depth_level == "admin3":
                filters["feature_code"] = "ADM3"
            else:
                filters["feature_class"] = "P"
                filters["min_population"] = config.min_population
        
        return filters