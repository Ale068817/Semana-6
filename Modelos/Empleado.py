


class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        # atributo "privado" (convención): no acceder directamente desde fuera
        self._salario = salario

    # Encapsulación: getter y setter usando property (permite validación)
    @property
    def salario(self):
        """Devuelve el salario del empleado."""
        return self._salario

    @salario.setter
    def salario(self, valor):
        """Valida que el salario sea un número positivo antes de asignar."""
        if valor < 0:
            raise ValueError("El salario no puede ser negativo.")
        self._salario = valor

    def trabajar(self):
        """Método pensado para ser sobreescrito por clases derivadas (polimorfismo)."""
        return f"{self.nombre} está trabajando."

    def __str__(self):
        return f"Empleado(nombre={self.nombre}, salario={self._salario})"
