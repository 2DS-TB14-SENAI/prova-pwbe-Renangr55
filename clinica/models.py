from django.db import models

# Create your models here.
class Medico(models.Model):

    
    especialidade_choice = (
        ('CAR',"Cardiologista"),
        ('ORT', "Ortopedista")
    ) 
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100,choices=especialidade_choice)
    crm = models.CharField(max_length=10,primary_key=True)
    email = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nome
    
    
class Consulta (models.Model):
    staus_choice = (
        ("agendado","agendado"),
        ("realizado","realizado"),
        ("cancelado","cancelado")
    )
    paciente = models.CharField(max_length=200)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico,on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=staus_choice)

    def __str__(self):
        return self.paciente


