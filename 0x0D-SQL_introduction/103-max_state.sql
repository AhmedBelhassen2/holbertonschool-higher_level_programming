-- Import in hbtn_0c_0 database this table dump
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
