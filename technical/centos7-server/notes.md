# Bugs

## [Python conflict on update](https://community.centminmod.com/threads/python-conflict-on-update.17144/)

```shell
file /usr/bin/python3.6 from install of python36-3.6.6-5.el7.x86_64 conflicts with file from package python36u-3.6.7-1.ius.centos7.x86_64
```

and hundreds lines like that

**Solution**

For CentOS 7, don't use IUS Community YUM Repo's python34u and python36u packages installed from addons/python34_install.sh and addons/python36_install.sh but instead use CentOS 7's EPEL yum repo versions of python34 and python36.

```shell
# remove ius community python34u
yum -y remove python34u python34u-devel python34u-pip python34u-setuptools python34u-tools python34u-libs python34u-tkinter
# remove ius community python36u
yum -y remove python36u python36u-devel python36u-pip python36u-setuptools python36u-tools python36u-libs python36u-tkinter
# install epel python34
yum -y install python34 python34-devel python34-pip python34-setuptools python34-tools python34-libs python34-tkinter
# install epel python36
yum -y install python36 python36-devel python36-pip python36-setuptools python36-tools python36-libs python36-tkinter
# reinstall removed dependencies from above removed ius community packages
yum -y install cmake3 cmake3-data
```

or run this script

```shell
#!/bin/bash
# fix python34/python34u and python36/python36u conflicts

if [[ "$(rpm -qa python34u)" ]]; then
  # remove ius community python34u
  yum -y remove python34u python34u-devel python34u-pip python34u-setuptools python34u-tools python34u-libs python34u-tkinter
  # install epel python34
  yum -y install python34 python34-devel python34-pip python34-setuptools python34-tools python34-libs python34-tkinter
fi
# only apply to centos 7 as centos 6 epel doesn't have python36
if [[ -f /bin/systemctl && "$(rpm -qa python36u)" ]]; then
  # remove ius community python36u
  yum -y remove python36u python36u-devel python36u-pip python36u-setuptools python36u-tools python36u-libs python36u-tkinter
  # install epel python36
  yum -y install python36 python36-devel python36-pip python36-setuptools python36-tools python36-libs python36-tkinter
fi
if [[ ! "$(rpm -qa cmake3)" ]]; then
  # reinstall removed dependencies from above removed ius community packages
  yum -y install cmake3 cmake3-data
fi
```
