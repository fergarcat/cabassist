# Vamos a probar los métodos principales de la clase Ride, incluyendo start(), stop(), reset() y las propiedades iniciales.
import pytest
import time
from ClassRide import Ride

# Prueba de inicialización de Ride
def test_ride_initialization():
    ride = Ride()
    assert ride.startTime > 0, "El tiempo de inicio no debería ser cero"
    assert ride.endTime is None, "endTime debería inicializarse como None"
    assert ride.driveMeter == 0, "driveMeter debería ser 0 al inicio"
    assert ride.waitMeter == 0, "waitMeter debería ser 0 al inicio"
    assert ride.Fare == 0.00, "Fare debería ser 0.00 al inicio"
    assert ride.waitcost == 0, "waitcost debería ser 0 al inicio"
    assert ride.drivecost == 0, "drivecost debería ser 0 al inicio"

# Prueba del método start()
def test_ride_start():
    ride = Ride()
    new_time = 1700000000  # Simulamos un timestamp
    ride.start(new_time)
    assert ride.startTime == new_time, "startTime no se actualizó correctamente"

# Prueba del método stop()
def test_ride_stop():
    ride = Ride()
    new_time = 1700003600  # Simulamos un timestamp más adelante
    ride.stop(new_time)
    assert hasattr(ride, 'stopTime'), "El atributo stopTime debería existir"
    assert ride.stopTime == new_time, "stopTime no se actualizó correctamente"

# Prueba del método reset()
def test_ride_reset():
    ride = Ride()
    ride.driveMeter = 50
    ride.waitMeter = 30
    ride.Fare = 20.0
    ride.reset(0.02, 0.05)

    assert ride.driveMeter == 0, "driveMeter debería reiniciarse a 0"
    assert ride.waitMeter == 0, "waitMeter debería reiniciarse a 0"
    assert ride.Fare == 0.00, "Fare debería reiniciarse a 0.00"
    assert ride.waitcost == 0.02, "waitcost debería establecerse correctamente"
    assert ride.drivecost == 0.05, "drivecost debería establecerse correctamente"
    assert ride.startTime > 0, "startTime debería reiniciarse"

# Explicación de las pruebas
# test_ride_initialization()

# Verifica que los atributos de Ride se inicialicen correctamente.
# test_ride_start()

# Confirma que start() actualiza startTime correctamente.
# test_ride_stop()

# Verifica que stop() cree stopTime y lo actualice.
# test_ride_reset()

# Comprueba que reset() reinicia correctamente los atributos y asigna nuevas tarifas de espera y conducción.