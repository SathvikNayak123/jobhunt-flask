from flask import Flask, render_template, jsonify, request
from database import load_jobs,search_jobs,add_application_to_db

app = Flask(__name__)

@app.route('/')
def home():
    jobs=load_jobs()
    return render_template('home.html',jobs=jobs)

@app.route('/api/json')
def list_jobs():
    jobs=load_jobs()
    return jsonify(jobs)

@app.route('/job/<int:id>')
def show_jobs(id):
    job = search_jobs(id)
    if not job:
        return "Not Found", 404
    else:
        return render_template('jobpage.html', job=job)
    
@app.route("/job/<int:id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = search_jobs(id)
  add_application_to_db(id, data)
  return render_template('submitted.html', 
                         application=data,
                         job=job)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
