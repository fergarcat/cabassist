from ClassRide import Ride
from ClassTimer import Timer

def initialize_session():
    global currentUser, Rides, currentRide, waitfee, drivefee, waitTimer, driveTimer, filename
    currentUser = None
    Rides = []
    currentRide = Ride()
    waitfee = 0.02
    drivefee = 0.05
    waitTimer = Timer()
    driveTimer = Timer()
    filename = 'rides.csv'

# Call this function to initialize the session variables
initialize_session()