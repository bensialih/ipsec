# ipsec

## About

this repo looks at a setup of ipsec/openswan on an ec2 amazon linux 2023 server

From intial deployment complete to creating a tunnel between the 2 servers.

## Steps
- launch desired servers
- run `sudo ipsec_setup.sh`




## Ansible requirements
- required: `ansible/inventory.ini`

```
[hosts]
PUBLIC_IP1__PITCHER
PUBLIC_IP2__CATCHER

[hosts:vars]
ansible_ssh_private_key_file=LOCATION_OF_KEY
ansible_ssh_user=ec2-user

```

we use pitcher and catcher to describe the flow of encryption.
The pitcher throws (this would be our Eastern service) and the catcher catched the ball (this would be our western server).


Ansible allows us to gather data from our subject servers and deploy our ipsec tunnel based on the details.


## running Ansible

check servers are reachable
- `ansible hosts -m ping -i ./ansible/inventory.ini`

run ansible playbook
- `ansible-playbook ./ansible/site.yml  -i ./ansible/inventory.ini`


