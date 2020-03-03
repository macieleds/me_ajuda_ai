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
    def get (self, job_id):
        for job in jobs:
            if job ['job_id'] == job_id:
                return job
        return {'message': 'Job não encontrado.'}, 404 # not found  
            
              
    def post (self, job_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        
        
        dados = argumentos.parse_args()
        
        novo_job = {
            'job_id': job_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }
        
        jobs.append(novo_job)
        return novo_job, 200        

    
    def put (self, job_id):
        pass    
    
    def delete (self, job_id):
        pass      