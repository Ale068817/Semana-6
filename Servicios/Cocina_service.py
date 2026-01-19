# services/cocina_service.py
from Modelos.Chef import Chef


def mostrar_actividad_empleados(empleados):

    resultados = []
    for emp in empleados:
        resultados.append(emp.trabajar())
    return resultados

def crear_chef_ejemplo():
    """Crea un Chef de ejemplo y retorna la instancia."""
    c = Chef("María", 800.0, "Pastelería")
    return c
