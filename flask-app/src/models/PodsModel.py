class PodsModel:
  def __init__(self, pod_ip, namespace, name):
    self.pod_ip = pod_ip
    self.namespace = namespace
    self.name = name


  def toJSON(self):
    return {
       "pod_ip": str(self.pod_ip),
       "namespace": str(self.namespace),
       "name": str(self.name)
    }
