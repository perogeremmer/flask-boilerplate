from environs import Env
import base64

env = Env()
env.read_env()
debugMode = True


class Config(object):
    APP_ENV = env.str("FLASK_ENV", default="development")
    FLASK_RUN_HOST = env.str("FLASK_RUN_HOST", default="localhost")
    FLASK_RUN_PORT = env.str("FLASK_RUN_PORT", default="5000")
    APP_URL = f"http://{FLASK_RUN_HOST}:{FLASK_RUN_PORT}"
    SENTRY_DSN = env.str("SENTRY_DSN", default="xxx")

    MYSQL_DATABASE_CHARSET = 'utf8mb4'

    array_env = ["production", "staging"]
    if APP_ENV in array_env:
        debugMode = False
        SERVER_NAME = env.str("SERVER_NAME", default="localhost:5000")

    HOST = env.str("DB_HOST", default="127.0.0.1")
    DATABASE = env.str("DB_DATABASE", default="local")
    PORT = env.str("DB_PORT", default="3306")
    USERNAME = env.str("DB_USERNAME", default="homestead")
    PASSWORD = env.str("DB_PASSWORD", default="secret")

    MONGO_URI = f"mongodb://{HOST}:{PORT}/{DATABASE}"

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG = debugMode

    tls = str(env.str("MAIL_USE_TLS", default="1"))
    ssl = str(env.str("MAIL_USE_SSL", default="1"))

    MAIL_SERVER = env.str("MAIL_SERVER", default="smtp.mailtrap.io")
    MAIL_PORT = env.str("MAIL_PORT", default=2525)
    MAIL_USERNAME = env.str("MAIL_USERNAME", default="xxxx")
    MAIL_PASSWORD = env.str("MAIL_PASSWORD", default="xxxx")
    MAIL_USE_TLS = True if tls == "1" else False
    MAIL_USE_SSL = True if ssl == "1" else False

    AWS_BUCKET = env.str("AWS_BUCKET", default="myawsbucket")

    FCM_SECRET_KEY = env.str("FCM_SECRET_KEY", default="xxxx")
    SECRET_KEY = env.str("APP_SECRET", default="secret")
    JWT_SECRET_KEY = env.str("JWT_SECRET", default="jwt-secret")
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 24 hours

    SENDGRID_SECRET_KEY = env.str("SENDGRID_SECRET_KEY", default="secret")

    LOCAL_TIMEZONE = env.str('LOCAL_TIMEZONE', default='Asia/Jakarta')

    FACEBOOK_CLIENT_ID = env.str('FACEBOOK_CLIENT_ID', default='xxx')
    FACEBOOK_CLIENT_SECRET = env.str('FACEBOOK_CLIENT_SECRET', default='xxx')

    GOOGLE_CLIENT_ID = env.str('GOOGLE_CLIENT_ID', default='xxx')
    GOOGLE_CLIENT_SECRET = env.str('GOOGLE_CLIENT_SECRET', default='xxx')

    TWILIO_ACCOUNT_SID = env.str('TWILIO_ACCOUNT_SID', default='xxx')
    TWILIO_AUTH_TOKEN = env.str('TWILIO_AUTH_TOKEN', default='xxx')
    TWILIO_NUMBER = env.str('TWILIO_NUMBER', default='xxx')
