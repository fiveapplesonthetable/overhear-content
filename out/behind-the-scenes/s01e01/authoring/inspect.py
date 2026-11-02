import sys

from importlib.machinery import SourceFileLoader
scene = SourceFileLoader("scene_05", "scene-05.py").load_module()

for i, walk in enumerate(scene.WALK):
    print(f"WALK[{i}]:")
    print(walk)
