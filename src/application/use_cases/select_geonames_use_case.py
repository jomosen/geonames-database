from src.domain.geonames.geoname_selection_service import GeoNameSelectionService
from src.domain.geonames.geoname_selection_criteria_vo import GeonameSelectionCriteriaVO

class SelectGeoNamesUseCase:
    def __init__(self, service: GeoNameSelectionService):
        self.service = service

    def execute(self, criteria_data: dict):
        criteria = GeonameSelectionCriteriaVO(**criteria_data)
        return self.service.select(criteria)
