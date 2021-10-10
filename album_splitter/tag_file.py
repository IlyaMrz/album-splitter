import music_tag
from pathlib import Path
from typing import Dict

def tag_file(file: Path, tag_data: Dict[str, str]):
    audio = music_tag.load_file(file)
    for tag, data in tag_data.items():
        if data:
            audio[tag] = data
    audio.save()
