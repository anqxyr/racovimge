import setuptools

setuptools.setup(
    name='racovimge',
    version='0.2',
    description='Random Cover Image Generator',
    long_description='',
    url='https://github.com/anqxyr/racovimge/',
    author='anqxyr',
    author_email='anqxyr@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'],
    packages=['racovimge'],
    package_data={'racovimge': ['templates/*']},
    scripts=['bin/racovimge'],
    install_requires=['jinja2'],
)
