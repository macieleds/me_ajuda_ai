from flask_restful import Resource, reqparse


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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
        
    def find_job(job_id):   
        for job in jobs:
            if job ['job_id'] == job_id:
                return job    
        return None
    
              
    def get (self, job_id):
        job = Job.find_job(job_id)
        if job:
            return job
        return {'message': 'Job não encontrado.'}, 404 # not found  
            
              
    def post (self, job_id):

        dados = Job.argumentos.parse_args()
        novo_job = {'job_id': job_id, **dados}
        
        jobs.append(novo_job)
        return novo_job, 200        

    
    def put (self, job_id):
        
        dados = Job.argumentos.parse_args()
        novo_job = {'job_id': job_id, **dados}
        
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