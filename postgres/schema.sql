CREATE TABLE contact_types (
	name VARCHAR(16) PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO contact_types
VALUES 	(
			'employee',
			'Contact for an employee'
		),
		(
			'customer',
			'Contact for a customer'
		);


CREATE TABLE contacts (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(32),
	last_name VARCHAR(32),
	phone_number VARCHAR(16),
	email VARCHAR(64),
	contact_type VARCHAR(16),
	FOREIGN KEY (contact_type) REFERENCES contact_types(name) ON DELETE SET NULL
);

CREATE TABLE user_groups (
	name VARCHAR(16) PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO user_groups
VALUES 	(
			'administartors',
			'Use with caution.'
		),
		(
			'standard',
			''
		);

CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username VARCHAR(24) UNIQUE,
	password VARCHAR(64) NOT NULL,
	contact_id INT,
	FOREIGN KEY (contact_id) REFERENCES contacts(id) ON DELETE SET NULL
);

CREATE TABLE ticket_types(
	name VARCHAR(16) PRIMARY KEY,
	description VARCHAR(255)
);

INSERT INTO ticket_types
VALUES 	(
			"standard",
			"Placeholder"
		);

CREATE TABLE tickets (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255),
	message_body TEXT NOT NULL,
	creation_time TIMESTAMP NOT NULL
	ticket_type VARCHAR(16),
	FOREIGN KEY (ticket_type) REFERENCES ticket_types(name) ON DELETE SET NULL
);

CREATE TABLE comment_types (
	name VARCHAR(16) PRIMARY KEY,
	description VARCHAR(255)
);

/*
	Insert some default values for comment types into the Database
*/
INSERT INTO comment_types (name, description)
VALUES	(
			'internal',
			'Comments that are not intended to be visible or seen by customers.'
		),
		(
			'standard',
			'Standard comment, perhaps visible to customer'
		);



CREATE TABLE comments (
	id SERIAL PRIMARY KEY,
	creation_time TIMESTAMP NOT NULL,
	message_body TEXT NOT NULL,
	comment_type VARCHAR(16),
	userid INT,
	ticketid INT,
	FOREIGN KEY (comment_type) REFERENCES comment_types(name) ON DELETE SET NULL,
	FOREIGN KEY (userid) REFERENCES users(id) ON DELETE SET NULL,
	FOREIGN KEY (ticketid) REFERENCES tickets(id) ON DELETE CASCADE
);