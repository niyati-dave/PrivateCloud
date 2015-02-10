#!/bin/bash
wget -e use_proxy=yes -e https_proxy=10.135.80.164:8678 https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
dpkg -i puppetlabs-release-trusty.deb
apt-get install puppet -y
puppet module install maestrodev-ssh_keygen

