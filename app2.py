from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_users():
    response = requests.get("https://dummyjson.com/users")
    if response.status_code == 200:
        return response.json()['users']
    return []

@app.route("/")
def show_home():
    users = get_users()
    return render_template('users.html', users = users)

if __name__ == "__main__":
    app.run(debug=True)