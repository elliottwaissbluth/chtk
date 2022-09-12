from msilib.schema import Error
from chtk import __version__
from chtk import compute_mel_spectrogram, SongDataset, Song
from pathlib import Path


def test_version():
    assert __version__ == '0.0.2'

# ---------------------------------------------------------------------------- #
#                                function tests                                #
# ---------------------------------------------------------------------------- #

def test_compute_mel_spectrogram():
    '''Includes tests for
        • load_song
        • simplify_notes_array
    '''
    song_path = Path.cwd() / 'chtk' / 'tests' / 'song' / 'separated.ogg'
    spec = compute_mel_spectrogram(song_path)
    assert spec.shape == (512, 13918) 

def test_SongDataset():
    '''Includes tests for
        • simplify_notes_array
            • __remove_release_keys
            • __remove_modifiers
    '''
    data_dir = Path.cwd() / 'tests' / 'data'
    dataset = SongDataset(data_dir)
    print(dataset.df.head())

def test_Song():
    song_dir = Path.cwd() / 'chtk' / 'tests' / 'data' / 'song_0'
    song = Song(song_dir)
    song.fill_notes_array()
    song.visualize(start=500)