import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='lxgen-provider-collection',
    version='0.1.0',
    author='Iverian',
    author_email='41ways1ucky@gmail.com',
    description='provider collection for package lxgen',
    long_description=long_description,
    url='https://github.com/Iverian/lxgen-provider-collection',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ),
    entry_points={
        'lxgen_data_provider': [
            'python=lxgen_provider_collection.python_provider:PythonProvider',
            'wolfram=lxgen_provider_collection.wolfram_provider:WolframProvider'
        ]
    }
)
