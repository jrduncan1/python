INSERT into users (first_name, last_name, email) VALUES ('Jake', 'Duncan', 'jake@email.com');
INSERT into users (first_name, last_name, email) VALUES ('Jordan', 'Duncan', 'jordan@email.com');
INSERT into users (first_name, last_name, email) VALUES ('Jared', 'Duncan', 'jared@email.com');

SELECT * FROM users;

SELECT * FROM users WHERE email='jake@email.com';

SELECT * FROM users WHERE id=3;

UPDATE users SET last_name='Pancakes' WHERE id=3;

DELETE from users WHERE id=2;

SELECT * FROM users
ORDER BY first_name;

SELECT * FROM users
ORDER BY first_name DESC;