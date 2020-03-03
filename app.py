from flask import Flask
from flask_restful import Api
from resources.jobs import Jobs, Job

app = Flask(__name__)
api = Api(app)



api.add_resource(Jobs, '/jobs')
api.add_resource(Job, '/jobs/<string:job_id>')

if __name__ == "__main__":
    app.run(debug=True)