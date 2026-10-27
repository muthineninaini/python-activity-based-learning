def energy_charge(units):
    slabs = [
        (100, 2.00),
        (100, 3.00),
        (100, 5.00),
        (float("inf"), 7.00)
    ]

    charge = 0
    remaining = units

    for limit, rate in slabs:
        portion = min(remaining, limit)
        charge += portion * rate
        remaining -= portion

        if remaining <= 0:
            break

    return charge


def calculate_bill(units, fixed, surcharge_rate, rebate):
    energy = energy_charge(units)
    surcharge = energy * surcharge_rate / 100
    total = max(0, energy + fixed + surcharge - rebate)

    return {
        "energy_charge": round(energy, 2),
        "fixed_charge": round(fixed, 2),
        "surcharge": round(surcharge, 2),
        "rebate": round(min(rebate, energy + fixed + surcharge), 2),
        "total_bill": round(total, 2)
    }


def compare_months(previous_bill, current_bill):
    if previous_bill <= 0:
        return None

    return round(
        (current_bill - previous_bill)
        / previous_bill * 100,
        2
    )
