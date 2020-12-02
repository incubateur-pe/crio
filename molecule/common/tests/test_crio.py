"""Role testing files using testinfra."""


def test_crio_installed(host):
    crio = host.file("/usr/bin/crio")
    assert crio.exists
    assert crio.user == "root"
    assert crio.group == "root"
    assert crio.mode == 0o755


def test_crio_service(host):
    crio = host.service("crio")
    assert crio.is_running
    assert crio.is_enabled


def test_crio_config(host):
    config = host.file("/etc/containers/registries.conf")
    assert config.exists
    assert config.contains("10.0.4.40:5000")
    assert config.contains("insecure = true")
