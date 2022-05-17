# Coded by Victor Li Team 4

# import section
from flask import Flask
from flask import render_template
from flask import request
import csv  # Key library to read and view CSV file of Covid and real estate data

app = Flask(__name__)

# Route to go to home.html
@app.route('/', methods=['GET', 'POST'])
def root():
    # GET method with just a button if there is no CSV file
    if request.method == 'GET':
        return render_template('home.html')
    # POST method that opens and adds the rows of the CSV file into an array of dictionaries
    elif request.method == 'POST':
        results = []

        with open('data.csv', 'r') as f:
            reader = [dict(item) for item in csv.DictReader(f)]

        for row in reader:
            results.append(dict(row))

        fieldnames = [key for key in results[0].keys()]
        return render_template('home.html', results=results, fieldnames=fieldnames, len=len)

# Runs the Flask application
if __name__ == '__main__':
    app.run(debug=True)
