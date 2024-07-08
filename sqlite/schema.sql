CREATE TABLE users 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT UNIQUE,
    password_salt TEXT,
    password_hash TEXT,
    first_name TEXT,
    last_name TEXT,
    is_admin INT NOT NULL
);

CREATE TABLE session_tokens 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token_salt TEXT NOT NULL,
    token_hash TEXT NOT NULL,
    creation_time TEXT NOT NULL,
    expiration_time TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE tickets
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    open_date TEXT NOT NULL,
    close_date TEXT,
    issue_title TEXT NOT NULL,
    contact_id INTEGER NOT NULL,
    FOREIGN KEY(contact_id) REFERENCES contacts(id)
);

CREATE TABLE logs 
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time_stamp INTEGER NOT NULL,
    body_text TEXT NOT NULL,
    logs_type TEXT NOT NULL,
    ticket_id INTEGER NOT NULL,
    FOREIGN KEY(ticket_id) REFERENCES tickets(id)
);

CREATE TABLE contacts
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone INTEGER NOT NULL,
    contact_address TEXT NOT NULL,
    is_a_massive_piece_of_shit INTEGER
);


