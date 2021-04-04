# Write your MySQL query statement below
Select
    *
FROM
    cinema
WHERE
    (id % 2 = 1) AND ('boring' != description)
ORDER BY 
    rating DESC;