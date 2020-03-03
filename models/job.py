from sql_alchemy import banco

class JobModel(banco.Model):
    __tablename__ = 'jobs'
    
    job_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

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

    @classmethod
    def find_job(cls, job_id):
        job = cls.query.filter_by(job_id=job_id).first()  #Comando executado ex.: SELECT * FROM jobs WHERE job_id = $job_id LIMIT=1
        if job: 
            return job
        return None
    
    def save_job(self):
        banco.session.add(self)
        banco.session.commit()