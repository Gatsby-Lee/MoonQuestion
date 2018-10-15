from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'sqlalchemy',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
]

setup(
    name='MoonQuestion',
    version='0.1',
    install_requires=requires,
    extras_require={
        'testing': tests_require,
    },
    entry_points="""\
      [paste.app_factory]
      main = moonquestion:main
      """,
)
