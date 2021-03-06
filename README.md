# Ansible configuration

- [Roles](#roles)
- [Ansible Playbooks](#ansible-playbooks)

## Roles

Environment roles:

- [common](provision/roles/common/README.md)
- [haproxy](provision/roles/haproxy/README.md)
- [nginx](provision/roles/nginx/README.md)

## Ansible Playbooks

All playbooks are located in the [playbooks dir](playbooks). To run a specific playbook on a box

```
ansible-playbook playbooks/your-role.yml
```

#Deploying HAProxy with Keepalived and Nginx via Ansible

#Infrastructure

###SPECIFICATION

The setup has two Nginx servers and two HAProxy LB's
They can be deployed via `vagrant up` command.


# SETUP REQUIRMENTS

Pre-requisites
1.  Virtualbox (tested with version 6.1)
2.  Vagrant (tested with version 2.2.7)

By default ansible is using the private keys generated by vagrant for ssh auth

You can change that parameter in `group_vars/all`.

## Managment instance
Ansible 2.9.18-1.el7 version installed and is used to deploy the stack on the vgrant nodes

## Webservers role
Commons installed;
Nginx installed;

## Load balancer (HAProxy)
Haproxy installed; HAProxy is running with roundrobin algo to balance traffic between the two nginx nodes.

## Keepalived master server (HAProxy+Keepalived)
Haproxy installed;
Keepalived installed; Keepalived is running in active/passive with a VIP to failover to backup node incase the master node goes down

## Keepalived (HAProxy+Keepalived)
Haproxy installed;
Keepalived installed;

# Deploy process instruction:

Clone git project to vagrant host.

`git clone https://github.com/vishalud/browserstack-assignment.git`

#Local infrastructure opened on Vagrant VirtualBox

OS: CentOS 7

Network: 10.0.26.0/24

### Hosts

- [ansible]
    - ansible (10.0.26.10)
- [lb]
    -haproxy1 (10.0.26.201)
    -haproxy2 (10.0.26.202)
- [webapp]
    - web1 (10.0.26.101)
    - web2 (10.0.26.102)

Up/Down all virtual hosts ```vagrant up``` / ```vagrant halt```

Up/Down single host ```vagrant up web1``` / ```vagrant halt web1```

#Access to components

###Web servers
web1: http://10.0.26.201

web2: http://10.0.26.202

###Load balancer server
lb1: http://10.0.26.101
lb2: http://10.0.26.102

####HAProxy Statistic page
http://127.0.0.1:8080/stats

    username: stat
    password: statpass







