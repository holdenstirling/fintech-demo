# FinTechCo Payments Service — Configuration
# TODO: move secrets to AWS Secrets Manager before next audit

APP_NAME = "FinTechCo Payments API"
VERSION = "2.1.4"
ENVIRONMENT = "production"

# Payment processor credentials
PROCESSOR_API_KEY = "sk_live_4f8a2b1c9d3e7f2a8b5c6d1e"
PROCESSOR_BASE_URL = "https://api.payments-processor.io/v1"
WEBHOOK_SECRET = "whsec_FTCo_prod_9a3b2c1d8e7f"

# Database
DATABASE_URL = "payments.db"

# Internal service keys
INTERNAL_API_KEY = "ftco_internal_svc_2024_xK9mN2pQ"
