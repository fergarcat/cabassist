
# Primero debemos identificar las funciones clave que requieren pruebas. Algunas funciones candidatas son:

# total_fare(currentRide, waitfee, drivefee): Si existe en otro módulo, podemos importarla y probar su cálculo.

# Ride y Timer: Necesitamos importar las clases y probar su funcionalidad.

import pytest
from cabAssist import total_fare, Ride, Timer

@pytest.fixture
def ride():
    return Ride()

def test_total_fare(ride):
    waitfee = 0.02
    drivefee = 0.05
    ride.waitMeter = 10  # Simulando 10 minutos de espera
    ride.driveMeter = 20  # Simulando 20 minutos de conducción
    fare = total_fare(ride, waitfee, drivefee)
    expected_fare = (10 * waitfee) + (20 * drivefee)
    assert fare == expected_fare, f"Se esperaba {expected_fare}, pero se obtuvo {fare}"

def test_timer():
    timer = Timer()
    timer.restart()
    assert timer.get_time() >= 0, "El tiempo debe ser mayor o igual a cero"

def test_ride_reset(ride):
    ride.reset(0.02, 0.05)
    assert ride.waitMeter == 0
    assert ride.driveMeter == 0
    assert ride.Fare == 0

