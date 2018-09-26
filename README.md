Запускать так

```bash
$ ./run.sh
```

Третье задание:

```sql
select 
P."InternalNumber", 
P."Position", 
T."Taxes", 
T."Month", 
E."Salary_year"/12 as Salary_month,
concat(E."Name", ' ', E."Surname") as Name_Surname

from "Employee" E JOIN "Positions" P
on P."EmployeeID" = E."ID"
JOIN "Taxes" T
on T."EmployeeID" = E."ID";
```