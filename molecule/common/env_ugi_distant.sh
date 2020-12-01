CRIO_REPOSITORY_BASE_URL=http://10.0.4.40:8081/repository/download-opensuse/
REMOTE_HOST=true
PROVIDER_ARGS=['host="kvm"', 'username="libvirt-user"']
SSH_CONFIG=ssh_config_ugi
SSH_ARGS=-o ProxyCommand="ssh -W %h:%p -q -l libvirt-user kvm"
