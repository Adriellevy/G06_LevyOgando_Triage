from Classes import *
def cargarpacientes_sin_atender():
    Organizador = cManejoArchivo()
    Lista_Pacientes = []
    Enum = ["rojo", "naranja", "amarillo", "verde", "azul"]
    cant = 20  # seteo el numero de pacientes
    # AGREGO 20 PACIENTES A UNA LISTA
    for i in range(0, cant):
        nombre = "" + str(i)  # seteo el nombre de los pacientes
        gravedad = i % 5  # seteo la gravedad de forma que la gravedad de los pacientes es ciclica de 0 a 4
        enfermero=cEnfermero(nombre,"00"+str(i))
        pac = cPaciente(nombre, Enum[gravedad], 1, None, enfermero, None)  # El seteo de la gravedad es al estilo enum
        Organizador.agregar_paciente(pac)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cargarpacientes_sin_atender()