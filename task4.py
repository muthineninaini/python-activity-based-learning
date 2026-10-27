
# Multi-Plan Telecommunications Cost Optimization

budget = float(input("Enter your budget (Rs.): "))
data_needed = float(input("Enter required data (GB): "))
calls_needed = int(input("Enter required calling minutes: "))
days_needed = int(input("Enter required validity (days): "))

plans = [
    {"name": "Plan A", "price": 199, "data": 2,
     "calls": 1000, "validity": 28,
     "extra_data": 20, "extra_call": 0.50},

    {"name": "Plan B", "price": 299, "data": 3,
     "calls": 1500, "validity": 56,
     "extra_data": 15, "extra_call": 0.40},

    {"name": "Plan C", "price": 399, "data": 5,
     "calls": 2000, "validity": 84,
     "extra_data": 10, "extra_call": 0.30}
]

eligible_plans = []

print("\n--- PLAN COMPARISON ---")

for plan in plans:
    excess_data = max(0, data_needed - plan["data"])
    excess_calls = max(0, calls_needed - plan["calls"])

    extra_charge = (
        excess_data * plan["extra_data"]
        + excess_calls * plan["extra_call"]
    )

    total_cost = plan["price"] + extra_charge

    eligible = (
        plan["validity"] >= days_needed
        and total_cost <= budget
    )

    print(f"\nPlan: {plan['name']}")
    print(f"Base Price: Rs. {plan['price']:.2f}")
    print(f"Excess Data: {excess_data:.2f} GB")
    print(f"Excess Calls: {excess_calls} minutes")
    print(f"Extra Charges: Rs. {extra_charge:.2f}")
    print(f"Total Cost: Rs. {total_cost:.2f}")
    print(f"Eligible: {'Yes' if eligible else 'No'}")

    if eligible:
        eligible_plans.append(
            (total_cost, plan["name"], plan["validity"])
        )

print("\n--- OPTIMAL PLAN ---")

if eligible_plans:
    best = min(eligible_plans)

    print(f"Recommended Plan: {best[1]}")
    print(f"Total Cost: Rs. {best[0]:.2f}")
    print(f"Validity: {best[2]} days")
else:
    print("No plan satisfies all constraints.")
    print("Try increasing your budget or reducing requirements.")
