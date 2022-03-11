from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "database": {
        "uri": os.getenv("MONGO_URI")
    }
}
