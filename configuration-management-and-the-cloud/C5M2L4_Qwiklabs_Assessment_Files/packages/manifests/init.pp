class packages {

    package { 'python-requests':
        ensure => installed,
    }

    if $facts[os][family] == "Debian" {
        # Resource entry to install golang package
        package { 'golang':
            ensure => installed,
        }
    }

    if $facts[os][family] == "RedHat" {
        # Resource entry
        package { 'nodejs':
            ensure => installed,
        }
    }

}
