DROP TABLE IF EXISTS pets;

CREATE TABLE pets (
    id serial PRIMARY KEY,
    pet_name varchar (20),
    breed varchar (20)
);

INSERT INTO pets (pet_name, breed) VALUES
    ('Jocko', 'hound'),
    ('Pol', 'dachshund'),
    ('Jasmine', 'cat'),
    ('Ollie', 'cat'),
    ('Puff', 'lizard'),
    ('Annie', 'easter egger');
  