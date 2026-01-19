
"""
Archivo principal para ejecutar la aplicación.
Demuestra instantiation, uso de servicios y la salida en consola.
"""

from Modelos.Empleado import Empleado
from Modelos.Chef import Chef
from Servicios.Cocina_service import mostrar_actividad_empleados, crear_chef_ejemplo

def main():
    # Crear instancias (se crean instancias de la clase base y derivada)
    emp1 = Empleado("Carlos", 500.0)
    chef1 = Chef("Ana", 1200.0, "Cocina internacional")
    chef2 = crear_chef_ejemplo()

    # Modificar salario usando la propiedad (encapsulación)
    emp1.salario = 550.0
    # chef1. Salario = -100 # esto lanzaría un ValueError (validación en setter)

    # Lista polimórfica: todos son tratados como Empleado, pero cada uno actúa distinto
    empleados = [emp1, chef1, chef2]

    actividades = mostrar_actividad_empleados(empleados)
    for a in actividades:
        print(a)

    # Uso de método específico de Chef
    print(chef1.preparar_plato("risotto de champiñones"))

if __name__ == "__main__":
    main()

