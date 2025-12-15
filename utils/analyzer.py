def check_ranges(values):
    ranges = {
        "glucose": (70, 140),
        "hemoglobin": (12, 16),
        "cholesterol": (125, 200)
    }

    results = {}

    for test, value in values.items():
        low, high = ranges[test]
        if value < low:
            status = "Low"
        elif value > high:
            status = "High"
        else:
            status = "Normal"

        results[test] = status

    return results
