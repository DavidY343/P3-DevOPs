class SistemaControlTemperatura:
    def __init__(self):
        self.I_TRef = None
        self.I_TReal = None
        self.O_SC_ON = False
        self.O_SR_ON = False
        self.I_Error_SC = False
        self.I_Error_SR = False
        self.O_ERROR_SYS = False

    def recibir_temperaturas(self, I_TRef, I_TReal):
        """Recibe las temperaturas de referencia y real"""
        self.I_TRef = I_TRef
        self.I_TReal = I_TReal

    def activar_calefaccion(self):
        """Activa o desactiva la calefacción dependiendo de la diferencia entre I_TRef y I_TReal"""
        if self.I_TReal < self.I_TRef - 0.5:
            self.O_SC_ON = True  # Encender calefacción
        else:
            self.O_SC_ON = False  # Apagar calefacción

    def activar_refrigeracion(self):
        """Activa o desactiva la refrigeración dependiendo de la diferencia entre I_TRef y I_TReal"""
        if self.I_TReal > self.I_TRef + 0.5:
            self.O_SR_ON = True  # Encender refrigeración
        else:
            self.O_SR_ON = False  # Apagar refrigeración

    def verificar_error_subsistemas(self):
        """Verifica si hay errores en los subsistemas"""
        if self.I_Error_SC or self.I_Error_SR:
            self.O_ERROR_SYS = True  # Error en el sistema
        else:
            self.O_ERROR_SYS = False  # Sin error

    def reiniciar_sistema(self):
        """Intenta reiniciar el sistema si hay un error"""
        if self.O_ERROR_SYS:
            # Simulación de reinicio del sistema
            self.O_ERROR_SYS = False
            return True  # Indica que el sistema se ha reiniciado
        return False  # Si no hay error, no se puede reiniciar

# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear una instancia del sistema
    sistema = SistemaControlTemperatura()

    # Simulación de entradas
    sistema.recibir_temperaturas(22, 21.4)  # I_TRef = 22, I_TReal = 21.4
    sistema.activar_calefaccion()
    print(f"Calefacción encendida: {sistema.O_SC_ON}")  # Debe ser True

    sistema.recibir_temperaturas(22, 22.6)  # I_TRef = 22, I_TReal = 22.6
    sistema.activar_refrigeracion()
    print(f"Refrigeración encendida: {sistema.O_SR_ON}")  # Debe ser True

    # Simulando error en subsistema calefacción
    sistema.I_Error_SC = True
    sistema.verificar_error_subsistemas()
    print(f"Error en el sistema: {sistema.O_ERROR_SYS}")  # Debe ser True

    # Intentar reiniciar el sistema
    reiniciado = sistema.reiniciar_sistema()
    print(f"¿Sistema reiniciado?: {reiniciado}")  # Debe ser True
    print(f"Error en el sistema después de reiniciar: {sistema.O_ERROR_SYS}")  # Debe ser False
