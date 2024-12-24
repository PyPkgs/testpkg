import setuptools


with open('VERSION', encoding='utf-8') as version_file:
    version = version_file.read().strip()

with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

with open('requirements.txt') as requirements_file:
    reqs = requirements_file.read().strip().split('\n')

setuptools.setup(
    name='testpkg',
    description='Just test packaging',
    version=version,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Haim Shulner',
    author_email='haim.shulner@gmail.com',
    include_package_data=True,
    package_data={},
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    entry_points={
    },
    python_requires='>=3.7',
    install_requires=reqs,
)