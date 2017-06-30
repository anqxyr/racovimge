import setuptools

with open('README.rst') as stream:
    readme = stream.read()

setuptools.setup(
    name='racovimge',
    version='0.9',
    description='Random Cover Image Generator',
    long_description=readme,
    url='https://github.com/anqxyr/racovimge/',
    author='anqxyr',
    author_email='anqxyr@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Multimedia',
        'Topic :: Utilities'],
    packages=['racovimge'],
    package_data={'racovimge': [
        'templates/*',
        'fonts/*',
        'colors.txt']},
    scripts=['bin/racovimge'],
    install_requires=['jinja2'],
)
