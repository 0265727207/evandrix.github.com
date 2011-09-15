from distutils.core import setup, Extension
                           
setup(  name = "yara-python",
        version = "1.6",
        author = "Victor M. Alvarez",
        author_email = "victor.alvarez@virustotal.com",
        url = 'http://yara-project.googlecode.com',
        platforms = ['any'],
        ext_modules = [ Extension(
                            name='yara', 
                            sources=['yara-python.c'],
                            libraries=['yara','pcre'],
                            include_dirs=['/usr/local/include'],
                            extra_compile_args=['-m64'],
                            extra_link_args=['-m64'],
                        )])
