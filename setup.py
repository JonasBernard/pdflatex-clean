import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pdflatex-clean',
    version='1.0.1',
    author="Jonas Bernard",
    author_email="public.jbernard@web.de",
    description="A python script that creates clean LaTeX-PDFs without active contents.",
    license="GPL-3.0",
    keywords="pdf pdflatex tex latex clean active content contents selection upload cv letter career simple print ghostscript",
    py_modules=['pdflatex-clean'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/JonasBernard/pdflatex-clean",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.8',
    entry_points=dict(
        console_scripts='pdflatex-clean=pdflatex_clean:main'
    ),
    project_urls={
        'Bug Reports': 'https://github.com/JonasBernard/pdflatex-clean/issues',
        'Source': 'https://github.com/JonasBernard/pdflatex-clean',
    },
)
