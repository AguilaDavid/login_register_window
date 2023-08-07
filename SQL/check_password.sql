-- Verify password during login

SELECT id, nome
FROM client
WHERE nome = 'Ernesto Martinez'
AND password = crypt('contrasena123', password);