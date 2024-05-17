import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='sistem_pemesanan_travel',
                 packages=['sistem_pemesanan_travel'],
                 install_requires=install_requires)
                