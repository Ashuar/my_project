from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.0.1',
    description='Gate pass project',
    author='Ashuar',
    author_email='ashuar@exconsol.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)

