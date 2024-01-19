# ipsec

## About

this repo looks at a setup of ipsec/openswan on an ec2 amazon linux 2023 server

From intial deployment complete to creating a tunnel between the 2 servers.

## Steps
- launch desired servers
- run `sudo ipsec_setup.sh`




## Ansible requirements
- required: `inventory.ini`

```
[pitcher]
ip_here

[catcher]
ip_here

[hosts:children]
pitcher
catcher


[pitcher:vars]
ansible_ssh_private_key_file=~/.ssh/location_of_ssh_key
ansible_ssh_user=ec2-user
ansible_host_key_checking=False

[catcher:vars]
ansible_ssh_private_key_file=~/.ssh/location_of_ssh_key
ansible_ssh_user=ec2-user
ansible_host_key_checking=False


[hosts:vars]
ansible_ssh_private_key_file=~/.ssh/location_of_ssh_key
ansible_ssh_user=ec2-user
ansible_host_key_checking=False


```

we use pitcher and catcher to describe the flow of encryption.
The pitcher throws (this would be our Eastern service) and the catcher catched the ball (this would be our western server).


Ansible allows us to gather data from our subject servers and deploy our ipsec tunnel based on the details.


## running Ansible

check servers are reachable
- `ansible hosts -m ping -i ./inventory.ini`

run ansible playbook
- `ansible-playbook main.yml  -i inventory.ini`


run a restart on the IPsec service
- `ansible-playbook restart.yml -v -i inventory.ini`


- Installing ipsec is done with `main.yml` but if you just need a restart, then use `restart.yml`
