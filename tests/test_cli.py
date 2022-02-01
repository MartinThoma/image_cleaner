# First party modules
from image_cleaner import cli


def test_cli(capsys):
    cli.show_metadata(["tests/example.png"])
    captured = capsys.readouterr()
    assert captured.out == "## tests/example.png\n  No metadata found.\n"
