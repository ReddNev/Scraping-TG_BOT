import os
from dotenv import load_dotenv
import logging

load_dotenv()

TOKEN = os.getenv('TOKEN')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
