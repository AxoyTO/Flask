CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    expert BOOLEAN NOT NULL,
    admin BOOLEAN NOT NULL
);

CREATE TABLE questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    answer_text TEXT,
    asked_by_id INTEGER NOT NULL,
    expert_id INTEGER,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(asked_by_id) REFERENCES users(userid) ON DELETE CASCADE,
    FOREIGN KEY(expert_id) REFERENCES users(userid) ON DELETE CASCADE
);
