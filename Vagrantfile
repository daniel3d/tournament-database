# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision "shell", path: "provision.sh"
  # config.vm.box = "hashicorp/precise32"
  config.vm.box = "ubuntu/trusty32"
  config.vm.network "forwarded_port", guest: 5432, host: 6432
  config.vm.network "forwarded_port", guest:   22, host: 2121
end
