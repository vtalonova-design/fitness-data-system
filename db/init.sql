CREATE TABLE IF NOT EXISTS fitness_events (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMP NOT NULL,
    steps INTEGER NOT NULL,
    heart_rate INTEGER NOT NULL,
    calories NUMERIC(5,2) NOT NULL,
    activity_type VARCHAR(50) NOT NULL
);
