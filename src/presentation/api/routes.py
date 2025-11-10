from fastapi import APIRouter, Query, Depends
from typing import Optional, List
from src.application.use_cases.select_geonames_use_case import SelectGeoNamesUseCase
from src.domain.geonames.geoname_selection_service import GeoNameSelectionService
from src.domain.geonames.geoname_selection_criteria_vo import GeonameSelectionCriteriaVO
from src.infrastructure.logging.system_logger import SystemLogger
from src.infrastructure.persistence.database.mysql_connector import MySQLConnector
from src.infrastructure.persistence.unit_of_work.sql_alchemy_unit_of_work_factory import SqlAlchemyUnitOfWorkFactory
from src.presentation.api.dependencies import get_uow_factory
from src.presentation.api.geoname_dto import GeoNameDTO
from src.presentation.api.geoname_mapper import GeoNameMapper


router = APIRouter(prefix="/geonames", tags=["GeoNames"])


@router.get("/", response_model=List[GeoNameDTO])
def get_geonames(
    scope: str = Query(..., description="Search scope: 'country'"),
    geoname_id: int = Query(..., description="GeoName ID of the country or region"),
    depth_level: Optional[str] = Query(
        None,
        description="Administrative depth: 'admin1', 'admin2', 'admin3', or None for populated places",
    ),
    min_population: Optional[int] = Query(
        None,
        description="Minimum population filter (used when depth_level is None)",
    ),
    uow_factory: SqlAlchemyUnitOfWorkFactory = Depends(get_uow_factory),
):
    criteria = GeonameSelectionCriteriaVO(
        scope=scope,
        geoname_id=geoname_id,
        depth_level=depth_level,
        min_population=min_population,
    )

    with uow_factory() as uow:
        service = GeoNameSelectionService(
            geoname_repository=uow.geoname_repo,
            country_repository=uow.country_geoname_repo
        )
        
        use_case = SelectGeoNamesUseCase(
            service=service
        )

        entities = use_case.execute(criteria)
        dtos = GeoNameMapper.to_dto_list(entities)
    
    return dtos