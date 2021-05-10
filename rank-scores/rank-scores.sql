# Write your MySQL query statement below
Select Scores.Score,
unique_value_rank.no_gap_rank as `Rank`

FROM Scores
-- join unique score with rank to origional score table
LEFT JOIN (
           -- Create a table of unique score and a column of row numbers
           SELECT unique_value,
           ROW_NUMBER() OVER(ORDER BY unique_value DESC) AS no_gap_rank
           -- Create a table of unique value of score
           FROM (
                 SELECT DISTINCT Score AS unique_value
                 FROM Scores) AS unique_value_table
          ) as unique_value_rank
          
ON Scores.Score = unique_value_rank.unique_value
ORDER BY Score DESC
