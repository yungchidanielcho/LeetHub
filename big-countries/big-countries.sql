# Write your MySQL query statement below
Select name, population, area from World
WHERE (area > 3 * POWER(10,6)) OR (population > 25 * POWER(10,6 )); 
