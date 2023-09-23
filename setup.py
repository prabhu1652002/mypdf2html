from setuptools import setup

setup(
    name='mypdf2html',
    version='0.1.0',    
    description='pdf2html',
    url='https://github.com/prabhu1652002/mypdf2html',
    author='Basav prabhu',
    author_email='basavaprabhu.g@cred.club',
    license='BSD 2-clause',
    packages=['mypdf2html'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
    ],
)