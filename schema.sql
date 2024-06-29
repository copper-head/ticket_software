CREATE TABLE users 
(
    id INT PRIMARY KEY AUTOINCREMENT,
    user_name TEXT UNIQUE,
    password_salt TEXT,
    password_hash TEXT,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE session_tokens 
(
    id INT PRIMARY KEY AUTOINCREMENT,
    token_salt TEXT NOT NULL,
    token_hash TEXT NOT NULL,
    creation_time TEXT NOT NULL,
    expiration_time TEXT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE tickets
(
    id INT PRIMARY KEY AUTOINCREMENT,
    open_date INT NOT NULL,
    close_date INT,
    issue TEXT NOT NULL,
    priority_l TEXT,
    assigned TEXT,
    is_finished BOOLEAN,
    resolution TEXT,
    contact_id INT NOT NULL,
    FOREIGN KEY(contact_id) REFERENCES contacts(id)
);

CREATE TABLE logs 
(
    id INT PRIMARY KEY AUTOINCREMENT,
    time_stamp INT NOT NULL,
    body_text TEXT NOT NULL,
    logs_type TEXT NOT NULL,
    ticket_id INT NOT NULL,
    FOREIGN KEY(ticket_id) REFERENCES tickets(id)
);

CREATE TABLE contacts
(
    id INT PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone INT NOT NULL,
    contact_address TEXT NOT NULL,
    is_a_massive_piece_of_shit BOOLEAN
);


