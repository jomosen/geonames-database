from typing import Generator
from src.application.services.abstract_geonames_importer import AbstractGeoNamesImporter
from src.infrastructure.services.abstract_geonames_file_importer import AbstractGeoNamesFileImporter
from src.infrastructure.services.mappers.geoname_file_row_importer import GeoNameFileRowMapper
from src.domain.geonames.geoname import GeoName


class CityGeoNamesFileImporter(AbstractGeoNamesFileImporter, AbstractGeoNamesImporter[GeoName]):

    FILE_URL = "https://download.geonames.org/export/dump/cities500.zip"

    def __init__(self):
        super().__init__(download_url=self.FILE_URL)
        self.mapper = GeoNameFileRowMapper()

    

    def load_entities(self) -> Generator[GeoName, None, None]:
        for raw_row in self.read_raw_data():
            try:
                yield self.mapper.to_entity(raw_row)
            except ValueError:
                continue
            except Exception as e:
                print(f"Error processing row {raw_row}: {e}")