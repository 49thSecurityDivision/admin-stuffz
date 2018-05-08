# 49th Security Division Lab

## Lab Trolls

### Setup

Do not use your own machine to test and create scripts for this repository, but also don't clone the repo yet (I will show you when to clone in instructions). Please use the vagrant box that is provided. Instructions for setup are below. (directory for this is vagrant file is [here](./dev_folder))

#### Requirements

packages needed for this vagrant box will be as follows, I can guarantee that the versions I list on Arch will work with everything...don't know about other distros and it would take too long to test... :D
* [Virtualbox](https://www.virtualbox.org/wiki/Downloads)(v5.2.10) (create a vmware branch if you want it...)
* [Vagrant](https://www.vagrantup.com/downloads.html) (v2.0.4) (of coarse :D )
* [ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) (v2.5.2)

#### Setup

* after you have installed everything, please create a directory called 49th wherever you want to do your dev work at. (i.e. ~/src/49th). This is important so you don't commit credentials (passwords, private keys, etc...) to the repo. 
* then create a folder called creds underneath the 49th folder. (this is where you will store all of your sensitive info (ssh keys, api tokens, etc...)). Example will be below.
* now clone this github repository in the 49th folder outside of creds directory, but inside the 49th folder.

```
src/49th
├── creds
│   ├── all.pass
│   ├── rsa-keys
│   │   ├── ctf_prov
│   │   └── ctf_prov.pub
│   └── rsa-pull
│       ├── access.json
│       └── client_secret.json
└── lab
    └── 49thlab_dev
        ├── ansible_prov
        │   ├── ansible_vagrant-manage.yml
        │   ├── pre-prov.yml
        │   ├── prov-google_api.yml
        │   └── prov.yml
        ├── bash_prov
        │   ├── prov-google_api.sh
        │   └── prov.sh
        └── Vagrantfile

```

#### other important info

I have not been maintiaining the bash scripts to work just as effectively as the ansible scripts. If you want to use the bash scripts please create another branch (since we will mainly be using ansible in the lab).

For more info checkout the 49thlab\_dev folders [README.md](49thlab_dev/README.md)

After you have completed the setup you are good to start developing. We can share all the credential information we need to through lastpass, so we don't post any plaintext creds on the repo.

## Repo Submodules and Projects

### Submodules

#### Notes
- Pull submodules:
```
git pull --recurse-submodules
```
