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
        return {'jobs': [job.json() for job in JobModel.query.all()]} #Equivalente - SELECT * FROM JOBS  

class Job(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="O campo 'nome' é de preenchimento obrigatório.")
    atributos.add_argument('estrelas', type=float)
    atributos.add_argument('diaria', type=float, required=True, help="O campo 'diaria' é de preenchimento obrigatório.")
    atributos.add_argument('cidade', type=str, required=True, help="O campo 'cidade' é de preenchimento obrigatório.")
    
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
        
        try:
            job.save_job()
        
        except: 
            return {'message': 'Ocorreu um erro interno ao salvar as informações'}
        return job.json()


    def put (self, job_id):
        dados = Job.atributos.parse_args()        
        job_encontrado = JobModel.find_job(job_id)   
        if job_encontrado:
            job_encontrado.update_hotel(**dados)
            job_encontrado.save_job()
            return job_encontrado.json(), 200 # OK  
        job = JobModel(job_id, **dados) 
        job.save_job()
        return job.json(), 201 #criado
        
    
    def delete (self, job_id):
        job = JobModel.find_job(job_id)
        if job:
            job.delete_job()
            return {'message': 'Job deletado.'}    
        return {'message': 'Job não encontrado.'}, 404 #not found