class MaquinaJuguera:
    def __init__(self, capacidad_max_jarra):
        self._encendida = False
        self.potencia = 0
        self.capacidad_max_jarra = capacidad_max_jarra
        self.jugo_en_jarra = 0

    def __str__(self):
        estado = "apagada" 
        if not self._encendida:
            estado = "encendida"
        return f"Máquina exprimidora: {estado}, capacidad máxima: {self.capacidad_max_jarra} ml, jugo actual: {self.jugo_en_jarra} ml"

    def encender(self):
        self._encendida = True

    def apagar(self):
        self._encendida = False

    def ajustar_potencia(self, nueva_potencia):
        if nueva_potencia <= 0 or nueva_potencia >= 100:
           raise ValueError("La potencia debe estar entre 0 y 100")
        
        self.potencia = nueva_potencia

    def procesar_frutas(self):
        if not self._encendida:
            raise ValueError("La máquina está apagada")
    
    def mostrar_jugo_extraido(self, cantidad_frutas):
        jugo_extraido = cantidad_frutas * self.potencia / 100 
        if self.jugo_en_jarra + jugo_extraido > self.capacidad_max_jarra:
            raise ValueError("La jarra está llena")

        self.jugo_en_jarra += jugo_extraido
        return f"Se extrajo {jugo_extraido} ml de jugo"
    
    @property
    def jugo_en_jarra(self):
        return self._jugo_en_jarra

    @jugo_en_jarra.setter
    def jugo_en_jarra(self, nueva_cantidad):
        if nueva_cantidad < 0 or nueva_cantidad > self.capacidad_max_jarra:
            raise ValueError("La cantidad de jugo debe estar entre 0 y la capacidad máxima")
        self._jugo_en_jarra = nueva_cantidad




maquina_de_jugo_1= MaquinaJuguera(50)
print (maquina_de_jugo_1)
    