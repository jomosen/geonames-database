from typing import Generator, Tuple, Iterator
from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.geonames.geoname import GeoName
from src.domain.geonames.abstract_geoname_repository import AbstractGeoNameRepository
from src.application.services.abstract_geonames_importer import AbstractGeoNamesImporter


class ImportGeoNamesUseCase(BaseUseCase):

    def __init__(self, 
                 repository: AbstractGeoNameRepository, 
                 importer: AbstractGeoNamesImporter[GeoName]):
        
        self.repository = repository
        self.importer = importer
        
    def execute(self) -> Tuple[int, Iterator[int]]: 

        count = self.repository.count_all()
        if count > 0:
            return 0, iter([])

        self.importer.ensure_data_is_available()

        total_records = self.importer.count_total_records()
        if total_records == 0:
            return 0, iter([])

        entities = self.importer.load_entities()

        return total_records, self.batch_insert_generator(entities)
    
    def batch_insert_generator(self, entities: Generator[GeoName, None, None]) -> Iterator[int]:
            
        batch_size = 5000
        batch = []

        for entity in entities:
            batch.append(entity)
            
            if len(batch) >= batch_size:
                self.repository.bulk_insert(batch)
                
                yield batch_size 
                batch.clear()
        
        if batch:
            self.repository.bulk_insert(batch)
            yield len(batch)

        self.importer.cleanup()