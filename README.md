# GlobalSettler API - Sistema de gestion de reubicacion internacional
## Descripcion: 
Esta aplicación es una API robusta diseñada para centralizar y automatizar el control financiero de procesos de reubicación internacional.

## ¿EL Por Que de este proyecto?
Permite a los usuarios gestionar sus ahorros quincenales en moneda local (COP) y visualizar su progreso en tiempo real frente a metas establecidas en divisas extranjeras (USD), facilitando la toma de decisiones presupuestarias.

## Ejemplo
Si un usuario registra un ingreso de $400,000 COP, el sistema valida el monto mediante esquemas de datos estrictos y proyecta cuánto representa esto en el presupuesto total necesario para la mudanza a EE. UU., descontando gastos operativos proyectados.

## Security by design
Dada la sensibilidad de los datos financieros gestionados, GlobalSettler API se desarrolla bajo principios de seguridad desde el diseño. Se implementan validaciones estrictas para prevenir ataques de inyección y se asegura la integridad de los datos de ahorro mediante el uso de esquemas de Pydantic y manejo de excepciones personalizadas.

## Plan de ejecucion


## Arquitectura del Proyecto

### Diagrama de Clases
![Diagrama de Clases](docs/diagrama_clases.png)

### Diagrama Entidad-Relación
![Diagrama ER](docs/diagrama_er.png)