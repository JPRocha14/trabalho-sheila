import os
from datetime import datetime

log_dir = "logs"
log_file = os.path.join(log_dir, "app.log")
os.makedirs(log_dir, exist_ok=True)

logs = [
    "2025-05-25 10:15:00,000 - INFO - Sistema iniciado com sucesso.",
    "2025-05-25 14:45:00,000 - WARNING - Conexao instavel detectada.",
    "2025-05-26 09:00:00,000 - ERROR - Falha ao carregar modulo de autenticacao.",
    "2025-05-27 11:30:00,000 - INFO - Usuário admin acessou o sistema.",
    "2025-05-27 16:00:00,000 - WARNING - Tentativa de login falhou 3 vezes."
]

with open(log_file, "a", encoding="utf-8") as f:
    for log in logs:
        f.write(log + "\n")

print("Logs pré-cadastrados adicionados com sucesso.")
