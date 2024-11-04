def water_treatment_tank(Qin, Qout, retention_time):
    """
    Calculate the required tank volume and total amount of water treated in a day.

    Parameters:
    Qin (float): Average inflow rate in liters per minute.
    Qout (float): Desired outflow rate in liters per minute.
    retention_time (float): Retention time in hours.

    Returns:
    tuple: Required tank volume in cubic meters, total water treated in cubic meters per day.
    """
    t_minutes = retention_time * 60
    tank_volume_liters = Qin * t_minutes
    tank_volume_m3 = tank_volume_liters / 1000
    total_treated_liters = Qout * 24 * 60
    total_treated_m3 = total_treated_liters / 1000

    return tank_volume_m3, total_treated_m3

# Manual input from the user
try:
    Qin = float(input("Enter the average inflow rate (in liters per minute): "))
    Qout = float(input("Enter the desired outflow rate (in liters per minute): "))
    retention_time = float(input("Enter the retention time (in hours): "))
    
    tank_volume, total_treated = water_treatment_tank(Qin, Qout, retention_time)
    print(f"The required tank volume is: {round(tank_volume, 2)} cubic meters")
    print(f"The total water treated in a day is: {round(total_treated, 2)} cubic meters")
except ValueError:
    print("Please enter valid numerical values.")
