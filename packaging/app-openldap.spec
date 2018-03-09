
Name: app-openldap
Epoch: 1
Version: 2.4.1
Release: 1%{dist}
Summary: OpenLDAP Driver - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-openldap-%{version}.tar.gz
Buildarch: noarch

%description
The OpenLDAP Driver app provides the the necessary tools for users, groups, accounts and other directory services.

%package core
Summary: OpenLDAP Driver - Core
Provides: system-ldap-driver
Requires: app-base-core
Requires: app-certificate-manager-core >= 1:2.4.20
Requires: app-ldap-core >= 1:1.6.1
Requires: app-mode-core
Requires: app-network-core
Requires: openldap-servers >= 2.4.44
Requires: openldap-clients >= 2.4.44
Requires: openssl

%description core
The OpenLDAP Driver app provides the the necessary tools for users, groups, accounts and other directory services.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/openldap
cp -r * %{buildroot}/usr/clearos/apps/openldap/

install -d -m 0755 %{buildroot}/etc/openldap/cacerts
install -d -m 0755 %{buildroot}/var/clearos/events/openldap_configuration
install -d -m 0755 %{buildroot}/var/clearos/events/openldap_online
install -d -m 0755 %{buildroot}/var/clearos/openldap
install -d -m 0755 %{buildroot}/var/clearos/openldap/backup
install -d -m 0775 %{buildroot}/var/clearos/openldap/lock
install -d -m 0755 %{buildroot}/var/clearos/openldap/provision
install -D -m 0755 packaging/certificate-manager-event %{buildroot}/var/clearos/events/certificate_manager/openldap
install -D -m 0644 packaging/filewatch-openldap-configuration-event.conf %{buildroot}/etc/clearsync.d/filewatch-openldap-configuration-event.conf
install -D -m 0644 packaging/filewatch-openldap-online-event.conf %{buildroot}/etc/clearsync.d/filewatch-openldap-online-event.conf
install -D -m 0755 packaging/ldap-import %{buildroot}/usr/sbin/ldap-import
install -D -m 0755 packaging/network-configuration-event %{buildroot}/var/clearos/events/network_configuration/openldap
install -D -m 0644 packaging/schema/RADIUS-LDAPv3.schema %{buildroot}/etc/openldap/schema/RADIUS-LDAPv3.schema
install -D -m 0644 packaging/schema/clearcenter.schema %{buildroot}/etc/openldap/schema/clearcenter.schema
install -D -m 0644 packaging/schema/clearfoundation.schema %{buildroot}/etc/openldap/schema/clearfoundation.schema
install -D -m 0644 packaging/schema/horde.schema %{buildroot}/etc/openldap/schema/horde.schema
install -D -m 0644 packaging/schema/kolab2.schema %{buildroot}/etc/openldap/schema/kolab2.schema
install -D -m 0644 packaging/schema/kopano.schema %{buildroot}/etc/openldap/schema/kopano.schema
install -D -m 0644 packaging/schema/owncloud.schema %{buildroot}/etc/openldap/schema/owncloud.schema
install -D -m 0644 packaging/schema/pcn.schema %{buildroot}/etc/openldap/schema/pcn.schema
install -D -m 0644 packaging/schema/rfc2307bis.schema %{buildroot}/etc/openldap/schema/rfc2307bis.schema
install -D -m 0644 packaging/schema/rfc2739.schema %{buildroot}/etc/openldap/schema/rfc2739.schema
install -D -m 0644 packaging/schema/samba.schema %{buildroot}/etc/openldap/schema/samba3.schema
install -D -m 0644 packaging/schema/zarafa.schema %{buildroot}/etc/openldap/schema/zarafa.schema
install -D -m 0644 packaging/slapd.php %{buildroot}/var/clearos/base/daemon/slapd.php

%post core
logger -p local6.notice -t installer 'app-openldap-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/openldap/deploy/install ] && /usr/clearos/apps/openldap/deploy/install
fi

[ -x /usr/clearos/apps/openldap/deploy/upgrade ] && /usr/clearos/apps/openldap/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-openldap-core - uninstalling'
    [ -x /usr/clearos/apps/openldap/deploy/uninstall ] && /usr/clearos/apps/openldap/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/openldap/packaging
%exclude /usr/clearos/apps/openldap/unify.json
%dir /usr/clearos/apps/openldap
%dir /etc/openldap/cacerts
%dir /var/clearos/events/openldap_configuration
%dir /var/clearos/events/openldap_online
%dir /var/clearos/openldap
%dir /var/clearos/openldap/backup
%dir %attr(0775,root,webconfig) /var/clearos/openldap/lock
%dir /var/clearos/openldap/provision
/usr/clearos/apps/openldap/deploy
/usr/clearos/apps/openldap/language
/usr/clearos/apps/openldap/libraries
/var/clearos/events/certificate_manager/openldap
/etc/clearsync.d/filewatch-openldap-configuration-event.conf
/etc/clearsync.d/filewatch-openldap-online-event.conf
/usr/sbin/ldap-import
/var/clearos/events/network_configuration/openldap
/etc/openldap/schema/RADIUS-LDAPv3.schema
/etc/openldap/schema/clearcenter.schema
/etc/openldap/schema/clearfoundation.schema
/etc/openldap/schema/horde.schema
/etc/openldap/schema/kolab2.schema
/etc/openldap/schema/kopano.schema
/etc/openldap/schema/owncloud.schema
/etc/openldap/schema/pcn.schema
/etc/openldap/schema/rfc2307bis.schema
/etc/openldap/schema/rfc2739.schema
/etc/openldap/schema/samba3.schema
/etc/openldap/schema/zarafa.schema
/var/clearos/base/daemon/slapd.php
