import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DATA_ROOT = Path(os.environ.get('AI_BABY_DATA', 'D:/AI_MEMORY'))

CONCEPTS_DIR = DATA_ROOT / 'CONCEPTS'
MODELS_DIR = DATA_ROOT / 'MODELS'
WORLDS_DIR = DATA_ROOT / 'worlds'
INDEX_FILE = DATA_ROOT / 'world_index.json'
CURRENT_WORLD_FILE = DATA_ROOT / 'current_world.txt'
TMP_DIR = DATA_ROOT / 'tmp'

PIXABAY_API_KEY = os.environ.get('PIXABAY_API_KEY', '')
FREESOUND_API_KEY = os.environ.get('FREESOUND_API_KEY', '')
PIXABAY_VIDEO_API_KEY = os.environ.get('PIXABAY_VIDEO_API_KEY', '')

TEACHER_MODEL_PATH = DATA_ROOT / 'models' / 'Qwen2.5-3B-Instruct'
