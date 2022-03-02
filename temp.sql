DROP TABLE IF EXISTS TableA;
CREATE TABLE TableA (
    id INTEGER PRIMARY KEY,
    name TEXT
)
;

DROP TABLE IF EXISTS TableB;
CREATE TABLE TableB (
    id INTEGER PRIMARY KEY,
    name TEXT
)
;

INSERT INTO TableA (name) VALUES
('Ali'),
('Billie'),
('Charlie')
;

INSERT INTO TableB (name) VALUES
('Array'),
('Byte'),
('Char')
;