import datetime as dt

import pytest
from Classes.cQuesMaestra import *


def test_Error_Insercion_Gravedad():
    """
    Este test tiene que asertar si al paciente se lo instancia con una gravedad distinta a las posibles
    :return:
    """
    with pytest.raises(cErrorGravedad):
        paciente_1 = cPaciente("Julian", "-")

def test_Paciente_Indepndendica_Gravedad_MayusMinus():
    """
    Este test tiene que asertar al darle a diferentes pacientes la misma gravedad si se escribe diferente
        :return:
    """
    paciente_1 = cPaciente("Julian", "AZUL")
    paciente_2 = cPaciente("andres", "azul")
    assert paciente_1.getGravedad() is paciente_2.getGravedad()

def test_Paciente_cambio_de_gravedad_naranja():
    """
    Si el paciente esta en sala de espera por mas del tiempo permitido debe cambiar de gravedad
    :return:
    """
    paciente_1 = cPaciente("1", "naranja")
    paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=10)
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 0

def test_Paciente_sin_cambio_de_gravedad_amarillo():
    with pytest.raises(cErrorPaciente):
        paciente_1 = cPaciente("2", "Amarillo")
        paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=50)
        paciente_1.setGravedadMayorPaciente()
        assert paciente_1.getGravedad() == 2

def test_Paciente_cambio_de_gravedad_amarillo():
    paciente_1 = cPaciente("2", "Amarillo")
    paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=60)
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 1
def test_Paciente_sin_cambio_de_gravedad_verde():
    with pytest.raises(cErrorPaciente):
        paciente_1 = cPaciente("3", "verde")
        paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=110)
        paciente_1.setGravedadMayorPaciente()
        assert paciente_1.getGravedad() == 3

def test_Paciente_cambio_de_gravedad_verde():
    paciente_1 = cPaciente("3", "verde")
    paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=120)
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 2
def test_Paciente_sin_cambio_de_gravedad_azul():
    with pytest.raises(cErrorPaciente):
        paciente_1 = cPaciente("4", "azul")
        paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=230)
        paciente_1.setGravedadMayorPaciente()
        assert paciente_1.getGravedad() == 4

def test_Paciente_cambio_de_gravedad_azul():
    paciente_1 = cPaciente("4", "azul")
    paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=240)
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 2

def test_Paciente_cambio_de_gravedad_varias_gravedades():
    paciente_1 = cPaciente("4", "azul")
    paciente_1.tiempoLlegada = paciente_1.tiempoLlegada - dt.timedelta(minutes=421)
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getGravedad() == 1

def test_Paciente_tiempo_restante():
    """
    Revisar este test
    :return:
    """
    paciente_1 = cPaciente("Julian", "naranja")
    paciente_1.tiempoLlegada = dt.datetime.now() - dt.timedelta(minutes=10)
    paciente_1.setGravedadMayorPaciente()
    assert paciente_1.getTiempoRestante() == dt.timedelta(0,0,0,0,0)


def test_cQuesMaestra_Insertar():
    paciente_1 = cPaciente("Julian", "rojo")
    paciente_2 = cPaciente("Julian2", "Verde")
    Organizador = cQuesMaestra()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    assert Organizador.V.qsize() == 1
    assert Organizador.R.qsize() == 1

def test_cQuesMaestra_Reorganizar():
    paciente_1 = cPaciente("Julian", "rojo")
    paciente_2 = cPaciente("Julian2", "Verde")
    Organizador = cQuesMaestra()
    Organizador.insert(paciente_1)
    Organizador.insert(paciente_2)
    paciente_1.tiempoLlegada = dt.datetime.now() - dt.timedelta(minutes=10)
    paciente_1.setGravedadMayorPaciente()
    Organizador.Reorganizar()
    assert 4==4