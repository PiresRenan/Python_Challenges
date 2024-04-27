import time


class Cronometro:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def iniciar_cronometro(self):
        self.inicio = time.time()

    def parar_cronometro(self):
        self.fim = time.time()

    def calcular_tempo_decorrido(self):
        if self.inicio is None or self.fim is None:
            return "Cronômetro não foi iniciado ou parado."

        tempo_decorrido_segundos = self.fim - self.inicio

        horas = int(tempo_decorrido_segundos // 3600)
        minutos = int((tempo_decorrido_segundos % 3600) // 60)
        segundos = int(tempo_decorrido_segundos % 60)

        return f"Tempo decorrido: {horas}h {minutos}m {segundos}s"
