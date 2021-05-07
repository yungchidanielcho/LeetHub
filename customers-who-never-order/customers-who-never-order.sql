# Write your MySQL query statement below
SELECT c.Name AS Customers
FROM Customers as c
Where c.ID NOT IN (SELECT CustomerId
                   FROM ORders)
