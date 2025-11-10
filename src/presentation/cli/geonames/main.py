from pyfiglet import Figlet
from src.infrastructure.logging.system_logger import SystemLogger
from src.infrastructure.persistence.database.mysql_connector import MySQLConnector
from src.infrastructure.persistence.unit_of_work.sql_alchemy_unit_of_work_factory import SqlAlchemyUnitOfWorkFactory
from src.presentation.cli.geonames.commands.import_geonames_command import import_geonames_data


def main():
    figlet = Figlet(font="slant")
    print(figlet.renderText("GeoNames Importer"))

    logger = SystemLogger()

    db_connector = MySQLConnector(logger)
    db_connector.init_db()
    uow_factory = SqlAlchemyUnitOfWorkFactory(db_connector)

    import_geonames_data(uow_factory, logger)


if __name__ == "__main__":
    main()
