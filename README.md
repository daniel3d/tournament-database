### ( Tournament Database ) 

## For Udacity Full Stack Web Developer Nanodegree

![terminal](http://c3.staticflickr.com/1/40/31148507730_73851b0d70_b.jpg)

#### Installation instructions

 * First make sure you have installed [Vagrant](https://www.vagrantup.com) and [Virtual Box](https://www.virtualbox.org) for help on this read this [wiki](https://www.udacity.com/wiki/ud197/install-vagrant)
 * Clone this repo `git clone https://github.com/daniel3d/tournament-database.git`
 * Make sure you are inside the folder `cd tournament-database` and start vagrant `vagrant up`
 * Once vagrant is up and running ssh to the virtual machine
 * Navigate to the project folder `cd /vagrant/tournament`
 * Run `psql -f tournament.sql` to create the database schema
 * And finally to run the test execute `python tournament_test.py`

### Stuff used to make this:

 * [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm) Use as a base to create this repo
 * [ASCII Art](http://patorjk.com) To create the nice header
 * [Pep8online](http://pep8online.com/) Check the code is compatable with PEP8 standard
 * [PEP8 Autoformat](https://packagecontrol.io/packages/Python%20PEP8%20Autoformat) To format the files in PEP8 requirements