from distutils.core import setup, Extension
import sipdistutils

setup(
    name='ftgl',
    version='0.1',
    ext_modules=[
        Extension('FTGL', 
                  ['ftgl.sip'],
                  library_dirs=['/usr/local/lib'],
                  libraries=['ftgl']),
    ],
    include_dirs=['.', '/usr/local/include', '/usr/local/include/freetype2'],
    cmdclass = {'build_ext':sipdistutils.build_ext}
)

