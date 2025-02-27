# Flask REST API

This project contains multiple Flask-based REST APIs for handling various functionalities, including students, books, movies, and football players.

## Requirements
Make sure you have the following dependencies installed:
```bash
pip install flask flask-restful pymysql pymongo
```

## API Endpoints

### Students API
- **Add Student** (`POST /student/add`)
- **Get All Students** (`GET /students/all`)
- **Update Student Age** (`PUT /student/ageupdate`)
- **Delete Student** (`DELETE /student/delete`)

### Books API
- **Get All Books** (`GET /books/all`)(mongodb database)

### Movies API
- **Search Movie by Name** (`GET /movie/search/<name>`)
- **Search Movie by Release Year** (`GET /movie/search/<release_year>`)

### Football Players API
- **Get Players by Nationality** (`GET /player/<nationality>`)

## Running the API
To start the API, run the respective script:
```bash
python <script_name>.py
```
For example:
```bash
python Allstudent.py
```

## Notes
- The API connects to MySQL and MongoDB databases.
- Ensure the database credentials are configured correctly in the scripts.
- Run the scripts in a Python environment with the necessary dependencies installed.

