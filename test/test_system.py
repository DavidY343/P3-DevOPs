import unittest
from system import SistemaControlTemperatura

class TestSistemaControlTemperatura(unittest.TestCase):

    def setUp(self):
        """Inicializa una nueva instancia del sistema antes de cada prueba"""
        self.sistema = SistemaControlTemperatura()

    def test_activar_calefaccion(self):
        """Debe encender la calefacción si la temperatura real es menor que la de referencia - 0.5°C"""
        self.sistema.recibir_temperaturas(22, 21.4)
        self.sistema.activar_calefaccion()
        self.assertTrue(self.sistema.O_SC_ON)

    def test_no_activar_calefaccion(self):
        """No debe encender la calefacción si la temperatura está en el rango de tolerancia"""
        self.sistema.recibir_temperaturas(22, 21.6)
        self.sistema.activar_calefaccion()
        self.assertFalse(self.sistema.O_SC_ON)

    def test_activar_refrigeracion(self):
        """Debe encender la refrigeración si la temperatura real es mayor que la de referencia + 0.5°C"""
        self.sistema.recibir_temperaturas(22, 22.6)
        self.sistema.activar_refrigeracion()
        self.assertTrue(self.sistema.O_SR_ON)

    def test_no_activar_refrigeracion(self):
        """No debe encender la refrigeración si la temperatura está en el rango de tolerancia"""
        self.sistema.recibir_temperaturas(22, 22.4)
        self.sistema.activar_refrigeracion()
        self.assertFalse(self.sistema.O_SR_ON)

    def test_error_subsistemas(self):
        """Debe activar la señal de error del sistema si hay error en los subsistemas"""
        self.sistema.I_Error_SC = True
        self.sistema.verificar_error_subsistemas()
        self.assertTrue(self.sistema.O_ERROR_SYS)

    def test_no_error_subsistemas(self):
        """No debe activar la señal de error del sistema si no hay errores en los subsistemas"""
        self.sistema.I_Error_SC = False
        self.sistema.I_Error_SR = False
        self.sistema.verificar_error_subsistemas()
        self.assertFalse(self.sistema.O_ERROR_SYS)

    def test_reinicio_sistema(self):
        """Debe reiniciar el sistema si hay un error"""
        self.sistema.O_ERROR_SYS = True
        reiniciado = self.sistema.reiniciar_sistema()
        self.assertTrue(reiniciado)
        self.assertFalse(self.sistema.O_ERROR_SYS)

    def test_no_reinicio_sistema(self):
        """No debe reiniciar el sistema si no hay errores"""
        self.sistema.O_ERROR_SYS = False
        reiniciado = self.sistema.reiniciar_sistema()
        self.assertFalse(reiniciado)

if __name__ == '__main__':
    unittest.main()
