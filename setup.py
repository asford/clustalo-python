import subprocess
from distutils.core import setup, Extension

def pkgconfig(*packages, **kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    for token in subprocess.check_output(["pkg-config", "--libs", "--cflags"] + list(packages)).strip().split(" "):
        kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw

clustalo_include_dirs = ['/usr/include/clustalo', '/usr/local/include/clustalo']
clustalo_library_dirs = []

try:
    clustalo_pkg_config = pkgconfig("clustalo")

    clustalo_include_dirs.extend( clustalo_pkg_config["include_dirs"] )
    clustalo_library_dirs.extend( clustalo_pkg_config["library_dirs"] )
except subprocess.CalledProcessError:
    pass

module = Extension('clustalo',
                   sources = ['clustalo.c'],
                   include_dirs=clustalo_include_dirs,
                   library_dirs=clustalo_library_dirs,
                   libraries=['clustalo', 'stdc++', 'gomp'],
                   extra_compile_args=['-fopenmp'])


setup(name='clustalo',
      version='0.1',
      description='Python wrapper around libclustalo',
      author='Joshua Ma',
      author_email='josh@benchling.com',
      url='https://github.com/benchling/clustalo-python',
      ext_modules=[module])
