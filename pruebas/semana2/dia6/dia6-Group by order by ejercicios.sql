use playa_estacionamiento;
# select * from t_registro;
# toda funcion de sql tiene que ir ligada con la clausula GROUP BY
select count(veh_id) as "conteo vehiculo playa", veh_id, playa_id from t_registro 
						group by playa_id, veh_id 
                        order by 3 desc;
# la clausula group by sirve para hacer un ordenamiento del resultado del select,
# no es obligatorio que tenga un group by, y luego va o el nombre de la columna
# o su posicion (comenzando en 1) y adicionalmente se puede poner la palabra asc=ascendente
# o desc = descendente

#-------------------------------------------------------------------------------------------

# MUESTRE TODOS LOS VEHICULOS INGRESADOS EN LA PLAYA CON ID 1 Y QUE ME DIGA SU 
# NOMBRE PLAYA     PLACA     FECHA INGRESO    FECHA SALIDA
select playa_nomb as Playa,
       veh_placa as Placa,       
	   reg_fechin as "Fecha ingreso",  
       reg_fechfin as "Fecha salida" 
from t_registro as reg 
       inner join t_playa as playa on reg.playa_id = playa.playa_id
	   inner join t_vehiculo as veh on reg.veh_id = veh.veh_id
where playa.playa_id = 1;

#------------------------------------------------------------------------------------------------

# INDIQUE TODOS LOS VEHICULOS INGRESADOS ENTRE EL 02 Y 05 DE NOVIEMBRE CON SUS MONTOS RESPECTIVOS
# PLACA   MARCA   FECHA INGRESO   FECHA SALIDA   MONTO
select veh_placa as Placa,
	   veh_marca as Marca,
	   reg_fechin as "Fecha ingreso", 
       reg_fechfin as "Fecha salida" ,
       reg_monto as Monto
from t_registro as reg 
	   inner join t_vehiculo as veh on reg.veh_id = veh.veh_id
where reg_fechfin <= '2020-11-05 23:59:59' and reg_fechin >= '2020-11-02 00:00:00';
 
#----------------------------------------------------------------------------------------------------

# MUESTRE LA LISTA DE VEHICULOS CON SUS # DE VECES QUE TUVIESEN REGISTROS EN CUALQUIERA DE LAS PLAYAS 
# EN ORDEN DE MAYOR A MENOR VECES
# HINT: COUNT() 
# PLACA   MARCA   MODELO   # VECES
select * from t_registro;
select veh_placa as Placa, 
       veh_marca as Marca, 
       veh_modelo as Modelo,
       veh.veh_id as Id,
       count(veh.veh_id) as "# VECES"
from t_registro as puente 
       inner join t_vehiculo as veh on puente.veh_id = veh.veh_id
group by veh_placa
order by 5 desc;





