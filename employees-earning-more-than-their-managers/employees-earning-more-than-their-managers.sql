# Write your MySQL query statement below
Select e1.Name as Employee
    FROM Employee as e1
    LEFT JOIN employee AS e2
    ON e1.ManagerID = e2.Id
    WHERE e1.Salary > e2.Salary 
;