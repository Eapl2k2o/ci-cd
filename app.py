from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL connection (using environment variables from docker-compose.yml)
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'devops'

@app.route('/')
def hello():
    return "Hello, DevOps World!"

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
