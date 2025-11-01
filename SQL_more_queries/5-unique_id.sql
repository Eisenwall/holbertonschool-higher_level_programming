-- Script that creates the table unique_id with a unique id column
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
