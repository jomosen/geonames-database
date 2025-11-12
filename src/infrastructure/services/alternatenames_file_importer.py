from src.infrastructure.services.mappers.abstract_file_row_mapper import AbstractFileRowMapper
from src.application.services.abstract_geonames_importer import AbstractGeoNamesImporter
from src.infrastructure.services.abstract_geonames_file_importer import AbstractGeoNamesFileImporter
from src.domain.geonames.alternatename import AlternateName


class AlternateNamesFileImporter(AbstractGeoNamesFileImporter, AbstractGeoNamesImporter[AlternateName]):

    FILE_URL = "https://download.geonames.org/export/dump/alternateNamesV2.zip"

    def __init__(self, mapper: AbstractFileRowMapper[AlternateName]):
        super().__init__(download_url=self.FILE_URL, mapper=mapper)