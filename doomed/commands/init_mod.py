import os
import sys
import click
import shutil
from pathlib import Path

@click.command()
@click.option('-n', '--name', required=True, help="The name of your mod.")
@click.option('-d', '--destination', required=True, help='Destination path.')
@click.option('-f', '--format', type=click.Choice(['1. GZDoom (UDMF)']),
              default='1. GZDoom (UDMF)', help='Mod format. Default is GZDoom (UDMF).')
def init_mod(name, destination, format):

  if os.path.exists(destination):
    confirm = input(f"The directory {destination} already exists. Do you want to delete it and recreate it? (Y/N):")
    if confirm.lower() != 'y':
      sys.exit(1)
    else:
      shutil.rmtree(destination, ignore_errors=True)
      os.makedirs(destination)
  else:
    os.makedirs(destination)

  # create skeleton directories
  skel = ['acs', 'colormaps', 'filter', 'flats',
          'graphics', 'hires', 'maps', 'music',
          'patches', 'sounds', 'sprites', 'textures',
          'voices', 'voxels']
  for dir in skel:
    os.makedirs(os.path.join(destination, dir))

  # initialize git repo in destination
  os.system(f'git init {destination} --quiet')

  # create .gitignore file
  gitignore_files = ["*.dbs", "*.bak", ".backup*", ".autosave*"]
  with open(os.path.join(destination, '.gitignore'), 'w') as f:
    for file in gitignore_files:
      f.write(file + '\n')
    f.close()

  # create README.md file
  with open(os.path.join(destination, 'README.md'), 'w') as f:
    f.write(f'# {name}\n\n')
    f.close()

  touch_files = ['MAPINFO.txt']
  for file in touch_files:
    Path(os.path.join(destination, file)).touch()

if __name__ == '__main__':
    init_mod()
