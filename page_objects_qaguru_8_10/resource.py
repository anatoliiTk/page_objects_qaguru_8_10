from pathlib import Path

def path(image):
    return str(Path(__file__).parent.joinpath(f'image/{image}'))