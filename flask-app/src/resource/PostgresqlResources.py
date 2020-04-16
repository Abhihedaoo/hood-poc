import psycopg2 
import src.resources.KubernetesResources as KR

conn = psycopg2.connect(
         database="kubernetes",
         user="postgres",
         password="postgres",
         host="127.0.0.1",
         port="5432"
       )

def popoulateNamespaces():
  namespaces = KR.getAllNamespaces()
  print(namespaces.name)
