## SQL answers

### 1. Escriba una Query que entregue la lista de alumnos para el curso "programación"
```sql
SELECT s.name 
FROM enrollments e
INNER JOIN courses c
ON e.course_id = c.id
INNER JOIN students s
ON e.student_id = s.id
WHERE c.name = 'programación';
```

### 2. Escriba una Query que calcule el promedio de notas de un alumno en un curso.
```sql
SELECT s.name, AVG(g.value)
FROM grades g
INNER join students s
on g.student_id = s.id
INNER JOIN tests t
ON g.test_id = t.id
INNER JOIN courses c
ON t.course_id  = c.id
WHERE c.name = 'programacion'
and s.name = 'Sergio'
GROUP by s.name;
```

### 3. Escriba una Query que entregue a los alumnos y el promedio que tiene en cada curso.
```sql
SELECT s.name, c.name, AVG(g.value)
FROM grades g
INNER join students s
on g.student_id = s.id
INNER JOIN tests t
ON g.test_id = t.id
INNER JOIN courses c
ON t.course_id  = c.id
GROUP by s.name, c.id;
```

### 4. Escriba una Query que lista a todos los alumnos con más de un curso con promedio rojo.
```sql
SELECT student, count(average) 
FROM (
	SELECT s.name AS student, AVG(g.value) AS average
	FROM grades g
	INNER join students s
	ON g.student_id = s.id
	INNER JOIN tests t
	ON g.test_id = t.id
	INNER JOIN courses c
	ON t.course_id  = c.id
	GROUP by s.name, c.id
	HAVING AVG(g.value) < 4) AS red_averages
GROUP BY red_averages.student
HAVING count(average) > 1;
```

### 5. Dejando de lado el problema del cólegio se tiene una tabla con información de jugadores de tenis: PLAYERS(Nombre, Pais, Ranking). 
Suponga que Ranking es un número de 1 a 100 que es distinto para cada jugador. Si la tabla en un momento dado tiene solo 20 registros, indique cuantos registros tiene la tabla que resulta de la siguiente consulta:
```sql
SELECT c1.Nombre, c2.Nombre
FROM PLAYERS c1, PLAYERS c2
WHERE c1.Ranking > c2.Ranking
```
Si suponemos que el ranking de esos 20 registros va de 1 a 20; podemos usar la formula para sumar los primeros n numeros naturales: n(n+1)/2 con n = 19 y obtener 190.

b) 190
