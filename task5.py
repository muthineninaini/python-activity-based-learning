Railway Fare and Reservati
# Railway Fare and Reservation Calculator

passengers = int(input("Enter number of passengers: "))

distance = float(input("Enter journey distance (km): "))
print("\nTravel Classes:")
print("1. Sleeper")
print("2. AC 3 Tier")
print("3. AC 2 Tier")
print("4. AC First Class")

class_choice = int(input("Select travel class (1-4): "))

classes = {
    1: ("Sleeper", 1.0, 20),
    2: ("AC 3 Tier", 2.0, 40),
    3: ("AC 2 Tier", 3.0, 50),
    4: ("AC First Class", 4.0, 60)
}

if class_choice not in classes:
    print("Invalid travel class.")
else:
    class_name, rate_multiplier, reservation_fee = (
        classes[class_choice]
    )

    # Illustrative distance-based base fare per km
    if distance <= 100:
        base_rate = 1.00
    elif distance <= 500:
        base_rate = 0.90
    else:
        base_rate = 0.80

    total_fare = 0
    passenger_details = []

    for i in range(1, passengers + 1):
        print(f"\nPassenger {i}")
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))

        # Illustrative age-based concessions
        if age < 5:
            concession = 1.00
        elif age < 12:
            concession = 0.50
        elif age >= 60:
            concession = 0.40
        else:
            concession = 0.00

        base_fare = distance * base_rate * rate_multiplier
        concession_amount = base_fare * concession

        fare_after_concession = base_fare - concession_amount
        passenger_fare = fare_after_concession + reservation_fee

        total_fare += passenger_fare

        passenger_details.append(
            (name, age, base_fare, concession_amount,
             reservation_fee, passenger_fare)
        )

    print("\nReservation Summary")
    print("=" * 75)
    print(f"Distance: {distance:.1f} km")
    print(f"Travel Class: {class_name}")
    print("-" * 75)

    print(f"{'Name':15}{'Age':6}{'Base':10}"
          f"{'Concession':13}{'Fee':8}{'Total':10}")

    for p in passenger_details:
        print(f"{p[0]:15}{p[1]:6}"
              f"{p[2]:10.2f}{p[3]:13.2f}"
              f"{p[4]:8.2f}{p[5]:10.2f}")

    print("-" * 75)
    print(f"Total Reservation Fare: Rs. {total_fare:.2f}")

    # Cancellation calculation
    cancel = input("\nCancel reservation? (yes/no): ").lower()

    if cancel == "yes":
        penalty_rate = float(
            input("Enter cancellation penalty percentage: ")
        )

        if 0 <= penalty_rate <= 100:
            penalty = total_fare * penalty_rate / 100
            refund = total_fare - penalty

            print("\nCancellation Statement")
            print(f"Original Fare: Rs. {total_fare:.2f}")
            print(f"Cancellation Penalty: Rs. {penalty:.2f}")
            print(f"Refund Amount: Rs. {refund:.2f}")
        else:
            print("Invalid penalty percentage.")
alculator: Calculate fares for multiple passengers using distance slabs, travel classes, age-based concessions, reservation fees, and specified cancellation penalties. 
