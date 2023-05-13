from flask import Flask, jsonify, request

app = Flask(__name__);

users = [
    {
        "id":1,
        "name": "John Doe M",
        "age": 26,
        "nationality": "English"
    },
     {
        "id":2,
        "name": "Maria Keys",
        "age": 32,
        "nationality": "American"
    },
     {
        "id":3,
        "name": "Kim Onono",
        "age": 28,
        "nationality": "Nigerian"
    },
     {
        "id":4,
        "name": "Larry Page",
        "age": 50,
        "nationality": "American"
    },
     {
        "id":5,
        "name": "Jui Wee",
        "age": 18,
        "nationality": "Korean"
    },
]

print("Hello...")

@app.route('/')
def mainRoute():
    return jsonify(users)