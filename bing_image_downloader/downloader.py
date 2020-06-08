import os
import shutil

try:
    from bing import Bing
except ImportError:  # Python 3
    from .bing import Bing


def download(query, limit=100, adult_filter_off=True, force_replace=False, output_dir=None):

    engine = 'bing'
    if adult_filter_off:
        adult = 'off'
    else:
        adult = 'on'

    cwd = os.getcwd()
    image_dir = os.path.join(cwd, 'dataset', engine, query)

    if force_replace:
        if os.path.isdir(image_dir):
            shutil.rmtree(image_dir)

    os.makedirs(output_dir, exist_ok=True)
    Bing(output_dir=output_dir).bing(query, limit, adult)
