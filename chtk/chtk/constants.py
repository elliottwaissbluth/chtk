from pathlib import Path
import pickle

if Path.cwd().stem != 'chtk':
    print(f'1: {Path.cwd()}')
    cwd = Path(__file__).parent
else:
    print(f'2: {Path.cwd()}')
    cwd = Path(__file__).parent.parent

# The following constants are useful for raw chart to notes array conversion
with open(cwd / 'resources' / 'COMBO_DICT.pkl', 'rb') as f:
    COMBO_DICT = pickle.load(f)
with open(cwd / 'resources' / 'INTERMEDIATE_NOTE_MAP.pkl', 'rb') as f:
    INTERMEDIATE_NOTE_MAP = pickle.load(f)

# VIZ_DICT maps one hot indices to their corresponding .chart representation
with open(cwd / 'resources' / 'VIZ_DICT.pkl', 'rb') as f:
    VIZ_DICT = pickle.load(f)

with open(cwd / 'resources' / 'SIMPLIFIED_NOTE_DICT.pkl', 'rb') as f:
    SIMPLIFIED_NOTE_DICT = pickle.load(f)