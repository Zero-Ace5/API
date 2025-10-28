from flask import Flask, jsonify
from backendApp.extensions import db, migrate
from backendApp.routes.notes import notes_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("backendApp.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(notes_bp, url_prefix="/api/notes")

    @app.route("/")
    def home():
        return {"message": "API is running!"}

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not Found"}), 404

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({"error": "Bad Request"}), 400

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
