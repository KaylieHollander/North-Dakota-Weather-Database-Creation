There are 3 main files that are needed for this project: one for the essential functions, another to pull the data from the API, and the last to create the database.

1) API File
    - This file will retrieve all the necessary data from the weather API website.
    - The first step is to create a class using the following template:
        - class class_name:
    - Next, define all the instance variables needed using this template:
        - def __init__(self, variable_1....variable_14):
            self.variable_1 = variable_1
            ....
            self.variable_14 = variable_14
    - Before creating the modules to retrieve the weather data, determine the location and date you want to add to the database
    - To properly aggregate and insert the data into the database, you will need to pull data for each year separately
    - Create a total of 15 modules for the years 2019-2023. You will end up with one module per year per value
    - When creating the modules, use the following template:
        - def value_to_be_pulled_Year ():
    - Inside the module you created, use the statement variable_name_1 = requests.get('API URL') to pull the data from the website and store it in a variable
    - Next, take the above variable with the raw data and use the following statement to convert it to a JSON object. This will turn the data into a mutable object that can be used later:
        - variable_name_2 = variable_name_1.json()
    - The second-to-last step is to use the following statement to return the data from the weather API website:
        - return variable_name_2
    - The last step is to press the play button in the top right corner of the screen

2) Essential Functions File
    - You will need to import all of the data from the above api file using this template:
        - from file_name import class_name
    - First, use the following template to assign the API module data from the above file to local variables before creating the class
        - variable_name = API_File.module_name
        - Make sure you create a local variable for every module in the API file
    - Next, create a class using the following template:
        - class class_name:
    - Then you will create 12 modules in total to properly aggregate the data. For these modules, you will need to index the respective local variable as you would for a nested list to get the needed value.
        - 3 modules will be created to find the maximum values and 3 modules to find the minimum values for the temperature, wind, and precipitation respectively.
        - 2 modules will be created to find the averages for the temperature and wind
        - 1 module will be created to find the sum of the precipitation values from the chosen location
        - 3 modules will be created to find the day, month, and years respectively
    - After creating each module, extract the value from the list using the following template, and then return it:
        - Place_Holder = ""
          for x in max/min/average..:
            Place_Holder = precip_Place_Holder + str(x)
          return float/int(Place_Holder)
        - The purpose of the placeholder string is to temporarily store the list value so you can cast it as a float or integer
    - Once you have created the modules, press the play button in the top right corner of the screen

3) Database creation file
    - You will need to import the following libraries and files using the provided template:
        - from random import randint
        - from sqlalchemy import create_engine, select
        - from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
        - import Essential_Functions
    - Then you will use SQLAlchemy ORM to create a database and table by instantiating an engine, a session, a user class, a base class, and an instance of the user class to add the data into the rows
        - The engine is responsible for establishing the connection to the database. You will create it using this template:
            - engine = create_engine('sqlite:///weather.db', echo=True)
            - Replace weather.db with any name you want for your database
        - The session is the primary interface used to interact with the database. You will create the session and use a separate block of code to add rows of data to the table and commit them, using these templates:
            - SessionLocal = sessionmaker(bind=engine)
              with SessionLocal() as session:
                session.add(weatherInput)
                session.commit()
        - The user class is where you define the rows that are going to be in the table. You need to ensure that the name you gave the table in the engine matches the __tablename__ variable. Use this template to create the user class:
            - class User(Base):
                __tablename__ = 'weather'
                id: Mapped[int] = mapped_column(primary_key=True)
                latitude: Mapped[float] = mapped_column()
                ....
        - The base class helps in the creation and management of the mapped table rows in the user class. You will use the following template to create this class:
            - class Base(DeclarativeBase)
                    pass
        -  Add values into the cells of the table by assigning the row names you created above to the corresponding module from the Essential_Functions file. Use this template:
            - weatherInput = User(
            id=randint(1, 9000000),
            latitude=Essential_Functions.meanTemp2019['latitude'],
            longitude=Essential_Functions.meanTemp2019['longitude'],
            month=Essential_Functions.Essentials.month(),
            date=Essential_Functions.Essentials.day(),
            year=Essential_Functions.Essentials.year()
            ....
            )
    - After creating the database, table, and inserting all of the data, create a query to ensure that the table populated correctly. Use the following template:
        - def query_all():
            with SessionLocal() as session:
            all_rows = session.execute(select(User)).scalars().all()
            for user in all_rows:
                print(user)

          query_all()
    -  Once you have created the database and query, press the play button in the top right corner of the screen. This will return the everything in the table selected