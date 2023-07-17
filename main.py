from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import mysql.connector
import httpx
import json

class Lead(BaseModel):
    phone_work: str
    first_name: str
    last_name: str

app = FastAPI()
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12Eggy34",
    database="suitecrm"
)
cursor = db.cursor()



@app.get("/collect-leads")
async def collect_leads():
    # SuiteCRM API credentials
    url = "https://suitecrmdemo.dtbc.eu/service/v4/rest.php"
    username = "Demo"
    password = "Demo"  # Please use the actual MD5 hashed password here

    # Fetching leads from SuiteCRM API
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url = "https://suitecrmdemo.dtbc.eu/index.php?module=Leads&action=index",
            params={
                "operation": "query",
                "sessionName": "your_session_name",
                "elementType": "Leads",
                "selectFields": "Office Phone,First Name,Last Name",
                "maxResults": 1000,  # Adjust as per your requirements
            },
            auth=(username, password)
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch Leads from SuiteCRM API")

        leads = response.json().get("result")


    # Storing leads in the MySQL database
    for lead in leads:
        lead_data = Lead(**lead)
        query = "INSERT INTO leads (phone_work, first_name, last_name) VALUES (%s, %s, %s)"
        values = (lead_data.phone_work, lead_data.first_name, lead_data.last_name)
        cursor.execute(query, values)
    db.commit()

    return {"message": "Leads collected and stored successfully."}

@app.get("/fetch-bitcoin-price")
async def fetch_bitcoin_price():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch Bitcoin price")

        bitcoin_price = response.json().get("bpi").get("USD").get("rate_float")

    query = "INSERT INTO bitcoin_prices (price_values) VALUES (%s)"
    values = (bitcoin_price,)
    cursor.execute(query, values)
    db.commit()

    return {"message": "Bitcoin price fetched and stored successfully."}

if __name__ == "_main_":
    uvicorn.run(app, host="0.0.0.0", port=8000)