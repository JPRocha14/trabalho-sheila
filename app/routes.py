from flask import Blueprint, render_template, request
from datetime import datetime
from .logger import get_logger
import os

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
    start_date_str = request.args.get("start_date")
    end_date_str = request.args.get("end_date")
    logs = []

    if start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
            end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()
            current_date = datetime.now().date()

            if start_date > end_date:
                logs = ["A data inicial não pode ser posterior à data final."]
            elif end_date > current_date:
                logs = ["A data final não pode ser superior à data atual."]
            else:
                with open("logs/app.log", "r") as f:
                    for line in f:
                        try:
                            log_date = datetime.strptime(line.split(" - ")[0], "%Y-%m-%d %H:%M:%S,%f").date()
                            if start_date <= log_date <= end_date:
                                logs.append(line.strip())
                        except (ValueError, IndexError):
                            continue

                if not logs:
                    logs = ["Nenhum log encontrado para o período informado."]
        except ValueError:
            logs = ["Formato de data inválido. Use DD/MM/AAAA."]
    else:
        logs = ["Informe ambas as datas."]

    return render_template("index.html", logs=logs, start_date=start_date_str, end_date=end_date_str)
