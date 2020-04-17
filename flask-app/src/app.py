from flask import Flask, Response, jsonify, request
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
  def get_data():
    return 'flask app working'



  @app.route('/namespaces', methods=['GET'])
  @cross_origin()
  def get_list_of_namespaces():
    all_namespaces = PR.get_namespaces()
    return Response(
      mimetype="application/json",
      response=all_namespaces,
      status=200
    )

  
  @app.route('/services', methods=['GET'])
  @cross_origin()
  def get_services_by_namespace():
    namespace = request.args.get('namespace')
    if namespace is None:
      services = PR.get_services()
    else:
      services = PR.get_services_by_namespace(namespace)
    return Response(
      mimetype="application/json",
      response=services,
      status=200
    )


  @app.route('/populatenamespaces', methods=['GET'])
  @cross_origin()
  def populate_namespaces():
    PR.populate_namespace()
    return Response(
      mimetype="application/json",
      response={
        "populated the namespaces",
      },
      status=200
    )


  @app.route('/populateservices', methods=['GET'])
  @cross_origin()
  def populate_service():
    PR.populate_services()
    return Response(
      mimetype="application/json",
      response={
        "populated servies"
      }
    )

  
  @app.route('/createtables', methods=['GET'])
  @cross_origin()
  def create_table():
    PR.create_table()
    return Response(
      mimetype="application/json",
      response={
        "Tables created"
      },
      status=200
    )

  return app
