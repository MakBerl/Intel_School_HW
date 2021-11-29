from setuptools import setup

setup(
name='get_time_package',
version='0.0.1',
description='description',
url='http://github.com/name/package_name',
author='Safonov Semyon',
author_email='semen.safonov@gmail.com',
license='MIT',
packages=['gt_namespace.get_time_mod'],
namespace_packages=['gt_namespace'],
install_requires=[
'requests==2.26.0'
],
entry_points={
'console_scripts': [
'get_time=gt_namespace.get_time_mod:script_fun'
]
}
)




