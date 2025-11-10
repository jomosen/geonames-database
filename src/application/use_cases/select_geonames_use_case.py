from typing import Any
from src.domain.geonames.geoname_selection_service import GeoNameSelectionService


class SelectGeoNamesUseCase:
    def __init__(self, service: GeoNameSelectionService):
        self.service = service

    def execute(self, filters: dict[str, Any]):
        return self.service.select(filters)