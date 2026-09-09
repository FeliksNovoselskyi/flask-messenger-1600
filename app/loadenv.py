
import os
import dotenv

def migration():
    dotenv.load_dotenv()

    os.system(os.getenv("INIT_DB"))
    os.system(os.getenv("MIGRATE_DB"))
    os.system(os.getenv("UPGRADE_DB"))
