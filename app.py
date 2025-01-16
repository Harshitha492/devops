from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Connect to RDS
db = pymysql.connect(
    host="database-1.cv0a0s0iavm5.us-east-1.rds.amazonaws.com",
    user="admin",
    password="123456789",
    database="database-1"
)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data['name']
    skill = data['skill']
    with db.cursor() as cursor:
        cursor.execute("INSERT INTO skills (name, skill) VALUES (%s, %s)", (name, skill))
        db.commit()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
