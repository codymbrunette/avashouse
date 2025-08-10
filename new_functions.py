#arguements and parameters
def calculate_mpg():

    car = {
        "make":"ford",
        "model":"fiesta",
        "milage":2300,
        "fuel_consumed":460
    }

    mpg = car["milage"] / car["fuel_consumed"]
    name.title = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")
calculate_mpg()