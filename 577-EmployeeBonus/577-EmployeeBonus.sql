-- Last updated: 7/14/2026, 2:17:23 PM
# Write your MySQL query statement below
select e.name,b.bonus from Employee as e left join bonus as b on e.empId = b.empId where b.bonus < 1000 or b.bonus IS Null;
