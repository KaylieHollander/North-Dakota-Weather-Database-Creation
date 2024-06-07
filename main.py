from WeatherAPI import Weather
import Essential_Functions
import sqlite3
from sqlalchemy import create_engine, text, Column, String, Integer, Float, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

engine = create_engine('sqlite:///weather.db', echo=True)
with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))

    print(result)

session = Session(bind=engine)


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
Base.metadata.create_all(bind=engine)

weatherInput = User(
    id=1,
    latitude=Essential_Functions.meanTemp2019['latitude'],
    longitude=Essential_Functions.meanTemp2019['longitude'],
    month=Essential_Functions.Essentials.month(),
    date=Essential_Functions.Essentials.day(),
    year=Essential_Functions.Essentials.year(),
    fiveYearTempAvg=Essential_Functions.Essentials.TempAvg(),
    fiveYearTempMin=Essential_Functions.Essentials.TempMin(),
    fiveYearTempMax=Essential_Functions.Essentials.TempMax(),
    fiveYearWindAvg=Essential_Functions.Essentials.WindAvg(),
    fiveYearWindMin=Essential_Functions.Essentials.WindMin(),
    fiveYearWindMax=Essential_Functions.Essentials.WindMax(),
    fiveYearRainSum=Essential_Functions.Essentials.PrecipSum(),
    fiveYearRainMin=Essential_Functions.Essentials.PrecipMin(),
    fiveYearRainMax=Essential_Functions.Essentials.PrecipMax()
)

session.add_all([weatherInput])

session.commit()

