from flask import Flask
from flask_restful import Api
from models import db
from resources import TaskList, TaskApi
import pymysql
from flasgger import Swagger


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345@localhost/tasksapi"
db.init_app(app)
api = Api(app)
swagger = Swagger(app,
      template= {
    "swagger": "3.0",
    "openapi": "3.0.0",
    "info": {
        "title": "Task",
        "version": "0.0.1",
    },
    "components": {
      "schemas": {
        "Task": {
          "properties": {
            "id": {
              "type": "integer"
            },
            "title": {
              "type": "string"
            },
            "description":{
                "type": "string"
            },
            "created_at":{
                "type": "string"
            },
            "updated_at":{
                "type": "string"
            }
          }
        }
      }
    }
  })

api.add_resource(TaskList, '/tasks')
api.add_resource(TaskApi, '/tasks/<int:task_id>')

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
