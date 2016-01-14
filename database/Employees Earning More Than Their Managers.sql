# Write your MySQL query statement below
SELECT employer.Name
    From Employee employer JOIN Employee manager ON employer.ManagerId = manager.Id
    where employer.Salary > manager.Salary
