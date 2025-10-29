from flask import Blueprint, request, jsonify
from backendApp.extensions import db
from backendApp.models import Note

notes_bp = Blueprint("notes", __name__)


@notes_bp.route("/", methods=["GET"])
def list_notes():
    notes = Note.query.all()
    return jsonify([n.to_dict() for n in notes])


@notes_bp.route("/", methods=["POST"])
def add_note():
    data = request.get_json()
    if not data or "title" not in data or "content" not in data:
        return jsonify({"error": "Missing Input"}), 400

    note = Note(title=data["title"], content=data["content"])
    db.session.add(note)
    db.session.commit()
    return jsonify(note.to_dict()), 201


@notes_bp.route("/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = db.session.get(Note, note_id)
    if note is None:
        return jsonify({"error": "Invalid Note ID"}), 404
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note Deleted"}), 200
