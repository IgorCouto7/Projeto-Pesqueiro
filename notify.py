import os
import smtplib
from email.mime.text import MIMEText


def main():
    """
    Envia uma notificação por e-mail simulada ou real.
    Retorna 0 em caso de sucesso e 1 em caso de falha.
    """
    email_destino = os.getenv("EMAIL_DESTINO")
    mensagem = os.getenv("PIPELINE_MESSAGE", "Pipeline executado com sucesso!")

    # Caso não haja e-mail configurado, simula o envio
    if not email_destino:
        print(f"[SIMULAÇÃO] Mensagem enviada: '{mensagem}'")
        return 0

    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")

    msg = MIMEText(mensagem)
    msg["From"] = smtp_user or "no-reply@pesqueiro.com"
    msg["To"] = email_destino
    msg["Subject"] = "Notificação da Pipeline"

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        print(f"E-mail enviado com sucesso para {email_destino}.")
        return 0
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return 1


if __name__ == "__main__":
    exit(main())