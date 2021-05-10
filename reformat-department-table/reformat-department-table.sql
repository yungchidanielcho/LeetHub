# Write your MySQL query statement below
Select id,
MAX(Case WHEN month = "Jan" THEN revenue Else Null END) As Jan_Revenue,
MAX(Case WHEN month = "Feb" THEN revenue Else Null END) As Feb_Revenue,
MAX(Case WHEN month = "Mar" THEN revenue Else Null END) As Mar_Revenue,
MAX(Case WHEN month = "Apr" THEN revenue Else Null END) As Apr_Revenue,
MAX(Case WHEN month = "May" THEN revenue Else Null END) As May_Revenue,
MAX(Case WHEN month = "Jun" THEN revenue Else Null END) As Jun_Revenue,
MAX(Case WHEN month = "Jul" THEN revenue Else Null END) As Jul_Revenue,
MAX(Case WHEN month = "Aug" THEN revenue Else Null END) As Aug_Revenue,
MAX(Case WHEN month = "Sep" THEN revenue Else Null END) As Sep_Revenue,
MAX(Case WHEN month = "Oct" THEN revenue Else Null END) As Oct_Revenue,
MAX(Case WHEN month = "Nov" THEN revenue Else Null END) As Nov_Revenue,
MAX(Case WHEN month = "Dec" THEN revenue Else Null END) As Dec_Revenue

FROM Department
GROUP BY id