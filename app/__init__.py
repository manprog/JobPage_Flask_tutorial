import os

from flask import Flask, render_template, jsonify

from .database import load_jobs_from_db

# jobs_context = [
#             {
#                 'id': 1,
#                 'title': "Data Analyst",
#                 'location': 'Bremen',
#                 'salary': '50k'
#             },
#             {
#                 'id': 2,
#                 'title': "Python Programmer",
#                 'location': 'Paris',
#                 'salary': '60k'
#             },
#             {
#                 'id': 1,
#                 'title': "Frontend Developer",
#                 'location': 'Berlin',
#                 'salary': '45k'
#             },
#             {
#                 'id': 1,
#                 'title': "Backend Developer",
#                 'location': 'Multan'
#             }
#             ]


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


@app.route('/')
def index():
    return render_template('index.html', jobs = load_jobs_from_db())

@app.route('/api/jobs')
def jobs():
    return jsonify(load_jobs_from_db())

if __name__ == '__main__':
    app.run(debug=True)