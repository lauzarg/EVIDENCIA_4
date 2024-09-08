from Maquina_jugo import MaquinaJuguera
import pytest

def test_maquina_jugo():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    assert isinstance(maquina_de_jugo_1, MaquinaJuguera)

def test_estado_en_str():
    maquina_de_jugo_1 = MaquinaJuguera (50)
    string_respuesta = "Máquina exprimidora: encendida, capacidad máxima: 50 ml, jugo actual: 0 ml"
    assert str(maquina_de_jugo_1) == string_respuesta

def encendido_maquina():
    maquina_de_jugo_1 = MaquinaJuguera(50)

def test_encender():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    assert not maquina_de_jugo_1._encendida
    maquina_de_jugo_1.encender()
    assert maquina_de_jugo_1._encendida

def test_ajustar_potencia_valor_valido():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    maquina_de_jugo_1.ajustar_potencia(50)
    assert maquina_de_jugo_1.potencia == 50

def test_ajustar_potencia_valor_menor_a_cero():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    with pytest.raises(ValueError):
        maquina_de_jugo_1.ajustar_potencia(-10)

def test_ajustar_potencia_valor_mayor_a_cien():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    with pytest.raises(ValueError):
        maquina_de_jugo_1.ajustar_potencia(110)

def test_procesar_frutas_encendida():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    maquina_de_jugo_1.encender()
    maquina_de_jugo_1.procesar_frutas()

def test_procesar_frutas_apagada():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    with pytest.raises(ValueError):
        maquina_de_jugo_1.procesar_frutas()

@pytest.fixture
def test_jugo_extraido(mostrar_jugo_extraido):
    resultado = mostrar_jugo_extraido (50)
    assert resultado == "Se extrajo 5.0 ml de jugo"

def test_getter_jugo_en_jarra():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    maquina_de_jugo_1.jugo_en_jarra = 30
    assert maquina_de_jugo_1.jugo_en_jarra == 30

def test_setter_jugo_en_jarra_valor_valido():
    maquina_de_jugo_1 = MaquinaJuguera(50)
    maquina_de_jugo_1.jugo_en_jarra = 25
    assert maquina_de_jugo_1.jugo_en_jarra == 25


def test_setter_jugo_en_jarra_valor_excede_capacidad():
    maquina_de_jugo_1= MaquinaJuguera(50)
    with pytest.raises(ValueError):
        maquina_de_jugo_1.jugo_en_jarra = 60

