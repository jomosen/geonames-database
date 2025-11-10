from typing import Iterator, Tuple, Generator
from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.geonames.abstract_country_geoname_repository import AbstractCountryGeoNameRepository
from src.application.services.abstract_geonames_importer import AbstractGeoNamesImporter
from src.domain.geonames.country import Country


class ImportCountriesUseCase(BaseUseCase):

    def __init__(self, 
                 repository: AbstractCountryGeoNameRepository, 
                 importer: AbstractGeoNamesImporter[Country]):
        
        self.repository = repository
        self.importer = importer

    def execute(self) -> Tuple[int, Iterator[int]]:
        
        existing_count = self.repository.count_all()
        
        if existing_count > 0:
            return 0, iter([])
        
        total_records = self.importer.count_total_records()
        if total_records == 0:
            return 0, iter([])

        entities = self.importer.load_entities()

        def batch_insert_generator(entities: Generator[Country, None, None]) -> Iterator[int]:
            
            batch_size = 100 
            batch = []

            for entity in entities:
                batch.append(entity)
                
                if len(batch) >= batch_size:
                    self.repository.bulk_insert(batch)
                    yield len(batch) 
                    batch.clear()
            
            if batch:
                self.repository.bulk_insert(batch)
                yield len(batch)

        return total_records, batch_insert_generator(entities)