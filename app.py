# Alexander Yao (awy2108)
# ADI Labs Challenge

from flask import Flask, render_template
import requests
import re

# Request url
pokerest_url = 'http://pokeapi.co/api/v2/pokemon/'

# Output responses
invalid_query = """<h1> Invalid Pokemon! Please check your query </h1>"""
pokemon_id = """<h1> The pokemon with id {1} is {0}"""
pokemon_name = """<h1> {0} has id {1} </h1>"""

# Filter for valid requests
valid_chars = "^[A-Za-z0-9]*$"

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

# Dynamic endpoint for pokemon query
@app.route('/pokemon/<query>')
def pokemon_query(query):

    # Check valid ints or string
    if not re.match(valid_chars, query):
        return invalid_query
    query = query.lower()

    # Get pokemon response
    response = requests.post(pokerest_url + query)
    
    # Check response valid
    if response.status_code != 200:
        return invalid_query

    # Output correct statement (name,id)
    data = response.json()

    if query.isdigit():
        return pokemon_id.format(data['name'], data['id'])
    else:
        return pokemon_name.format(data['name'], data['id'])


if __name__ == '__main__':
    app.run()
