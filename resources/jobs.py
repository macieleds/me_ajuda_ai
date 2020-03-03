from flask_restful import Resource


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
        pass    
    
    def put (self, job_id):
        pass    
    
    def delete (self, job_id):
        pass      