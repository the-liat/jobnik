VERSION=3.11
pyenv install "$VERSION"
pyenv local "$VERSION"
poetry init
poetry env use "$VERSION"
poetry install
