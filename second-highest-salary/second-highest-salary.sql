# Write your MySQL query statement below
Select Max(Salary) as SecondHighestSalary
FROM Employee
Where Salary < (Select Max(Salary)
                FROM Employee)
