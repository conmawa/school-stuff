SELECT verkäufe.v_id, verkäufe.p_id, produkte.name, COUNT(verkäufe.p_id)
FROM verkäufe
JOIN produkte
ON verkäufe.p_id = produkte.p_id
GROUP BY verkäufe.p_id
ORDER BY COUNT(verkäufe.p_id) DESC