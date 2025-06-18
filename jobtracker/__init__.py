from flask import Flask

def create_app():
    app = Flask(__name__)
    from jobtracker.routes import jobs, users
    app.register_blueprint(jobs.bp)
    app.register_blueprint(users.bp)
    return app
