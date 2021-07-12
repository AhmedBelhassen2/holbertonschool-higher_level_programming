-- Import in hbtn_0c_0 database this table dump
SELECT city,AVG(value) as tem FROM temperatures GROUP BY city ORDER BY tem DESC;
