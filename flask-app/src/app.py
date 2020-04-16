from flask import Flask, Response, jsonify
from flask_cors import CORS, cross_origin
import json

import src.resource.KubernetesResources as KR
import src.resource.PostgresqlResources as PR

from .config import app_config

def create_app(env_name):
  # app initialization
  app = Flask(__name__)
  
  app.config.from_object(app_config[env_name])

  @app.route('/', methods=['GET'])
  @cross_origin()
  def getData():
    return 'flask appp working'


  @app.route('/getPods', methods=['GET'])
  @cross_origin()
  def getPods():
    allPodsList = KR.getAllPods()
    return Response(
      mimetype="application/json",
      response=allPodsList,
      status=200
    )

  @app.route('/getNamespaces', methods=['GET'])
  @cross_origin()
  def getNamespaces():
    allNamespaceList = KR.getAllNamespaces()
    return Response(
      mimetype="application/json",
      response=allNamespaceList,
      status=200
    )

  @app.route('/getServices', methods=['GET'])
  @cross_origin()
  def getServices():
    allServiceList = KR.getAllServices()
    return Response(
      mimetype="application/json",
      response=allServiceList,
      status=200
    )

  @app.route('/populateNamespaces', methods=['GET'])
  @cross_origin()
  def populateNamespaces():
    PR.populateNamespaces()
    return 'Populate'


  return app
