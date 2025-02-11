buildmatrix = [
    ##### DEBIAN 9 (stretch) [default] ######
    {
        "name": 'stable',
        "flavour": 'vagrant',
        "version": 'stable'
    },
    {
        "name": 'development',
        "flavour": 'vagrant',
        "version": 'development'
    },
    {
        "name": 'latest', #'latest' is the default docker tag
        "flavour": 'docker',
        "version": 'stable'
    },
    {
        "name": 'develop', #tag compatible with LaMachine v1
        "flavour": 'docker',
        "version": 'development'
    },
    ##### OTHER DISTRIBUTIONS ######
    {
        "name": 'stable-centos7',
        "flavour": 'vagrant',
        "version": 'stable',
        "vagrantbox": "centos/7"
    },
    {
        "name": 'stable-ubuntu1604',
        "flavour": 'vagrant',
        "version": 'stable',
        "vagrantbox": "ubuntu/xenial64"
    },
    {
        "name": 'stable-ubuntu1804',
        "flavour": 'vagrant',
        "version": 'stable',
        "vagrantbox": "ubuntu/bionic64"
    },
    {
        "name": 'development-centos7',
        "flavour": 'vagrant',
        "version": 'development',
        "vagrantbox": "centos/7"
    },
    #{
    #    "name": 'stable-fedora27',
    #    "flavour": 'vagrant',
    #    "version": 'stable',
    #    "vagrantbox": "fedora/27-cloud-base" #this image won't boot
    #},
    ##### LOCAL BUILDS ######
    {
        "name": 'stable-venv-debian9',
        "flavour": 'local',
        "version": 'stable',
        "context": "debian9",
    },
    {
        "name": 'stable-venv-centos7',
        "flavour": 'local',
        "version": 'stable',
        "context": "centos7",
    },
    {
        "name": 'stable-venv-ubuntu1604',
        "flavour": 'local',
        "version": 'stable',
        "context": "ubuntu1604",
    },
    {
        "name": 'stable-venv-ubuntu1804',
        "flavour": 'local',
        "version": 'stable',
        "context": "ubuntu1804",
    },
    {
        "name": 'stable-venv-arch',
        "flavour": 'local',
        "version": 'stable',
        "context": "arch",
    },
    ##### SPECIALISED BUILDS WITH OPTIONAL SOFTWARE ######
    {
        "name": 'piccl',
        "flavour": 'docker',
        "version": 'stable',
        "minimal": True,
        "install": "piccl"
    },
    {
        "name": 'tscan',
        "flavour": 'docker',
        "version": 'stable',
        "minimal": True,
        "install": "tscan"
    },
    {
        "name": 'fy_nl_ASR',
        "flavour": 'docker',
        "version": 'stable',
        "minimal": True,
        "install": "fy_nl_ASR"
    }
]
