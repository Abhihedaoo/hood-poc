class NamespaceModel:
  def __init__(self, uid, name):
    self.uid = uid
    self.name = name


  def toJSON(self):
    return {
      "uid": str(self.uid),
      "name": str(self.name)
    }
