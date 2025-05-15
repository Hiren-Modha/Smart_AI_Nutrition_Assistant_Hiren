def summarize_calories(response_text):
    lines = response_text.strip().split('\n')
    total_calories = 0
    breakdown = []

    for line in lines:
        if '-' in line:
            parts = line.split('-')
            name = parts[0].strip()
            cal_info = parts[1].strip()
            breakdown.append(f"{name}: {cal_info}")
            try:
                cal_num = int(''.join(filter(str.isdigit, cal_info)))
                total_calories += cal_num
            except:
                pass

    return total_calories, breakdown
