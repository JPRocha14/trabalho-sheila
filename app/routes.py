from flask import Blueprint, render_template, request
from datetime import datetime
from .logger import get_logger

main = Blueprint('main', __name__)
logger = get_logger()

@main.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        log_type = request.form.get("type")
        log_msg = request.form.get("message")
        if log_type == "info":
            logger.info(log_msg)
        elif log_type == "warning":
            logger.warning(log_msg)
        elif log_type == "error":
            logger.error(log_msg)
        message = "Log registrado com sucesso!"

    return render_template("index.html", message=message)

@main.route("/logs", methods=["GET"])
def view_logs():
    date_filter = request.args.get("date")
    logs = []
    if date_filter:
        try:
            selected_date = datetime.strptime(date_filter, "%d/%m/%Y").date()
            selected_date_str = selected_date.strftime("%Y-%m-%d")
            with open("logs/app.log", "r") as f:
                for line in f:
                    if line.startswith(selected_date_str):
                        logs.append(line.strip())
            if not logs:
                logs = ["Nenhum log encontrado para a data informada."]
        except ValueError:
            logs = ["Formato de data inválido. Use DD/MM/AAAA."]
    else:
        with open("logs/app.log", "r") as f:
            logs = [line.strip() for line in f.readlines()[-100:]]

    return render_template("index.html", logs=logs, date_filter=date_filter)
