from setuptools import setup

setup(
name='pretty_printed_package',
version='0.0.1',
description='description',
url='http://github.com/name/package_name',
author='Safonov Semen',
author_email='semen.safonov@gmail.com',
license='MIT',
packages=['gt_namespace.pretty_print_mod'],
namespace_packages=['gt_namespace'],
install_requires=['get_time_package>0.0.0'],
entry_points={
'console_scripts': [
'get_time_pp=gt_namespace.pretty_print_mod:main']
}
)




