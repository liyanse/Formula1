import requests
import json
import spacy
import datetime

### The dataset we'll be using has been provided as a json file at this link(https://ergast.com/api/f1/current.json)
def extract_data():
    url = "https://ergast.com/api/f1/current.json"
    response = requests.get(url)
    data = json.loads(response.text)
    
  ## Race information  
    races = data['MRData']['RaceTable']['Races']
    

    circuits = []
    for race in race:
        circuit = race["Circuit"]
        circuits.append(
            [
                circuit["circuitId"],
                circuit["circuitName"],
                circuit["Location"]["locality"],
                circuit["Location"]["country"],
            ]
        )

## Driver information
    url = "http://ergast.com/api/f1/current/driverStandings.json"
    response = requests.get(url)
    data = json.loads(response.text)

    leaderboard = []
    drivers = []
    teams = {}
    for driver in data["MRData"]["StandingsTable"]["StandingsLists"][0][
        "DriverStandings"
    ]:
        leaderboard.append(
            [
                driver["position"],
                driver["Driver"]["givenName"],
                driver["Driver"]["familyName"],
                driver["Constructors"][0]["name"],
                driver["points"],
            ]
        )
        drivers.append(
            [
                driver["Driver"]["driverId"],
                driver["Driver"]["givenName"],
                driver["Driver"]["familyName"],
                driver["Driver"]["nationality"],
                driver["Constructors"][0]["name"],
            ]
        )
        if driver["Constructors"][0]["name"] in teams:
            teams[driver["Constructors"][0]["name"]].append(
                [
                    driver["Driver"]["driverId"],
                    driver["Driver"]["givenName"],
                    driver["Driver"]["familyName"],
                ]
            )
        else:
            teams[driver["Constructors"][0]["name"]] = [
                [
                    driver["Driver"]["driverId"],
                    driver["Driver"]["givenName"],
                    driver["Driver"]["familyName"],
                ]
            ]

    return races, leaderboard, drivers, teams, circuits
