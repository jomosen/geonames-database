from src.infrastructure.services.mappers.country_file_row_mapper import CountryFileRowMapper
from src.infrastructure.services.mappers.geoname_file_row_importer import GeoNameFileRowMapper
from src.infrastructure.services.mappers.alternatename_file_row_mapper import AlternateNameFileRowMapper
from src.infrastructure.services.all_geonames_file_importer import AllGeoNamesFileImporter
from src.infrastructure.services.countries_file_importer import CountriesFileImporter
from src.infrastructure.services.admin_geonames_file_importer import AdminGeoNamesFileImporter
from src.infrastructure.services.city_geonames_file_importer import CityGeoNamesFileImporter
from src.infrastructure.services.alternatenames_file_importer import AlternateNamesFileImporter

GEONAMES_IMPORT_CONFIG = [
    {
        "description": "Importing countries",
        "importer_cls": CountriesFileImporter,
        "mapper_cls": CountryFileRowMapper,
        "repository_attr": "country_geoname_repo",
    },
    {
        "description": "Importing admin divisions",
        "importer_cls": AdminGeoNamesFileImporter,
        "mapper_cls": GeoNameFileRowMapper,
        "repository_attr": "admin_geoname_repo",
    },
    {
        "description": "Importing cities",
        "importer_cls": CityGeoNamesFileImporter,
        "mapper_cls": GeoNameFileRowMapper,
        "repository_attr": "city_geoname_repo",
    },
    {
        "description": "Importing alternate names",
        "importer_cls": AlternateNamesFileImporter,
        "mapper_cls": AlternateNameFileRowMapper,
        "repository_attr": "geoname_alternatename_repo",
    },
    {
        "description": "Importing all geonames",
        "importer_cls": AllGeoNamesFileImporter,
        "mapper_cls": GeoNameFileRowMapper,
        "repository_attr": "geoname_repo",
    },
]