# pip install neo4j
from neo4j import GraphDatabase

Uri = None
User = None
Password = None
Driver = None
Database = "Delivery"

def conectar(uri, user, password):
    global Uri, User, Password, Driver, Session
    try:
        Driver = GraphDatabase.driver(uri, auth=(user, password))

        with Driver.session(database="system") as sys_session:
            sys_session.run(f"CREATE DATABASE {Database} IF NOT EXISTS")


        parametros_originales = [
            {
            "nombre_zona": "Alta Vista",
            "tipo_zona": "comercial",
            "tiempo_min": 8,
            "trafico": 2,
            "capacidad": 90,
            "nombre_centro": "Centro Alta Vista",
            "status": 0
            },
            {
            "nombre_zona": "Alta Vista",
            "tipo_zona": "comercial",
            "tiempo_min": 15,
            "trafico": 1,
            "capacidad": 60,
            "nombre_centro": "Centro Castillito",
            "status": 0
            },
            {
            "nombre_zona": "Campo B",
            "tipo_zona": "rural",
            "tiempo_min": 30,
            "trafico": 0,
            "capacidad": 50,
            "nombre_centro": "Centro Puerto Ordaz",
            "status": 0
            },
            {
            "nombre_zona": "Campo Rojo",
            "tipo_zona": "rural",
            "tiempo_min": 18,
            "trafico": 0,
            "capacidad": 40,
            "nombre_centro": "Centro San Felix",
            "status": 0
            },
            {
            "nombre_zona": "Campo Rojo",
            "tipo_zona": "rural",
            "tiempo_min": 28,
            "trafico": 0,
            "capacidad": 45,
            "nombre_centro": "Centro Castillito",
            "status": 0
            },
            {
            "nombre_zona": "Castillito",
            "tipo_zona": "comercial",
            "tiempo_min": 7,
            "trafico": 2,
            "capacidad": 85,
            "nombre_centro": "Centro Castillito",
            "status": 0
            },
            {
            "nombre_zona": "Castillito",
            "tipo_zona": "comercial",
            "tiempo_min": 10,
            "trafico": 1,
            "capacidad": 70,
            "nombre_centro": "Centro Puerto Ordaz",
            "status": 0
            },
            {
            "nombre_zona": "Core 8",
            "tipo_zona": "rural",
            "tiempo_min": 25,
            "trafico": 0,
            "capacidad": 55,
            "nombre_centro": "Centro Puerto Ordaz",
            "status": 0
            },
            {
            "nombre_zona": "El Gallo",
            "tipo_zona": "comercial",
            "tiempo_min": 22,
            "trafico": 2,
            "capacidad": 80,
            "nombre_centro": "Centro San Felix",
            "status": 0
            },
            {
            "nombre_zona": "El Gallo",
            "tipo_zona": "comercial",
            "tiempo_min": 18,
            "trafico": 2,
            "capacidad": 75,
            "nombre_centro": "Centro Castillito",
            "status": 0
            },
            {
            "nombre_zona": "Francisco Avendaño",
            "tipo_zona": "residencial",
            "tiempo_min": 21,
            "trafico": 1,
            "capacidad": 60,
            "nombre_centro": "Centro Alta Vista",
            "status": 0
            },
            {
            "nombre_zona": "Las Américas",
            "tipo_zona": "residencial",
            "tiempo_min": 17,
            "trafico": 1,
            "capacidad": 65,
            "nombre_centro": "Centro Alta Vista",
            "status": 0
            },
            {
            "nombre_zona": "Los Alacranes",
            "tipo_zona": "rural",
            "tiempo_min": 40,
            "trafico": 0,
            "capacidad": 30,
            "nombre_centro": "Centro Puerto Ordaz",
            "status": 0
            },
            {
            "nombre_zona": "Los Monos",
            "tipo_zona": "rural",
            "tiempo_min": 35,
            "trafico": 0,
            "capacidad": 35,
            "nombre_centro": "Centro Puerto Ordaz",
            "status": 0
            },
            {
            "nombre_zona": "Los Olivos",
            "tipo_zona": "residencial",
            "tiempo_min": 15,
            "trafico": 1,
            "capacidad": 70,
            "nombre_centro": "Centro Alta Vista",
            "status": 0
            },
            {
            "nombre_zona": "Los Samanes",
            "tipo_zona": "residencial",
            "tiempo_min": 11,
            "trafico": 1,
            "capacidad": 60,
            "nombre_centro": "Centro Alta Vista",
            "status": 0
            },
            {
            "nombre_zona": "Puerto Ordaz",
            "tipo_zona": "comercial",
            "tiempo_min": 9,
            "trafico": 2,
            "capacidad": 95,
            "nombre_centro": "Centro Puerto Ordaz",
            "status": 0
            },
            {
            "nombre_zona": "Puerto Ordaz",
            "tipo_zona": "comercial",
            "tiempo_min": 14,
            "trafico": 2,
            "capacidad": 80,
            "nombre_centro": "Centro Alta Vista",
            "status": 0
            },
            {
            "nombre_zona": "San Felix",
            "tipo_zona": "comercial",
            "tiempo_min": 5,
            "trafico": 1,
            "capacidad": 100,
            "nombre_centro": "Centro San Felix",
            "status": 0
            },
            {
            "nombre_zona": "San Felix",
            "tipo_zona": "comercial",
            "tiempo_min": 20,
            "trafico": 2,
            "capacidad": 90,
            "nombre_centro": "Centro Castillito",
            "status": 0
            },
            {
            "nombre_zona": "San Felix",
            "tipo_zona": "comercial",
            "tiempo_min": 22,
            "trafico": 2,
            "capacidad": 85,
            "nombre_centro": "Centro Unare",
            "status": 0
            },
            {
            "nombre_zona": "UD-102",
            "tipo_zona": "residencial",
            "tiempo_min": 21,
            "trafico": 0,
            "capacidad": 70,
            "nombre_centro": "Centro San Felix",
            "status": 0
            },
            {
            "nombre_zona": "UD-102",
            "tipo_zona": "residencial",
            "tiempo_min": 14,
            "trafico": 0,
            "capacidad": 65,
            "nombre_centro": "Centro Unare",
            "status": 0
            },
            {
            "nombre_zona": "UD-104",
            "tipo_zona": "residencial",
            "tiempo_min": 19,
            "trafico": 1,
            "capacidad": 75,
            "nombre_centro": "Centro San Felix",
            "status": 0
            },
            {
            "nombre_zona": "UD-104",
            "tipo_zona": "residencial",
            "tiempo_min": 13,
            "trafico": 1,
            "capacidad": 70,
            "nombre_centro": "Centro Unare",
            "status": 0
            },
            {
            "nombre_zona": "UD-146",
            "tipo_zona": "residencial",
            "tiempo_min": 20,
            "trafico": 1,
            "capacidad": 60,
            "nombre_centro": "Centro San Felix",
            "status": 0
            },
            {
            "nombre_zona": "UD-146",
            "tipo_zona": "residencial",
            "tiempo_min": 16,
            "trafico": 1,
            "capacidad": 55,
            "nombre_centro": "Centro Unare",
            "status": 0
            },
            {
            "nombre_zona": "Unare",
            "tipo_zona": "residencial",
            "tiempo_min": 10,
            "trafico": 1,
            "capacidad": 80,
            "nombre_centro": "Centro Unare",
            "status": 0
            },
            {
            "nombre_zona": "Unare",
            "tipo_zona": "residencial",
            "tiempo_min": 12,
            "trafico": 2,
            "capacidad": 75,
            "nombre_centro": "Centro Alta Vista",
            "status": 0
            },
            {
            "nombre_zona": "Villa Brasil",
            "tipo_zona": "residencial",
            "tiempo_min": 12,
            "trafico": 1,
            "capacidad": 70,
            "nombre_centro": "Centro Unare",
            "status": 0
            },
            {
            "nombre_zona": "Vista al Sol",
            "tipo_zona": "residencial",
            "tiempo_min": 19,
            "trafico": 1,
            "capacidad": 60,
            "nombre_centro": "Centro Castillito",
            "status": 0
            }
        ]
        with Driver.session(database=Database) as session: 
            query = (
                "MERGE (z:Zona { nombre: $nombre_zona, tipo: $tipo_zona })"
                "MERGE (c:CentroDistribucion { nombre: $nombre_centro })"
                )
            for parametros in parametros_originales:
                session.run(query, parametros)

        conectar_zonas_a_centros(parametros_originales)
        conectar_zonas_a_zona(parametros_originales)

        return f"Conexión exitosa a la base de datos {Database}.", None
    
    except Exception as e:
        return None, f"Error al conectar a la base de datos: \n {e}"

def conectar_zonas_a_centros(parametros_originales):

    query = (
        "MERGE (z:Zona { nombre: $nombre_zona, tipo: $tipo_zona }) "
        "MERGE (c:CentroDistribucion { nombre: $nombre_centro }) "
        "MERGE (z)-[r1:CONECTA]->(c) "
        "ON CREATE SET r1.tiempo_minutos = $tiempo_min, r1.trafico_actual = $trafico, r1.capacidad = $capacidad, r1.status = $status "
        "MERGE (c)-[r2:CONECTA]->(z) "
        "ON CREATE SET r2.tiempo_minutos = $tiempo_min, r2.trafico_actual = $trafico, r2.capacidad = $capacidad, r2.status = $status "
    )

    parametros_filtrados = [ p for p in parametros_originales if p["nombre_zona"] in p["nombre_centro"].replace("Centro ", "")]
    with Driver.session(database=Database) as session:
        for parameter in parametros_filtrados:
            session.run(query, parameter)

def conectar_zonas_a_zona(parametros):

    zonas_principales = set(zona["nombre_zona"] for zona in parametros if (zona["nombre_zona"] in zona["nombre_centro"].replace("Centro ", "") ))

    with Driver.session(database=Database) as session:
        
        query_conecta = (
            "MATCH (z1:Zona {nombre: $nombre_zona}), (z2:Zona {nombre: $zona_principal}) "
            "MERGE (z1)-[r1:CONECTA]->(z2) "
            "ON CREATE SET r1.tiempo_minutos = $tiempo_min, r1.trafico_actual = $trafico, r1.capacidad = $capacidad, r1.status = $status "
            "MERGE (z2)-[r2:CONECTA]->(z1) "
            "ON CREATE SET r2.tiempo_minutos = $tiempo_min, r2.trafico_actual = $trafico, r2.capacidad = $capacidad, r2.status = $status "
        )
        for zona in parametros:

            nombre_centro = zona["nombre_centro"].replace("Centro ", "")

            if(zona["nombre_zona"] != nombre_centro and nombre_centro in zonas_principales):

                session.run(query_conecta, {
                    "nombre_zona": zona["nombre_zona"],
                    "zona_principal": nombre_centro,
                    "tiempo_min": zona["tiempo_min"],
                    "trafico": zona["trafico"],
                    "capacidad": zona["capacidad"],
                    "status": zona["status"]
                })

def consultar_zonas():

    with Driver.session(database=Database) as session:
        zonas = []
        tipos = []
        result = session.run("MATCH (z:Zona) RETURN z.nombre AS nombre, z.tipo as tipo ORDER BY z.nombre")
        for zona in result:
            zonas.append(zona["nombre"])
            tipos.append(zona["tipo"])
        return zonas, tipos

def consultar_centros():
    with Driver.session(database=Database) as session:
        centros = []
        result = session.run("MATCH (c:CentroDistribucion) RETURN c.nombre AS nombre  ORDER BY c.nombre")
        for centro in result:
            centros.append(centro["nombre"])
        return centros

def consultar_vias():
    with Driver.session(database=Database) as session:
        nombre_vias = []
        vias = []
        result = session.run(
            "MATCH (a)-[v:CONECTA]->(b) "
            "ORDER BY a.nombre, b.nombre "
            "RETURN a.nombre AS a_nombre, b.nombre AS b_nombre, v AS via ORDER BY a.nombre"
        )
        for via in result:
            nombre_vias.append(f"{via["a_nombre"]} - {via["b_nombre"]}")
            vias.append(via["via"]._properties) 

        return nombre_vias, vias

def consultar_relaciones(nombre_nodo):
    with Driver.session(database=Database) as session:
        relaciones = []
        result = session.run(
            "MATCH (n {nombre: $nombre_nodo})-[r:CONECTA]-(m) "
            "RETURN m.nombre AS nombre_relacionado, "
            "r.tiempo_minutos AS tiempo_min, "
            "r.status AS status, "
            "CASE WHEN startNode(r).nombre = $nombre_nodo THEN '->' ELSE '<-' END AS direccion "
            "ORDER BY n.nombre, m.nombre",
            {"nombre_nodo": nombre_nodo}
        )
        for relacion in result:
            relaciones.append({
                "nombre": relacion["nombre_relacionado"],
                "minutos": relacion["tiempo_min"],
                "direccion": relacion["direccion"],
                "status": relacion["status"]
            })

        no_relacionado = []
        result_no_rel = session.run(
            "MATCH (n) WHERE n.nombre <> $nombre_nodo AND NOT (n {nombre: $nombre_nodo})--() "
            "RETURN n.nombre AS nombre",
            {"nombre_nodo": nombre_nodo}
        )
        for nodo in result_no_rel:
            no_relacionado.append(nodo["nombre"])

        return relaciones, no_relacionado

def añadir_zona(nombre_zona, tipo_zona):
    with Driver.session(database=Database) as session:
        query = (
            "MERGE (z:Zona {nombre: $nombre_zona, tipo: $tipo_zona}) "
            "RETURN z"
        )
        result = session.run(query, {
            "nombre_zona": nombre_zona,
            "tipo_zona": tipo_zona
        })
        return result.single() is not None

def añadir_centro(nombre_centro):
    with Driver.session(database=Database) as session:
        query = (
            "MERGE (c:CentroDistribucion {nombre: $nombre_centro}) "
            "RETURN c"
        )
        result = session.run(query, {
            "nombre_centro": nombre_centro
        })
        return result.single() is not None

def añadir_via(n_origen, n_fin, tiempo, trafico, capacidad, status):
    with Driver.session(database=Database) as session:
        query = (
            "MATCH (a {nombre: $nombre_a}), (b {nombre: $nombre_b}) "
            "MERGE (a)-[r:CONECTA {tiempo_minutos: $tiempo_min, trafico_actual: $trafico, capacidad: $capacidad, status: $status}]->(b) "
            "RETURN r"
        )
        params = {
            "nombre_a": n_origen, 
            "nombre_b": n_fin,  
            "tiempo_min": int(tiempo),        
            "trafico": int(trafico),            
            "capacidad": int(capacidad),         
            "status": int(status)              
        }
        result = session.run(query, params)
        return result.single() is not None

def eliminar_zona(nombre_zona, tipo_zona):
    with Driver.session(database=Database) as session:
        query = (
            "MATCH (z:Zona {nombre: $nombre_zona, tipo: $tipo_zona}) "
            "DETACH DELETE z"
        )
        result = session.run(query, {
            "nombre_zona": nombre_zona,
            "tipo_zona": tipo_zona
        })
        return result.consume().counters.nodes_deleted > 0

def eliminar_centro(nombre_centro):
    with Driver.session(database=Database) as session:
        query = (
            "MATCH (c:CentroDistribucion {nombre: $nombre_centro}) "
            "DETACH DELETE c"
        )
        result = session.run(query, {
            "nombre_centro": nombre_centro
        })
        return result.consume().counters.nodes_deleted > 0

def eliminar_via(n_origen, n_fin, tiempo, trafico, capacidad, status):
    with Driver.session(database=Database) as session:
        query = (
            "MATCH (a)-[r:CONECTA]->(b) "
            "WHERE a.nombre = $nombre_a AND b.nombre = $nombre_b "
            "AND r.tiempo_minutos = $tiempo_min AND r.trafico_actual = $trafico "
            "AND r.capacidad = $capacidad AND r.status = $status "
            "DELETE r"
        )
        params = {
            "nombre_a": n_origen, 
            "nombre_b": n_fin,  
            "tiempo_min": int(tiempo),        
            "trafico": int(trafico),            
            "capacidad": int(capacidad),         
            "status": int(status)              
        }
        result = session.run(query, params)
        return result.consume().counters.relationships_deleted > 0

def modificar_zona(nombre_zona, tipo_zona, nuevo_nombre, nueva_zona):
    with Driver.session(database=Database) as session:
        query = (
            "MATCH (z:Zona {nombre: $nombre_zona, tipo: $tipo_zona}) "
            "SET z.nombre = $nuevo_nombre, z.tipo = $nueva_zona "
            "RETURN z"
        )
        result = session.run(query, {
            "nombre_zona": nombre_zona,
            "tipo_zona": tipo_zona,
            "nuevo_nombre": nuevo_nombre,
            "nueva_zona": nueva_zona
        })
        return result.single() is not None

def modificar_centro(nombre_centro, nuevo_nombre):
    with Driver.session(database=Database) as session:
        query = (
            "MATCH (c:CentroDistribucion {nombre: $nombre_centro}) "
            "SET c.nombre = $nuevo_nombre "
            "RETURN c"
        )
        result = session.run(query, {
            "nombre_centro": nombre_centro,
            "nuevo_nombre": nuevo_nombre
        })
        return result.single() is not None

def modificar_via(n_origen, n_fin, tiempo, trafico, capacidad, status):
    with Driver.session(database=Database) as session:
        # Eliminar relaciones existentes
        delete_query = (
            "MATCH (a)-[r:CONECTA]->(b) "
            "WHERE a.nombre = $nombre_a AND b.nombre = $nombre_b "
            "DELETE r"
        )
        session.run(delete_query, {"nombre_a": n_origen, "nombre_b": n_fin})

        # Crear la nueva relación (asegurando que los nodos existen y son únicos)
        create_query = (
            "MATCH (a {nombre: $nombre_a}), (b {nombre: $nombre_b}) "
            "CREATE (a)-[r:CONECTA { tiempo_minutos: $tiempo_min, trafico_actual: $trafico, capacidad: $capacidad, status: $status }]->(b) "
            "RETURN r"
        )
        params = {
            "nombre_a": n_origen, 
            "nombre_b": n_fin,  
            "tiempo_min": int(tiempo),        
            "trafico": int(trafico),            
            "capacidad": int(capacidad),         
            "status": int(status)              
        }
        result = session.run(create_query, params)
        return result.single() is not None

def buscar_camino(zona_origen, zona_destino):
    with Driver.session(database=Database) as session:
        query = (
            " MATCH path = allShortestPaths( (start { nombre: $zona_origen })-[:CONECTA*]->(end {nombre: $zona_destino}) ) \n" 
            "RETURN reduce(status_total = 0, r IN relationships(path) | status_total + toInteger(r.status) ) AS status_ruta, \n"
            "reduce(tiempo = 0, r IN relationships(path) | tiempo + toInteger(r.tiempo_minutos)) AS tiempo_total \n"
        )
        result = session.run(query, {"zona_origen": zona_origen, "zona_destino": zona_destino})

        record = result.single()
        if record is not None and record["tiempo_total"] is not None:
            return {
                "nodo_origen": zona_origen,
                "nodo_destino": zona_destino,
                "status_ruta": record["status_ruta"],
                "tiempo_total": record["tiempo_total"],
            }
        else:
            return None

def buscar_centro(nombre_zona_origen, centro, trafico = None, capacidad = None, status = None):
    condiciones = []

    with Driver.session(database=Database) as session:
        
        condicion = "WHERE all(r IN relationships(path) WHERE "

        if(trafico is not None):
            condiciones.append(f"toInteger(r.trafico_actual) {trafico}")
        
        if(status is not None):
            condiciones.append(f" {" AND" if (len(condiciones) > 0) else ""} toInteger(r.status) {status}")

        if(capacidad is not None):
            condiciones.append( f" {" AND" if (len(condiciones) > 0) else ""} toInteger(r.capacidad) {capacidad}" )


        for con in condiciones:
            condicion += con
        condicion += " )"

        query = (
            " MATCH path = allShortestPaths( (start:Zona { nombre: $origen })-[:CONECTA*]->(end:CentroDistribucion { nombre: $centro }) ) \n" 
                f"{condicion if (len(condiciones) > 0) else ""}\n"
            "RETURN [n IN nodes(path) | n.nombre] AS camino, \n"
            "[r IN relationships(path) | toInteger(r.status) ] AS status_calles, \n"
            "[r IN relationships(path) | toInteger(r.trafico_actual) ] AS trafico, \n"
            "[r IN relationships(path) | toInteger(r.tiempo_minutos) ] AS tiempo_min, \n"
            "reduce(tiempo = 0, r IN relationships(path) | tiempo + toInteger(r.tiempo_minutos)) AS tiempo_total \n"
        )

        print(f"---------- {nombre_zona_origen} -> {centro} ----------")
        print(query)
        print("--------------------------------------------------------------\n\n")

        result = session.run(query, {"origen": nombre_zona_origen, "centro": centro})
        records = []
        for record in result:
            camino = {
                "camino": record["camino"],
                "trafico": record["trafico"],
                "tiempo_min": record["tiempo_min"],
                "status_calles" : record["status_calles"],
                "tiempo_total": record["tiempo_total"]
                }
            records.append(camino)
            
        if(len(records) > 0):
            return records[0]
        else:
            return None

