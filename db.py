from fastapi import FastAPI
import mysql.connector
import requests

app = FastAPI()

@app.get("/fetch-data")
async def fetch_data():
    url = "https://suitecrmdemo.dtbc.eu/index.php?module=Leads&action=index"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response status is not successful
        data = response.json()
        return data
    except (requests.RequestException, ValueError) as e:
        return {"error": str(e)}

@app.get("/insert-data")
async def insert_data():
    # Connect to MySQL database
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12Eggy34",
        database="suitecrm"
    )
    cursor = cnx.cursor()

    # Fetch data from the provided link
    url = "https://suitecrmdemo.dtbc.eu/index.php?module=Leads&action=index"
    response = requests.get(url)
    data = response.json()

    # Insert data into MySQL database
    for item in data:
        office_phone = item["Office_Phone"]
        first_name = item["First_Name"]
        last_name = item["Last_Name"]
        query = "INSERT INTO leaad (office_phone, first_name, last_name) VALUES (%s, %s, %s)"
        values = (office_phone, first_name, last_name)
        cursor.execute(query, values)

    # Commit the changes and close the connection
    cnx.commit()
    cursor.close()
    cnx.close()

    return {"message": "Data inserted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
