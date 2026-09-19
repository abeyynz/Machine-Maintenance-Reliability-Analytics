DROP TABLE IF EXISTS telemetry, errors, failures, maintenance, machines CASCADE;

CREATE TABLE machines (
    machine_id INTEGER PRIMARY KEY,
    model VARCHAR(20) NOT NULL,
    age INTEGER NOT NULL
);

CREATE TABLE maintenance (
    datetime TIMESTAMP NOT NULL,
    machine_id INTEGER NOT NULL REFERENCES machines(machine_id),
    component VARCHAR(20) NOT NULL,
    maintenance_type VARCHAR(20) NOT NULL,
    date DATE,
    month VARCHAR(7),
    year INTEGER
);

CREATE TABLE failures (
    datetime TIMESTAMP NOT NULL,
    machine_id INTEGER NOT NULL REFERENCES machines(machine_id),
    component VARCHAR(20) NOT NULL,
    date DATE,
    month VARCHAR(7),
    year INTEGER
);

CREATE TABLE errors (
    datetime TIMESTAMP NOT NULL,
    machine_id INTEGER NOT NULL REFERENCES machines(machine_id),
    error_id VARCHAR(20) NOT NULL,
    date DATE,
    month VARCHAR(7),
    year INTEGER
);

CREATE TABLE telemetry (
    datetime TIMESTAMP NOT NULL,
    machine_id INTEGER NOT NULL REFERENCES machines(machine_id),
    volt DOUBLE PRECISION,
    rotate DOUBLE PRECISION,
    pressure DOUBLE PRECISION,
    vibration DOUBLE PRECISION,
    date DATE,
    month VARCHAR(7),
    year INTEGER
);
