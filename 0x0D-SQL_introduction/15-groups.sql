-- List number of records with same score in table
SELECT score, COUNT(score) AS number FROM second_table AS C
GROUP BY score
ORDER BY score DESC;
