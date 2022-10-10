def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    try:
        count = 0
        for item in permanence_period:
            if item[0] <= target_time <= item[1]:
                count += 1
    except TypeError:
        return None

    return count
