# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "boxcutter/ubuntu1604"

  config.vm.network "forwarded_port", guest: 8000, host: 8000, auto_correct: true

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "vagrant/provision.yml"
  end
end
