from kubernetes import client, config
import src.models.PodsModel as PM
import src.models.NamespaceModel as NM
import src.models.ServiceModel as SM
from flask import json


config.load_incluster_config()

v1 = client.CoreV1Api()

# def getAllPods():
#   print("Listing pods with their IPs:")
#   ret = v1.list_pod_for_all_namespaces(watch=False)
#   pods = []
#   for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
#     pods.append(PM.PodsModel(i.status.pod_ip, i.metadata.namespace, i.metadata.name))
  
#   jsonStr = json.dumps([pod.toJSON() for pod in pods])
#   return jsonStr

def get_all_namespaces():
  response = v1.list_namespace()
  namespaces = []
  for i in response.items:
    print("%s\t%s" % (i.metadata.uid, i.metadata.name))
    namespaces.append(NM.NamespaceModel(i.metadata.uid, i.metadata.name))

  # jsonStr = json.dumps([namespace.toJSON() for namespace in namespaces])
  return namespaces


def get_all_services():
  response = v1.list_service_for_all_namespaces(watch=False)
  services = []
  for i in response.items:
    print("%s\t%s\t%s\t%s\t%s" % (i.metadata.name, i.metadata.namespace, i.spec.ports[0].name, i.spec.ports[0].port, i.spec.ports[0].protocol))
    services.append(SM.ServiceModel(i.metadata.name, i.metadata.namespace, i.spec.ports[0].name, i.spec.ports[0].port, i.spec.ports[0].protocol))

  # jsonStr = json.dumps([service.toJSON() for service in services])
  return services
