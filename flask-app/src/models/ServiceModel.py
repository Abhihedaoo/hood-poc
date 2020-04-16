class ServiceModel:
    def __init__(self, name, namespace, port_name, port, protocol):
        self.name = name
        self.namespace = namespace
        self.port_name = port_name
        self.port = port
        self.protocol = protocol

    
    def toJSON(self):
        return {
            "name": str(self.name),
            "namespace": str(self.namespace),
            "port_name": str(self.port_name),
            "port": str(self.port),
            "protocol": str(self.protocol)
        }
 
