class Viagem: 
    def __init__(self):
        
        self.distancia_km = 0
        self.tempo_gasto = 0

    def calc_velocidade_media(self):
        
        vel_media = (self.distancia_km/self.tempo_gasto)
        
        return vel_media


natal_mossoro = Viagem()

natal_mossoro.distancia_km = 279
natal_mossoro.tempo_gasto = 3

natal_parnamirim = Viagem()
natal_parnamirim.distancia_km = 30
natal_parnamirim.tempo_gasto = 0.4

print(Viagem.calc_velocidade_media(natal_mossoro))
print(Viagem.calc_velocidade_media(natal_parnamirim))

