from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"Equipe: {self.nome} ({self.pais})"

class Piloto(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    data_nasc = models.DateField()

    def __str__(self):
        return f"Piloto: {self.nome} ({self.pais})"

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carro: {self.modelo} ({self.ano}), Equipe: {self.equipe.nome}"

class Circuito(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    comprimento = models.FloatField(help_text="Comprimento do circuito em km")

    def __str__(self):
        return f"Circuito: {self.nome} ({self.pais})"




    def __str__(self):
        return f"Vitória: {self.carro.modelo} ({self.carro.ano}), Piloto: {self.piloto.nome}, Corrida: {self.corrida.circuito.nome}, Número de Vitórias: {self.numero_vitorias}"

class Sponsor(models.Model):
    nome = models.CharField(max_length=100)
    valor_contrato = models.DecimalField(max_digits=10, decimal_places=2)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sponsor: {self.nome}, Equipe: {self.equipe.nome}"

class Temporada(models.Model):
    ano = models.IntegerField(unique=True)
    campeao_piloto = models.ForeignKey(Piloto, on_delete=models.SET_NULL, null=True, related_name="campeao_piloto")
    campeao_equipe = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, related_name="campeao_equipe")

    def __str__(self):
        return f"Temporada: {self.ano}, Campeão Piloto: {self.campeao_piloto.nome}, Campeão Equipe: {self.campeao_equipe.nome}"

class Corrida(models.Model):
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name='corridas')  # Adicionando related_name
    data = models.DateField()

    def __str__(self):
        return f"Corrida: {self.circuito.nome} ({self.temporada})"

class Classificacao(models.Model):
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE, related_name='classificacoes')
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    posicao = models.IntegerField()

    def __str__(self):
        return f"{self.piloto.nome} - {self.posicao}ª posição na corrida {self.corrida}"

class VitoriaF1(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    corrida = models.ForeignKey(Corrida, on_delete=models.CASCADE)
    numero_vitorias = models.IntegerField()