import sys
sys.path.insert(0, '/src')

from src.app import create_app


if __name__ == '__main__':
  env_name= 'developement'
  app = create_app(env_name)
  #run app
  app.run()
