from typing import Any, Type
from src.application.services.abstract_logger import AbstractLogger
from src.application.services.abstract_unit_of_work_factory import AbstractUnitOfWorkFactory
from src.application.use_cases.base_use_case import BaseUseCase
from src.application.use_cases.import_geonames_use_case import ImportGeoNamesUseCase
from src.infrastructure.services.tqdm_progress_bar import TqdmProgressBar
from src.presentation.cli.geonames.commands.geonames_import_config import GEONAMES_IMPORT_CONFIG


def import_geonames_data(uow_factory: AbstractUnitOfWorkFactory, logger: AbstractLogger | None = None):
    
    with uow_factory() as uow:

        for import_config in GEONAMES_IMPORT_CONFIG:
            
            _run_import(
                getattr(uow, import_config["repository_attr"]),
                import_config["importer_cls"](
                    mapper=import_config["mapper_cls"]()
                ),
                ImportGeoNamesUseCase,
                import_config["description"],
                logger,
            )

def _run_import(repository: Any, importer: Any, use_case_cls: Type[BaseUseCase], description: str, logger: AbstractLogger | None = None):

    use_case = use_case_cls(repository, importer)

    try:
        total, insert_generator = use_case.execute()
        if not total:
            return
        
        if logger:
            logger.info(f"{description}: {total} records to import")

        with TqdmProgressBar(total=total, desc=description, unit="records", colour="green") as progress:
            progress.run(insert_generator)

        if logger:
            logger.info(f"{total} records imported")
    
    except Exception as e:
        if logger:
            logger.error(f"Error during {description}: {e}")
        return

    
