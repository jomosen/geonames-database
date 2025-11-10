from sqlalchemy import (
    Column,
    String,
    Integer,
    BigInteger,
    DECIMAL,
    CHAR
)
from src.infrastructure.persistence.models.base_model import BaseModel


class CountryModel(BaseModel):

    __tablename__ = "countries"

    geoname_id = Column(Integer, primary_key=True, autoincrement=False)
    iso_alpha2 = Column(CHAR(2), nullable=False)
    iso_alpha3 = Column(CHAR(3))
    iso_numeric = Column(Integer)
    fips_code = Column(CHAR(2))
    country_name = Column(String(100), nullable=False)
    capital = Column(String(100))
    area_in_sq_km = Column(DECIMAL(12, 2))
    population = Column(BigInteger)
    continent_code = Column(CHAR(2))
    continent_name = Column(String(50))
    languages = Column(String(255))
    currency_code = Column(CHAR(3))
    postal_code_format = Column(String(200))
    north = Column(DECIMAL(12, 8))
    south = Column(DECIMAL(12, 8))
    east = Column(DECIMAL(12, 8))
    west = Column(DECIMAL(12, 8))
