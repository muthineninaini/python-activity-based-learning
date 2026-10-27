
# Campus Event Financial Planning

print("=== CAMPUS EVENT FINANCIAL PLANNING ===")

# Input event expenses
venue = float(input("Enter venue cost (Rs.): "))
equipment = float(input("Enter equipment cost (Rs.): "))
catering_per_person = float(
    input("Enter catering cost per participant (Rs.): ")
)
transport = float(input("Enter transport cost (Rs.): "))
certificate_per_person = float(
    input("Enter certificate cost per participant (Rs.): ")
)

# Input financial details
participants = int(input("Enter expected participants: "))
registration_fee = float(input("Enter registration fee per person: "))
sponsorship = float(input("Enter sponsorship amount (Rs.): "))

if (
    min(venue, equipment, catering_per_person, transport,
        certificate_per_person, registration_fee, sponsorship) < 0
    or participants < 0
):
    print("Error: Values cannot be negative.")

else:
    # Fixed and variable costs
    fixed_cost = venue + equipment + transport
    variable_cost_per_person = (
        catering_per_person + certificate_per_person
    )

    total_variable_cost = variable_cost_per_person * participants
    total_cost = fixed_cost + total_variable_cost

    # Participant contributions
    participant_contributions = participants * registration_fee

    # Total available funds
    total_funds = participant_contributions + sponsorship

    # Sponsorship shortfall before registrations
    sponsorship_shortfall = max(0, total_cost - sponsorship)

    # Funding position after registrations and sponsorship
    surplus_or_deficit = total_funds - total_cost

    # Minimum registrations required to break even
    required_funds = max(0, total_cost - sponsorship)
    contribution_margin = (
        registration_fee - variable_cost_per_person
    )

    print("\n" + "=" * 45)
    print("         EVENT FINANCIAL REPORT")
    print("=" * 45)

    print(f"Venue Cost:              Rs. {venue:.2f}")
    print(f"Equipment Cost:           Rs. {equipment:.2f}")
    print(f"Transport Cost:           Rs. {transport:.2f}")
    print(f"Catering Cost:            Rs. {total_variable_cost:.2f}")
    print(f"Certificate Cost:         Rs. {certificate_per_person * participants:.2f}")
    print("-" * 45)
    print(f"Total Event Cost:         Rs. {total_cost:.2f}")
    print(f"Participant Contributions: Rs. {participant_contributions:.2f}")
    print(f"Sponsorship:              Rs. {sponsorship:.2f}")
    print(f"Total Available Funds:    Rs. {total_funds:.2f}")
    print(f"Sponsorship Shortfall:    Rs. {sponsorship_shortfall:.2f}")

    if contribution_margin > 0:
        min_registrations = max(
            0,
            int(required_funds / contribution_margin)
            + (1 if required_funds % contribution_margin != 0 else 0)
        )
        print(f"Break-even Registrations: {min_registrations}")
    elif required_funds == 0:
        print("Break-even Registrations: 0")
    else:
        print("Break-even is not achievable with this registration fee.")

    print("-" * 45)

    if surplus_or_deficit > 0:
        print(f"Financial Surplus:       Rs. {surplus_or_deficit:.2f}")
    elif surplus_or_deficit < 0:
        print(f"Financial Deficit:       Rs. {-surplus_or_deficit:.2f}")
    else:
        print("Financial Status: Break-even")

    print("=" * 45)
