from typing import Generator
from src.infrastructure.services.mappers.abstract_file_row_mapper import AbstractFileRowMapper
from src.application.services.abstract_geonames_importer import AbstractGeoNamesImporter
from src.infrastructure.services.abstract_geonames_file_importer import AbstractGeoNamesFileImporter
from src.domain.geonames.geoname import GeoName


class AllGeoNamesFileImporter(AbstractGeoNamesFileImporter, AbstractGeoNamesImporter[GeoName]):

    FILE_URL = "https://download.geonames.org/export/dump/allCountries.zip"

    def __init__(self, mapper: AbstractFileRowMapper[GeoName]):
        super().__init__(download_url=self.FILE_URL, mapper=mapper)