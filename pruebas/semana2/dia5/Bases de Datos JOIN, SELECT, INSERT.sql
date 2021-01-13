# USE "nombre_bd" >> Para utilizar cierta Base de datos
use bdprueba;

# CREATE TABLE "nombre_tabla" >> Para crear una tabla
create table t_alumno(
# solamente puede haber un campo en una tabla que sea autoincrementable
	alumno_id int auto_increment not null primary key,
    alumno_nombre varchar(35),
    alumno_fecnac date,
    alumno_email varchar(25),
    alumno_dni varchar(10)
);

# INSERT INTO >> La forma correcta de insertar datos a una tabla.
insert into t_alumno (alumno_nombre, alumno_fecnac, alumno_email, alumno_dni) value
					 ('Yomar','1984-09-12','yomarcs84@gmail.com','42731171');
insert into t_alumno (alumno_nombre, alumno_fecnac, alumno_email, alumno_dni) value
					 ('Kevin','1996-02-10','kalexcs@hotmail.com','12345678');
insert into t_alualumno_idmno (alumno_nombre, alumno_fecnac, alumno_email, alumno_dni) value
					 ('Fabian','2008-10-12','fabiancr@gmail.com','87654321');

# La forma para visualizar la informacion de uno o varios campos de una tabla
select alumno_nombre, alumno_fecnac from t_alumno;

# SELECT * FROM "nombre_tabla" >> La forma para visualizar toda la informacion de una tabla
select * from t_alumno;

# La forma de usar condicionales en bases de datos es luego de indicar las tablas usamos la clausula
select * from t_alumno where alumno_nombre = 'Yomar';
# select : seleccionar los siguientes campos
# campos | * si usamos el asterisco indica que va a devolver todos los campos de la tabla
# from: indicar desde que tabla o tablas queremos devolver
# tablas: minimo una tabla
# Adicionalmente where : nos sirve para indicar ciertas restricciones de filtro

# Crear una tabla de habilidades en la cual se guarde la descripción de la habilidad y su nivel
create table t_habilidad(
	habilidad_id int auto_increment not null primary key,
    habilidad_descripcion varchar(100),
    habilidad_nivel varchar(15),
    alumno_id int not null,
    foreign key (alumno_id) references t_alumno(alumno_id)
);

# ALTER TABLE >> modificar campos de una tabla
alter table t_alumno modify alumno_email varchar(50);

insert into t_habilidad(habilidad_descripcion, habilidad_nivel, alumno_id) values
					   ('Estudioso','alto',1),
                       ('Hiperactivo','medio',2),
                       ('Deportista','bajo',3),
                       ('Estudioso','medio',2),
                       ('Cientifico','alto',1);
                       
select * from t_habilidad;

# INNER JOIN >> devolver la interseción de ambas tablas con el atributo alumno_id
select * from t_habilidad inner join t_alumno on t_habilidad.alumno_id = t_alumno.alumno_id;

# Crear una base da datos bd empresa en el cual se tenga 2 tablas, una departamento y otra empleado
# En la tabla departamento debe ir el nom_dep, nivel; y en la tabla empleado debe ir el nombre, apellido
# y num_contrato e indicra la relacion que deben tener ambas tablas.
create database bdEmpresa;
use bdEmpresa;
create table t_departamento(
	dep_id int not null auto_increment,
    dep_nombre varchar(25),
    dep_nivel int,
    primary key(dep_id) # Otra forma de declarar primary key a un campo
);

create table t_empleado(
	empleado_id int not null auto_increment primary key,
    empleado_nombre varchar(35),
    empleado_apellido varchar(45),
    empleado_numContrado varchar(5),
    dep_id int,
    foreign key (dep_id) references t_departamento(dep_id)
    );

insert into t_departamento(dep_nombre,dep_nivel) values
                          ('Ventas',1),
                          ('Administracion',2),
                          ('Finanzas',3),
                          ('Marketing',4);
					
insert into t_empleado(empleado_nombre,empleado_apellido,empleado_numContrado,dep_id) values
                     ('Yomar','Cerdán Sulca', '0001', Null),
                     ('Fabian','Cerdán Reyes','0002',1),
                     ('Gabriel','Cerdán De La Cruz','0003',2),
                     ('Kevin','Cerdán Sulca','0004',3),
                     ('Reynaldo','Cerdán Pérez','0005',2),
                     ('Elsa','Sulca Huacausi','0006',3); 
 
# AS >> es para poner una alias a las columnas, a las tablas e inclusive a algunas funciones
select * from t_empleado as emp inner join t_departamento as dep on dep.dep_id = emp.dep_id;
 
# LEFT JOIN >> devuelve todo el universo de la izquierda y  la interseccion del universo de la derecha
select * from t_empleado as emp left join t_departamento as dep on dep.dep_id = emp.dep_id;

# RIGHT JOIN >> devuelve todo el universo de la derecha y  la interseccion del universo de la izquierda
select * from t_empleado as emp right join t_departamento as dep on dep.dep_id = emp.dep_id;

# FULL OUTER JOIN >> En MySQL no existe, pero podemos utilizar UNION
# UNION >> Devuelve una union entre el universo de la izquierda y el de la derecha(absolutamente todo)
select * from t_empleado as emp left join t_departamento as dep on dep.dep_id = emp.dep_id union   
select * from t_empleado as emp right join t_departamento as dep on dep.dep_id = emp.dep_id;

# https://dev.mysql.com/doc/refman/8.0/en/string-functions.html
# select year(alum_fecnac) from t_alumno;
# traer todos los alumnos que nacieron entre 1992 y 1994
select * from t_alumno where year(alum_fecnac) >= 1992 and year(alum_fecnac) <= 1994;