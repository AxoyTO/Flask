CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    expert BOOLEAN NOT NULL,
    admin BOOLEAN NOT NULL
);

CREATE TABLE questions(
    id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer_text TEXT,
    asked_by_id INTEGER NOT NULL,
    expert_id INTEGER,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_asker_id
        FOREIGN KEY(asked_by_id)
            REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_expert_id
        FOREIGN KEY(expert_id)
            REFERENCES users(id) ON DELETE CASCADE
);
