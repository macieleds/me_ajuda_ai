from flask_restful import Resource, reqparse
from models.job import JobModel

jobs = [
    {
        'job_id': 'alpha',
        'nome': 'alhpajobs',
        'estrelas': 4.3,
        'diaria': 450.00,
        'cidade': 'São Paulo'
    },
        {
        'job_id': 'omega',
        'nome': 'omegajobs',
        'estrelas': 3.4,
        'diaria': 480.00,
        'cidade': 'Rio Grande do Sul'
    },
            {
        'job_id': 'gama',
        'nome': 'gamajobsjobs',
        'estrelas': 4.8,
        'diaria': 340.00,
        'cidade': 'Corona Virus Town'
    }
    
]

class Jobs(Resource):
    def get(self):
        return {'jobs': jobs}   

class Job(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')
    
    def get (self, job_id):
        job = JobModel.find_job(job_id)
        if job:
            return job.json()
        return {'message': 'Job não encontrado.'}, 404 # not found  
            
              
    def post (self, job_id):
        
        if JobModel.find_job(job_id):
            return {"message": "Esse id de job '({})' já existe.".format(job_id)}, 400 #Bad Request
        dados = Job.atributos.parse_args()
        job = JobModel(job_id, **dados)  
        job.save_job()
        return job.json()
        
         

    def put (self, job_id):
        dados = Job.atributos.parse_args()
        job_objeto = JobModel(job_id, **dados)
        novo_job = job_objeto.json()
        job = Job.find_job(job_id)   
        if job:
            job.update(novo_job) 
            return novo_job, 200 # OK   
        jobs.append(novo_job)    
        return novo_job, 201 #criado
        
    
    def delete (self, job_id):
        global jobs
        jobs = [job for job in jobs if job['job_id'] != job_id]
        return {'message': 'Job deletado.'}    