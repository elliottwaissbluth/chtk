from chtk import __version__
from chtk import compute_mel_spectrogram
from pathlib import Path


def test_version():
    assert __version__ == '0.0.2'

def test_compute_mel_spectrogram():
    song_path = Path.cwd() / 'tests' / 'song' / 'separated.ogg'
    spec = compute_mel_spectrogram(song_path)
    assert spec.shape == (512, 13918) 