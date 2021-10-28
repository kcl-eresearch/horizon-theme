from setuptools import setup
setup(
    name='horizon_kcler_theme',
    description='KCL e-research Horizon Theme',
    url='https://github.com/kcl-eresearch/horizon-theme',
    license='MIT',
    author='KCL e-research',
    python_requires='>=2.7',
    packages=[
        'openstack_dashboard/themes/kcler/img/',
        'openstack_dashboard/themes/kcler/'
    ],
    package_data={'': ['*.*']},
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    zip_safe=False,
    install_requires=[],
    entry_points={}
)
