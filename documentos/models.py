from django.db import models

class Documento(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('acordao', 'Acórdão'),
        ('decisao', 'Decisão'),
        ('despacho', 'Despacho'),
    ]
    
    TIPO_PROCESSO_CHOICES = [
        ('concentracao', 'Ato de Concentração'),
        ('administrativo', 'Processo Administrativo'),
    ]
    
    SETOR_CHOICES = [
        ('energia', 'Energia'),
        ('telecom', 'Telecomunicações'),
        ('transporte', 'Transporte'),
    ]

    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='documentos/')
    tipo_documento = models.CharField(max_length=20, choices=TIPO_DOCUMENTO_CHOICES)
    tipo_processo = models.CharField(max_length=20, choices=TIPO_PROCESSO_CHOICES)
    setor = models.CharField(max_length=20, choices=SETOR_CHOICES)
    ano = models.IntegerField()
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_upload']