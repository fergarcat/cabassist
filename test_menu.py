# Funciones a probar en menu.py
# menu_display() → Muestra diferentes menús y toma entradas del usuario.
# Simularemos entradas con patch("builtins.input")
# Simularemos la impresión en consola con patch("builtins.print")
# Simularemos os.system('cls') con patch("os.system")

import pytest
from unittest.mock import patch
from menu import menu_display
from definitions import display_fees, display_drive, display_last_rides

class MockRide:
    def __init__(self):
        self.startTime = 1700000000
        self.endTime = 1700003600
        self.driveMeter = 20
        self.waitMeter = 10
        self.Fare = 15.0

@pytest.fixture
def ride():
    return MockRide()

# Test para el menú de bienvenida
@patch("builtins.print")
@patch("builtins.input", return_value="")
@patch("os.system")
def test_menu_welcome(mock_os, mock_input, mock_print, ride):
    menu_display("welcome", ride, [], 0.02, 0.05, "rides.csv")
    mock_print.assert_called()  # Verificar que imprime algo en consola
    mock_input.assert_called_once()  # Verificar que espera una entrada del usuario

# Test para el menú de inicio con opción "R" (reiniciar viaje)
@patch("builtins.print")
@patch("builtins.input", return_value="R")
@patch("os.system")
def test_menu_home_restart(mock_os, mock_input, mock_print, ride):
    result = menu_display("home", ride, [], 0.02, 0.05, "rides.csv")
    assert result == "R", "Se esperaba 'R' como opción seleccionada"

# Test para el menú de espera con opción "D" (comenzar a conducir)
@patch("builtins.print")
@patch("builtins.input", return_value="D")
@patch("os.system")
def test_menu_wait_drive(mock_os, mock_input, mock_print, ride):
    result = menu_display("wait", ride, [], 0.02, 0.05, "rides.csv")
    assert result == "D", "Se esperaba 'D' como opción seleccionada"

# Test para el menú de conducción con opción "S" (volver a esperar)
@patch("builtins.print")
@patch("builtins.input", return_value="S")
@patch("os.system")
def test_menu_drive_stop(mock_os, mock_input, mock_print, ride):
    result = menu_display("drive", ride, [], 0.02, 0.05, "rides.csv")
    assert result == "S", "Se esperaba 'S' como opción seleccionada"

# Test para el menú de configuración con opción "M" (volver a inicio)
@patch("builtins.print")
@patch("builtins.input", return_value="M")
@patch("os.system")
def test_menu_setup_main(mock_os, mock_input, mock_print, ride):
    result = menu_display("setup", ride, [], 0.02, 0.05, "rides.csv")
    assert result == "M", "Se esperaba 'M' como opción seleccionada"

# Test para el menú de lista de viajes (sin opciones de entrada)
@patch("builtins.print")
@patch("builtins.input", return_value="")
@patch("os.system")
def test_menu_list(mock_os, mock_input, mock_print, ride):
    menu_display("list", ride, [], 0.02, 0.05, "rides.csv")
    mock_print.assert_called()  # Verifica que imprimió datos en consola
    mock_input.assert_called_once()  # Verifica que pidió una entrada

# Test para el mensaje de entrada incorrecta
@patch("builtins.print")
@patch("os.system")
def test_menu_wrong(mock_os, mock_print, ride):
    menu_display("wrong", ride, [], 0.02, 0.05, "rides.csv")
    mock_print.assert_called()  # Verificar que imprimió el mensaje de error

# Explicación de las pruebas
# test_menu_welcome()

# Simula el menú de bienvenida y verifica que espera una entrada del usuario.
# test_menu_home_restart()

# Simula el menú de inicio, ingresando "R" y asegurando que devuelve "R".
# test_menu_wait_drive()

# Simula el menú de espera, ingresando "D" y verificando que devuelve "D".
# test_menu_drive_stop()

# Simula el menú de conducción, ingresando "S" y asegurando que devuelve "S".
# test_menu_setup_main()

# Simula el menú de configuración, ingresando "M" y verificando que devuelve "M".
# test_menu_list()

# Simula el menú de lista de viajes y verifica que imprime algo y espera una entrada.
# test_menu_wrong()

# Simula el caso en que el usuario ingresa una opción incorrecta y verifica que imprime un mensaje de error.