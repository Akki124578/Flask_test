from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    return 'Savan Sutariya'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
