import os

from flask import Flask, render_template, jsonify, abort, request

from .database import load_jobs_from_db, load_single_job_from_db, add_application_into_db


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

@app.route('/job/<id>')
def single_job_page(id):
    return render_template('job_description.html', job=load_single_job_from_db(id))

@app.route('/job/<id>/apply/', methods=['post'])
def apply_to_job(id):
    data = request.form  # Use request.form for post method
    job=load_single_job_from_db(id)
    add_application_into_db(job_id=id, data=data)
    return render_template('form_submitted.html', data=data)

@app.route('/api/jobs')
def jobs_api():
    return jsonify(load_jobs_from_db())

@app.route('/api/job/<id>')
def single_job_api(id):
    job = load_single_job_from_db(id)
    if job is not None:
        return jsonify(job)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)