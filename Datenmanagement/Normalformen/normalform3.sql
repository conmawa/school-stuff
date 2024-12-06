SELECT lieferanten.name, lieferanten.l_id, COUNT(produkte.l_id)
FROM produkte
JOIN lieferanten 
ON lieferanten.l_id = produkte.l_id
GROUP BY produkte.l_id
ORDER BY COUNT(produkte.l_id) DESC
LIMIT 1