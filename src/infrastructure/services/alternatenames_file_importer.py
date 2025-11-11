from typing import Generator
from src.infrastructure.services.mappers.abstract_file_row_mapper import AbstractFileRowMapper
from src.application.services.abstract_geonames_importer import AbstractGeoNamesImporter
from src.infrastructure.services.abstract_geonames_file_importer import AbstractGeoNamesFileImporter
from src.domain.geonames.alternatename import AlternateName


class AlternateNamesFileImporter(AbstractGeoNamesFileImporter, AbstractGeoNamesImporter[AlternateName]):

    FILE_URL = "https://download.geonames.org/export/dump/alternateNamesV2.zip"

    def __init__(self, mapper: AbstractFileRowMapper[AlternateName]):
        super().__init__(download_url=self.FILE_URL)
        self.mapper = mapper

    def load_entities(self) -> Generator[AlternateName, None, None]:
        
        for raw_row in self.read_raw_data():
            try:
                entity = self.mapper.to_entity(raw_row)
                yield entity
            except ValueError:
                continue
            except Exception as e:
                print(f"Error processing row {raw_row}: {e}")