![pipeline_status](https://gitlab.com/incubateur-pe/crio/badges/dev/pipeline.svg)

crio
=========

Install and configure crio

Role Variables
--------------

| Nom | valeur par defaut | description |
|-----|-------------------|-------------|
| crio_version | 1.19 | cri-o version to install |
| crio_repository_base_url | https://download.opensuse.org | repository base url |
| podman_enabled | true | Controls podman installation |
| podman_docker_enabled | true | Installs docker emulation |
| podman_docker_no_warning | false | Remove warning when running "docker" commands |
| crio_unqualified_search_registries | ["docker.io"] | Repositories to search when using unqualified search like `busybox:latest` |
| crio_registries | [] | registries, see https://www.mankier.com/5/containers-registries.conf |
| crio_mirrors | [] | mirror, see https://www.mankier.com/5/containers-registries.conf |
| crio_runroot | /var/run/containers/storage | see https://www.mankier.com/5/containers-storage.conf |
| crio_graphroot | /var/run/containers/storage | see https://www.mankier.com/5/containers-storage.conf |
| crio_storage_driver | overlay | see  https://www.mankier.com/5/containers-storage.conf |

Example Playbook
----------------

Simple crio install:

```yaml
- hosts: all
  roles:
  - role: 'crio'
```

Registry configuration example :

```yaml
- hosts: all
  tasks:
    roles:
    - role: "crio"
  vars:
    crio_registries:
      - prefix: quay.io
        insecure: true
        blocked: false
        location: local_registry:5002
      - prefix: k8s.gcr.io
        insecure: true
        location: local_registry:5001
      - prefix: docker.io
        insecure: true
        location: local_registry:5000
```

Tests
-----

See tests.md

License
-------

BSD 3-Clause
