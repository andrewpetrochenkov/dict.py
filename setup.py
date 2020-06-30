import setuptools

setuptools.setup(
    name='dict',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
