def update_preferences_based_on_feedback(feedback):
    if "too many carbs" in feedback.lower():
        return "Reducing carbs in future plans..."
    return "Preferences updated."
