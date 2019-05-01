import os

EMAIL_PORT = int(os.getenv("SMTP_PORT", 465))
EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT", "smp-system@139.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "AikauAXprz1u4dNe")
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.139.com")
EMAIL_SSL = bool(int(os.getenv("EMAIL_SSL", 1)))
EMAIL_TLS = False
EMAIL_FROM = "smp-system@139.com"
