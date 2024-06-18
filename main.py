from random import randint
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
import Essential_Functions

engine = create_engine('sqlite:///weather.db', echo=True)


SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'weather'
    id: Mapped[int] = mapped_column(primary_key=True)
    latitude: Mapped[float] = mapped_column()
    longitude: Mapped[float] = mapped_column()
    month: Mapped[int] = mapped_column()
    date: Mapped[int] = mapped_column()
    year: Mapped[int] = mapped_column()
    fiveYearTempAvg: Mapped[float] = mapped_column()
    fiveYearTempMin: Mapped[float] = mapped_column()
    fiveYearTempMax: Mapped[float] = mapped_column()
    fiveYearWindAvg: Mapped[float] = mapped_column()
    fiveYearWindMin: Mapped[float] = mapped_column()
    fiveYearWindMax: Mapped[float] = mapped_column()
    fiveYearRainSum: Mapped[float] = mapped_column()
    fiveYearRainMin: Mapped[float] = mapped_column()
    fiveYearRainMax: Mapped[float] = mapped_column()

    def __repr__(self):
        return (f"<User(latitude={self.latitude}, longitude={self.longitude}, "
                f"month={self.month}, date={self.date}, year={self.year}, "
                f"fiveYearTempAvg={self.fiveYearTempAvg},fiveYearTempMin={self.fiveYearTempMin}, "
                f"fiveYearTempMax={self.fiveYearTempMax}, fiveYearWindAvg={self.fiveYearWindAvg}, "
                f"fiveYearWindMin={self.fiveYearWindMin}, fiveYearWindMax={self.fiveYearWindMax}, "
                f"fiveYearRainSum={self.fiveYearRainSum}, fiveYearRainMin={self.fiveYearRainMin}, "
                f"fiveyearRainMax={self.fiveYearRainMax})>")

Base.metadata.create_all(bind=engine)

weatherInput = User(
    id=randint(1, 9000000),
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


with SessionLocal() as session:
    session.add(weatherInput)
    session.commit()


def query_all():
    with SessionLocal() as session:
        all_rows = session.execute(select(User)).scalars().all()
        for user in all_rows:
            print(user)

query_all()
