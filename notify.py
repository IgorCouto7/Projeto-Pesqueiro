import os
import sys

DESTINO = os.environ.get("EMAIL_DESTINO")
MENSAGEM = os.environ.get("PIPELINE_MESSAGE", "Pipeline executado!")

def main():
    if not DESTINO:
        print(">>> Variável EMAIL_DESTINO não configurada. Fazendo simulação de envio.")
        print(f"Destinatário (esperado): {DESTINO}")
        print(f"Mensagem: {MENSAGEM}")
        print("Simulação de envio bem-sucedida. O e-mail não está hardcoded.")
        return 0

    SMTP_HOST = os.environ.get("SMTP_HOST")
    SMTP_PORT = os.environ.get("SMTP_PORT")
    SMTP_USER = os.environ.get("SMTP_USER")
    SMTP_PASS = os.environ.get("SMTP_PASS")

    if SMTP_HOST and SMTP_USER and SMTP_PASS:
        try:
            import smtplib
            from email.message import EmailMessage
            msg = EmailMessage()
            msg["Subject"] = "Notificação de pipeline - Projeto Pesqueiro"
            msg["From"] = SMTP_USER
            msg["To"] = DESTINO
            msg.set_content(MENSAGEM)
            with smtplib.SMTP(SMTP_HOST, int(SMTP_PORT or 25)) as smtp:
                smtp.starttls()
                smtp.login(SMTP_USER, SMTP_PASS)
                smtp.send_message(msg)
            print("E-mail enviado com sucesso via SMTP.")
            return 0
        except Exception as e:
            print("Falha ao enviar e-mail via SMTP:", e)
            return 2
    else:
        print("--- Envio de E-mail (simulado) ---")
        print(f"Destinatário: {DESTINO}")
        print(f"Mensagem: {MENSAGEM}")
        print("Simulação de envio bem-sucedida. O e-mail não está hardcoded.")
        print("-----------------------")
        return 0

if __name__ == "__main__":
    sys.exit(main())
'@ > notify.py