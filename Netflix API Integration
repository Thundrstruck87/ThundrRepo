# This program will search the Netflix API to list all movie and/or shows that have a particular actor or actress
# API database being used is RapidAPI
#
#
import requests

actor = input("Please enter the name of the Actor or Actress: ")

url = "https://unogsng.p.rapidapi.com/people"

querystring = {"name":"{}".format(actor.casefold())}

headers = {
    'x-rapidapi-key': "4859ed6d76mshd24e36a328c8cd3p133253jsn7b0a50af935c",
    'x-rapidapi-host': "unogsng.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
