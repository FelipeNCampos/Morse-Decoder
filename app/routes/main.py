from flask import render_template, request

from app.routes import main_bp
from app.services.morse import morse_to_text, text_to_morse


@main_bp.route("/", methods=["GET", "POST"])
def index():
    texto = ""
    morse = ""
    error = None

    if request.method == "POST":
        operation = request.form.get("operation")

        try:
            if operation == "encode":
                texto = request.form.get("texto", "")
                morse = text_to_morse(texto)
            elif operation == "decode":
                morse = request.form.get("morse", "")
                texto = morse_to_text(morse)
        except ValueError as exception:
            error = str(exception)

    return render_template("index.html", texto=texto, morse=morse, error=error)
