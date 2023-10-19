import datetime as dt

import pytest
from Classes.cQuesMaestra import *
def test_insertar():
    paciente_1 = cPaciente("Julian", "rojo")
    paciente_2 = cPaciente("Julian2", "Verde")
    Organizador = cQuesMaestra()
    assert 4 == 4
    #assert square(3) == 9

@pytest.mark.xfail(raises=cErrorGravedad)
def test_Error_Insercion_Gravedad():
    paciente_1 = cPaciente("Julian", "-")

def test_Paciente_Indepndendica_Gravedad_MayusMinus():
    paciente_1 = cPaciente("Julian", "AZUL")
    paciente_2 = cPaciente("andres", "azul")
    assert paciente_1.getGravedad().color is paciente_2.getGravedad().color

def test_Paciente_cambio_de_gravedad():
    paciente_1 = cPaciente("Julian", "naranja")
    paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=10)
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad().color == 0

def test_Paciente_tiempo_restante():
    """
    Revisar este test
    :return:
    """
    paciente_1 = cPaciente("Julian", "naranja")
    #paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - (dt.datetime.now() - dt.timedelta(minutes=10))
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getTiempoRestante() == dt.timedelta(0,0,0,0,0)