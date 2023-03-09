import os

from flask import Flask, render_template, jsonify

jobs_context = [
            {
                'id': 1,
                'title': "Data Analyst",
                'location': 'Bremen',
                'salary': '50k'
            },
            {
                'id': 2,
                'title': "Python Programmer",
                'location': 'Paris',
                'salary': '60k'
            },
            {
                'id': 1,
                'title': "Frontend Developer",
                'location': 'Berlin',
                'salary': '45k'
            },
            {
                'id': 1,
                'title': "Backend Developer",
                'location': 'Multan'
            }
            ]


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World! Just testing'

@app.route('/')
def index():
    return render_template('index.html', jobs = jobs_context)

@app.route('/api/jobs')
def jobs():
    return jsonify(jobs_context)

if __name__ == '__main__':
    app.run(debug=True)