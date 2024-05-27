from flask_restful import Resource, reqparse
from models import Task, db


class TaskList(Resource):
    def get(self):
        """
        Get all tasks
        ---
        description: Get all tasks.
        tags:
          - tasks
        responses:
          200:
            description: List of all tasks.
            content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: '#/components/schemas/Task'
                    
        """
        tasks = db.session.query(Task).all()
        task_list = [{'id': task.id, 'title': task.title, 'description': task.description, 'created_at': str(task.created_at),
                    'updated_at': str(task.updated_at)} for task in tasks]
        if task_list:
            return {'tasks': task_list}
        else:
            return {'message': "No tasks"}

    def post(self):
        """
        Create a new task
        ---
        description: Create a new task.
        tags:
          - tasks
        requestBody:
            required: true
            content:
                application/json:
                    schema:
                        type: object
                        required:
                            - title
                            - description
                        properties:
                            title:
                                type: string
                                description: The title task.
                            description:
                                type: string
                                description: The description task.
        responses:
          200:
            description: The task inserted in the database
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/Task'
        """
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        
        args = parser.parse_args()
        
        title = args['title']
        description = args['description']
                
        new_task = Task(description=description, title=title)
        db.session.add(new_task)
        db.session.commit()
        return {'message': 'Task added', 'task': {'id': new_task.id,
                                                  'title': new_task.title,
                                                  'description': new_task.description,
                                                  'created_at': str(new_task.created_at),
                                                  'updated_at': str(new_task.updated_at)}}


class TaskApi(Resource): 
       
    def get(self, task_id):
        
        """
            Get one task
            ---
            description: Get one task
            tags:
                - tasks
            parameters:
              - name: task_id
                in: path
                description: ID task
                required: true
                schema:
                    type: integer

            responses:
                200:
                    description: One task.
                    content:
                        application/json:
                            schema:
                                items:
                                    $ref: '#/components/schemas/Task'
        """
        
        task = db.session.query(Task).get(task_id)
        if task:
            return {'id': task.id, 'title': task.title,
                    'description': task.description,
                    'created_at': str(task.created_at),
                    'updated_at': str(task.updated_at)}
        else:
            return {'message': 'Task not found'}
    
    def put(self, task_id):
        
        """
            Update task
            ---
            description: Update task
            tags:
                - tasks
            parameters:
              - name: task_id
                in: path
                description: ID task
                required: true
                schema:
                    type: integer
            requestBody:
                required: true
                content:
                    application/json:
                        schema:
                            type: object
                            required:
                                - title
                                - description
                            properties:
                                title:
                                    type: string
                                    description: The title task.
                                description:
                                    type: string
                                    description: The description task.
            responses:
                200:
                    description: Update task.
                    content:
                        application/json:
                            schema:
                                items:
                                    $ref: '#/components/schemas/Task'
        """
        
        task = db.session.query(Task).get(task_id)
        if task:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True, help='Title is required')
            parser.add_argument('description', type=str, required=True, help='Description is required')
            
            args = parser.parse_args()
            
            title = args['title']
            description = args['description']
            task.description = description
            task.title = title
            db.session.commit()
            return {'message': 'Task update', 'task': {'id': task.id,
                                                       'title': task.title,
                                                       'description': task.description,
                                                       'created_at': str(task.created_at),
                                                       'updated_at': str(task.updated_at)}}
        else:
            return {"message": "Task not found"}

    def delete(self, task_id):
        
        """
            Delete task
            ---
            description: Delete task
            tags:
                - tasks
            parameters:
              - name: task_id
                in: path
                description: ID task
                required: true
                schema:
                    type: integer
            responses:
                200:
                    description: Delete task.
        """
        
        task = db.session.query(Task).get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': f"Task {task_id} deleted"}
        else:
            return {"message": "Task not found"}
