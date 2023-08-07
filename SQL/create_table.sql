CREATE TABLE client (
	id		 SERIAL,
	nome		 VARCHAR(512) NOT NULL,
	email		 VARCHAR(512) NOT NULL,
	password		 VARCHAR(512) NOT NULL,
	registration_date DATE,
	PRIMARY KEY(id)
);

ALTER TABLE client ADD UNIQUE (nome, email);