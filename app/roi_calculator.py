def calculate_roi(area_sqft, sunlight_hours, panel_efficiency=0.18, cost_per_watt=0.8):
    watts = area_sqft * 10  # Example: 10W per sqft
    cost = watts * cost_per_watt
    annual_savings = watts * sunlight_hours * 365 * 0.001 * 0.12  # $0.12 per kWh
    payback_years = round(cost / annual_savings, 2)
    return {"cost": cost, "annual_savings": annual_savings, "payback_years": payback_years}
