class JobModel:
    def __init__(self, job_id, nome, estrelas, diaria, cidade):
        self.job_id = job_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
    
    def json(self):
        return {
            'job_id': self.job_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }    
