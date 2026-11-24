import math


def calculate_turf(area_sqm: float, waste_percent: float = 0.08) -> dict:
    """Calculate total turf area required including cutting waste."""
    total_sqm = round(area_sqm * (1 + waste_percent), 2)
    standard_rolls_50sqm = math.ceil(total_sqm / 50.0)
    return {
        "net_area_sqm": area_sqm,
        "waste_percent": f"{int(waste_percent * 100)}%",
        "total_required_sqm": total_sqm,
        "estimated_rolls_2x25m": standard_rolls_50sqm,
    }


def calculate_planting_density(
    area_sqm: float, spacing_cm: float, pattern: str = "square"
) -> int:
    """Calculate number of plants needed for square or triangular grid spacing."""
    spacing_m = spacing_cm / 100.0
    if pattern == "triangular":
        area_per_plant = (spacing_m**2) * 0.866
    else:
        area_per_plant = spacing_m**2
    return math.ceil(area_sqm / area_per_plant)


def calculate_daily_irrigation(
    plant_count: int, liters_per_plant_day: float, efficiency: float = 0.90
) -> float:
    """Estimate gross daily irrigation water demand in cubic meters (m3)."""
    net_liters = plant_count * liters_per_plant_day
    gross_liters = net_liters / efficiency
    return round(gross_liters / 1000.0, 3)


if __name__ == "__main__":
    print("=== Lamsat Jamal Landscape BOQ Quick Estimator ===")
    print("Turf (120 m2):", calculate_turf(120))
    print(
        "Groundcovers (50 m2 @ 30cm triangular):",
        calculate_planting_density(50, 30, "triangular"),
        "plants",
    )
    print(
        "Daily Irrigation (45 palms @ 60L/day):",
        calculate_daily_irrigation(45, 60),
        "m3/day",
    )
  
