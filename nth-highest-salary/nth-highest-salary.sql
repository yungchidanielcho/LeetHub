CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      -- Get Salary where rank is N
      SELECT unique_salary
      FROM (SELECT unique_salary,
            -- Create a table of unique salary with rank. Optimize by limiting table length to N
                   RANK() OVER (ORDER BY unique_salary DESC) as `rank`
                    -- Create a table of unique salary
            FROM ( SELECT DISTINCT Salary AS unique_salary
                   FROM Employee) AS unique_salary_table
            ORDER BY unique_salary DESC
            LIMIT N) AS unique_salary_rank_table
      WHERE unique_salary_rank_table.`rank`= N
  );
END