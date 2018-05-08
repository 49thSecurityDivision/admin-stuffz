# Devlopment Env

## Dos and Donts

* Don't alter the Vagrantfile without submitting an issue so we can talk about it.
* do create other provisioner scipts per what you need for your development environment (i.e. what I used for the rsa pull project interacting with the google api script [here](./ansible_prov/prov-google_api.yml)) then add it to your local Vagrantfile and please remove before pushing/merging.
* Don't push to the master branch first, create a seperate branch (i.e. develop) and then merge with master. This will prevent any accidental overwrites.

## Tips and Tricks

If you want to make life easy on yourself checkout some of the cusomizations that I have done with ansible playbooks [here](./ansible_prov/).

A couple are the following.
* installed screen and aliased it to `screen -q ` so it doesn't give annoying message to accept. So if you use tmux, then you can use screen inside of tmux.
* aliased a command called dev, that will move you to your development that you are working on at the time.
