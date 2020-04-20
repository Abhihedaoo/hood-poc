import psycopg2 
import src.resource.KubernetesResources as KR
import src.models.NamespaceModel as NM
import src.models.ServiceModel as SM
import json

conn = psycopg2.connect(
         database="kubernetes",
         user="postgres",
         password="postgres",
         host="127.0.0.1",
         port="5432"
       )

cur = conn.cursor()

def populate_namespace():
  namespaces = KR.get_all_namespaces()
  for namespace in namespaces:
    print(str(namespace.name))
    sql = "INSERT INTO namespaces VALUES(%s, %s)"
    cur.execute(sql, (namespace.name, namespace.uid,))
    conn.commit()


def populate_services():
  services = KR.get_all_services()
  for service in services:
    sql = "INSERT INTO services VALUES(%s, %s, %s, %s, %s)"
    cur.execute(sql, (service.name, service.namespace, service.port_name, service.port, service.protocol,))
    conn.commit()


def get_namespaces():
  cur.execute("SELECT * FROM namespaces")
  print('The number of rows: ', cur.rowcount)
  row = cur.fetchone()
  namespaces = []
  while row is not None:
    print(row[0])
    namespaces.append(NM.NamespaceModel(str(row[1]), str(row[0])))
    row = cur.fetchone()
    
  jsonStr = json.dumps([namespace.toJSON() for namespace in namespaces])
  return jsonStr  

def get_services():
  cur.execute('SELECT * FROM services')
  row = cur.fetchone()
  services = []
  while row is not None:
    print(row)
    services.append(SM.ServiceModel(row[0], row[1], row[2], row[3], row[4]))
    row = cur.fetchone()
  
  jsonStr = json.dumps([service.toJSON() for service in services])
  return jsonStr


def get_services_by_namespace(namespace):
  sql = "SELECT * FROM services WHERE namespace = %s"
  cur.execute(sql, (namespace,))
  row = cur.fetchone()
  services = []
  while row is not None:
    print(row)
    services.append(SM.ServiceModel(row[0], row[1], row[2], row[3], row[4]))
    row = cur.fetchone()
  
  jsonStr = json.dumps([service.toJSON() for service in services])
  return jsonStr

    


def create_table():
  cur.execute('CREATE TABLE namespaces (name TEXT PRIMARY KEY NOT NULL, uid TEXT NOT NULL)')
  conn.commit()
  cur.execute('CREATE TABLE services (name TEXT PRIMARY KEY NOT NULL, namespace TEXT NOT NULL, port_name TEXT, port TEXT, protocol TEXT);')
  conn.commit()