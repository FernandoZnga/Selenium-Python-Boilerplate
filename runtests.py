import os.path
import nose
from dotenv import load_dotenv


# Try to parse/load env file (if one exist)
env_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(env_path):
    load_dotenv(env_path)

nose.main()
