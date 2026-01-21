import time
import random
import psycopg2
from datetime import datetime

DB_CONFIG = {
    "host": "postgres",
    "database": "fitness",
    "user": "fitness_user",
    "password": "fitness_password"
}

ACTIVITIES = {
    "rest": {
        "steps": (0, 2),
        "heart_rate": (55, 75),
        "calories": (0.5, 1.5)
    },
    "walk": {
        "steps": (5, 15),
        "heart_rate": (80, 110),
        "calories": (2, 5)
    },
    "run": {
        "steps": (15, 30),
        "heart_rate": (120, 160),
        "calories": (6, 12)
    }
}

def generate_event():
    activity = random.choice(list(ACTIVITIES.keys()))
    data = ACTIVITIES[activity]

    return (
        datetime.utcnow(),
        random.randint(*data["steps"]),
        random.randint(*data["heart_rate"]),
        round(random.uniform(*data["calories"]), 2),
        activity
    )

def main():
    time.sleep(5)  # ждём, пока БД поднимется

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    while True:
        event = generate_event()
        cursor.execute(
            """
            INSERT INTO fitness_events
            (event_time, steps, heart_rate, calories, activity_type)
            VALUES (%s, %s, %s, %s, %s)
            """,
            event
        )
        conn.commit()
        print("Inserted:", event)
        time.sleep(1)

if __name__ == "__main__":
    main()
