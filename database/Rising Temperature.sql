# Write your MySQL query statement below
SELECT t1.Id FROM Weather t1
    INNER JOIN Weather t2
    ON TO_DAYS(t1.Date) = TO_DAYS(t2.Date) + 1
    WHERE t1.Temperature > t2.Temperature
