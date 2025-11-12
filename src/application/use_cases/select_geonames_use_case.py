from typing import Any
from application.services.abstract_logger import AbstractLogger
from domain.geoname_selection_service import GeoNameSelectionService


class SelectGeoNamesUseCase:

    def __init__(self, 
                 service: GeoNameSelectionService, 
                 logger: AbstractLogger | None = None):
        
        self.service = service
        self.logger = logger

    def execute(self, filters: dict[str, Any]):

        geonames = []

        try:
            geonames = self.service.select(filters)

        except Exception as e:
            if self.logger:
                self.logger.error(e)
            raise e
        
        return geonames