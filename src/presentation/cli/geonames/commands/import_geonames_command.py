from typing import Type
from src.application.use_cases.base_use_case import BaseUseCase
from src.infrastructure.services.countries_api_importer import CountriesApiImporter
from src.infrastructure.services.admin_geonames_file_importer import AdminGeoNamesFileImporter
from src.infrastructure.services.city_geonames_file_importer import CityGeoNamesFileImporter
from src.infrastructure.services.alternatenames_file_importer import AlternateNamesFileImporter
from src.application.use_cases.import_countries_use_case import ImportCountriesUseCase
from src.application.use_cases.import_geonames_use_case import ImportGeoNamesUseCase
from src.application.use_cases.import_alternatenames_use_case import ImportAlternateNamesUseCase
from src.infrastructure.services.tqdm_progress_bar import TqdmProgressBar
from src.application.services.abstract_logger import AbstractLogger
from src.application.services.abstract_unit_of_work_factory import AbstractUnitOfWorkFactory


def import_geonames_data(uow_factory: AbstractUnitOfWorkFactory, logger: AbstractLogger | None = None):
    with uow_factory() as uow:
        # Countries
        _run_import(
            uow.country_geoname_repo,
            CountriesApiImporter(),
            ImportCountriesUseCase,
            "Importing countries",
            logger,
        )

        # Admin divisions
        _run_import(
            uow.admin_geoname_repo,
            AdminGeoNamesFileImporter(),
            ImportGeoNamesUseCase,
            "Importing admin divisions",
            logger,
        )

        # Cities
        _run_import(
            uow.city_geoname_repo,
            CityGeoNamesFileImporter(),
            ImportGeoNamesUseCase,
            "Importing cities",
            logger,
        )

        # Alternate names
        _run_import(
            uow.geoname_alternatename_repo,
            AlternateNamesFileImporter(),
            ImportAlternateNamesUseCase,
            "Importing alternate names",
            logger,
        )


def _run_import(repository, importer, use_case_cls: Type[BaseUseCase], desc, logger: AbstractLogger | None = None):
    use_case = use_case_cls(repository, importer)
    total, insert_generator = use_case.execute()

    if not total:
        return
    
    if logger:
        logger.info(f"{desc}: {total} records to import")

    with TqdmProgressBar(total=total, desc=desc, unit="records", colour="green") as progress:
        progress.run(insert_generator)

    if logger:
        logger.info(f"{total} records imported")
