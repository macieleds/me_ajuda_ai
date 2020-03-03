from flask import Flask
from flask_restful import Api
from resources.jobs import Jobs, Job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #Para modificar o banco, só trocar o sqlite:///
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Jobs, '/jobs')
api.add_resource(Job, '/jobs/<string:job_id>')

if __name__ == "__main__":
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)