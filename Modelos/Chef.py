
from Modelos.Empleado import Empleado


class Chef(Empleado):
    def __init__(self, nombre: str, salario: float, especialidad: str):
        super().__init__(nombre, salario)
        self.especialidad = especialidad

    def preparar_plato(self, plato: str):
        """Método propio de Chef: preparar un plato."""
        return f"{self.nombre} (Chef de {self.especialidad}) está preparando {plato}."

    def trabajar(self):
        return f"{self.nombre} está cocinando. Especialidad: {self.especialidad}"

    def __str__(self):
        return f"Chef(nombre={self.nombre}, especialidad={self.especialidad}, salario={self._salario})"
