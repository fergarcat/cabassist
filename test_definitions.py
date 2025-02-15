# Pasos Clave:
# Probar total_fare() → Validar el cálculo de tarifas.
# Probar formatTime() → Asegurar que el formato de tiempo es correcto.
# Probar save_data() → Simular la escritura en un archivo con mock_open().
# Probar display_last_rides() → Simular la lectura de un CSV con mock_open() y pandas.read_csv.
import pytest
import pandas as pd
import time
from unittest.mock import patch, mock_open
from definitions import total_fare, formatTime, save_data, display_last_rides

class MockRide:
    def __init__(self):
        self.startTime = 1700000000  # Ejemplo de timestamp
        self.endTime = 1700003600  # 1 hora después
        self.driveMeter = 20
        self.waitMeter = 10
        self.Fare = 15.0

@pytest.fixture
def ride():
    return MockRide()

# Test para total_fare()
def test_total_fare(ride):
    waitfee = 0.02
    drivefee = 0.05
    fare = total_fare(ride, waitfee, drivefee)
    expected_fare = (ride.driveMeter * drivefee) + (ride.waitMeter * waitfee)
    assert fare == round(expected_fare, 2), f"Esperado {expected_fare}, obtenido {fare}"

# Test para formatTime()
def test_format_time():
    timestamp = 1700000000  # Timestamp fijo
    formatted_time = formatTime(timestamp)
    expected_time = time.strftime("%H:%M:%S", time.localtime(timestamp))
    assert formatted_time == expected_time, f"Esperado {expected_time}, obtenido {formatted_time}"

# Test para save_data() con mock_open
@patch("builtins.open", new_callable=mock_open)
@patch("os.path.exists", return_value=False)
def test_save_data(mock_exists, mock_file, ride):
    save_data(ride, "test_rides.csv")
    mock_file.assert_called_once_with("test_rides.csv", "w")  # Verificar que se abre el archivo en modo escritura

# Test para display_last_rides() con mock de pandas.read_csv
@patch("pandas.read_csv")
@patch("builtins.print")
def test_display_last_rides(mock_print, mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({
        "StartTime": ["10:00:00"],
        "EndTime": ["10:30:00"],
        "DriveMeter": [15],
        "WaitMeter": [5],
        "Fare": [10.0]
    })
    display_last_rides("test_rides.csv")
    mock_read_csv.assert_called_once_with("test_rides.csv")  # Verificar que se intentó leer el archivo
    mock_print.assert_called()  # Verificar que hubo salida en la terminal

# Explicación de las pruebas
# test_total_fare()

# Valida que total_fare() calcule correctamente la tarifa basada en driveMeter y waitMeter.
# test_format_time()

# Asegura que formatTime() convierte correctamente un timestamp en formato HH:MM:SS.
# test_save_data()

# Usa mock_open() para evitar la creación de archivos y verifica que save_data() intenta abrir el archivo.
# test_display_last_rides()

# Simula la lectura de un CSV con pandas.read_csv() y verifica que la función se ejecuta correctamente.