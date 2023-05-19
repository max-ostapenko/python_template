from setuptools import setup, find_packages

setup(
    name='your-module-name',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your module',
    long_description='A longer description of your module',
    url='https://github.com/your-username/your-module-repo',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='your-module-keywords',
    install_requires=[
        'dependency1>=1.0.0',
        'dependency2>=2.0.0',
    ],
    entry_points={
        'console_scripts': [
            'your-module-name=your_module_name.main:main',
        ],
    },
)
