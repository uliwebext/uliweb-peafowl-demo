import uliweb
from uliweb.utils.setup import setup
import apps

__doc__ = """doc"""

setup(name='uliweb-peafowl-demo',
    version=apps.__version__,
    description="Description of your project",
    package_dir = {'uliweb-peafowl-demo':'apps'},
    packages = ['uliweb-peafowl-demo'],
    include_package_data=True,
    zip_safe=False,
)
