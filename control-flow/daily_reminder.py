import datetime

def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "afternoon"
    else:
        return "evening"

def get_daily_task(time_of_day):
    tasks = {
        "morning": "Start your day with a healthy breakfast and a quick review of your goals.",
        "afternoon": "Time for a productive work session or to tackle your main tasks.",
        "evening": "Wind down with a relaxing activity, like reading or a light walk."
    }
    return tasks.get(time_of_day, "No specific reminder for this time.")

if __name__ == "__main__":
    time_of_day = get_time_of_day()
    task = get_daily_task(time_of_day)
    print(f"Good {time_of_day}! Here's your reminder: {task}")