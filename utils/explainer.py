def explain(test, status):
    messages = {
        "glucose": {
            "Low": "Blood sugar is below normal; this may cause weakness.",
            "Normal": "Blood sugar level is healthy.",
            "High": "Blood sugar is high; diabetes risk may exist."
        },
        "hemoglobin": {
            "Low": "Low hemoglobin can indicate anemia.",
            "Normal": "Hemoglobin level is normal.",
            "High": "High hemoglobin may need medical review."
        },
        "cholesterol": {
            "Low": "Low cholesterol is usually safe.",
            "Normal": "Cholesterol level is healthy.",
            "High": "High cholesterol increases heart disease risk."
        }
    }
    return messages[test][status]
