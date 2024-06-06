from WeatherAPI import Weather
import sqlite3
from sqlalchemy import create_engine, text, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, DeclarativeBase

meanTemp = Weather.mean_temp()
maxWind = Weather.max_wind()
rainSum = Weather.precip_sum()

engine = create_engine('sqlite:///weather.db', echo=True)
with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))

    print(result)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    date = Column(Integer)
    year = Column(Integer)
    fiveYearTempAvg = Column(Float)
    fiveYearTempMin = Column(Float)
    fiveYearTempMax = Column(Float)
    fiveYearWindAvg = Column(Float)
    fiveYearWindMin = Column(Float)
    fiveYearWindMax = Column(Float)
    fiveYearRainSum = Column(Float)
    fiveYearRainMin = Column(Float)
    fiveYearRainMax = Column(Float)

    def __repr__(self):
        return (f"<User(latitude={self.latitude}, longitude={self.longitude}, "
                f"month={self.month}, date={self.date}, year={self.year}, "
                f"fiveYearTempAvg={self.fiveYearTempAvg},fiveYearTempMin={self.fiveYearTempMin}, "
                f"fiveYearTempMax={self.fiveYearTempMax}, fiveYearWindAvg={self.fiveYearWindAvg}, "
                f"fiveYearWindMin={self.fiveYearWindMin}, fiveYearWindMax={self.fiveYearWindMax}, "
                f"fiveYearRainSum={self.fiveYearRainSum}, fiveYearRainMin={self.fiveYearRainMin}, "
                f"fiveyearRainMax={self.fiveYearRainMax})>")


#print("Creating Tables >>>>> ")
#Base.metadata.create_all(bind=engine)

print(meanTemp['longitude'])
