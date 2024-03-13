from flask import Flask, request
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect("Datenbank.db")

@app.route('/')
def start():
    return "Hallo, Welt!"


@app.route('/json_example', methods=['POST'])
def handle_json():
    cursor = connection.cursor()
    data = request.form.to_dict(flat=True)
    for key, value in data.items():
        cursor.execute(f"UPDATE symbols set count = {value} where id = '{key}'")
    connection.commit()
    connection.close()
    return "POST hat funktioniert!"


if __name__ == '__main__':
    app.run(debug=True)