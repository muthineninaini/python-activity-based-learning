
# Fuel Consumption and Route Comparison

distance = float(input("Enter journey distance (km): "))
budget = float(input("Enter fuel budget (Rs.): "))
reserve_percent = float(input("Enter fuel reserve percentage: "))

vehicles = [
    {"name": "Bike", "mileage": 45, "price": 105,
     "tank": 12},
    {"name": "Car", "mileage": 18, "price": 105,
     "tank": 45},
    {"name": "SUV", "mileage": 12, "price": 105,
     "tank": 60}
]

if distance <= 0 or budget < 0 or not 0 <= reserve_percent <= 100:
    print("Invalid distance, budget, or reserve percentage.")
else:
    feasible_vehicles = []

    print("\n========== VEHICLE COMPARISON ==========")

    for vehicle in vehicles:
        mileage = vehicle["mileage"]
        fuel_price = vehicle["price"]
        tank_capacity = vehicle["tank"]

        # Fuel required for the journey
        journey_fuel = distance / mileage

        # Additional fuel kept as reserve
        reserve_fuel = journey_fuel * reserve_percent / 100

        total_fuel = journey_fuel + reserve_fuel
        journey_cost = journey_fuel * fuel_price
        total_cost_with_reserve = total_fuel * fuel_price

        # Feasibility checks
        tank_ok = total_fuel <= tank_capacity
        budget_ok = total_cost_with_reserve <= budget
        feasible = tank_ok and budget_ok

        print(f"\nVehicle: {vehicle['name']}")
        print(f"Distance: {distance:.2f} km")
        print(f"Mileage: {mileage} km/litre")
        print(f"Journey Fuel: {journey_fuel:.2f} litres")
        print(f"Reserve Fuel: {reserve_fuel:.2f} litres")
        print(f"Total Fuel Needed: {total_fuel:.2f} litres")
        print(f"Journey Fuel Cost: Rs. {journey_cost:.2f}")
        print(f"Cost Including Reserve: Rs. {total_cost_with_reserve:.2f}")
        print(f"Tank Capacity: {tank_capacity} litres")
        print(f"Feasible: {'Yes' if feasible else 'No'}")

        if feasible:
            feasible_vehicles.append(
                (total_cost_with_reserve, vehicle["name"],
                 total_fuel, journey_cost)
            )

    print("\n========== BEST OPTION ==========")

    if feasible_vehicles:
        best = min(feasible_vehicles)

        print(f"Lowest-Cost Vehicle: {best[1]}")
        print(f"Fuel Required Including Reserve: {best[2]:.2f} litres")
        print(f"Journey Fuel Cost: Rs. {best[3]:.2f}")
        print(f"Cost Including Reserve: Rs. {best[0]:.2f}")
    else:
        print("No vehicle meets both budget and tank requirements.")

    print("=================================")
