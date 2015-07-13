<?php

/////////////////////////////////////////////////////////////////////////////
// General information
/////////////////////////////////////////////////////////////////////////////

$app['basename'] = 'openldap';
$app['version'] = '1.6.9';
$app['release'] = '1';
$app['vendor'] = 'ClearFoundation';
$app['packager'] = 'ClearFoundation';
$app['license'] = 'GPLv3';
$app['license_core'] = 'LGPLv3';
$app['description'] = lang('openldap_app_description');

/////////////////////////////////////////////////////////////////////////////
// App name and categories
/////////////////////////////////////////////////////////////////////////////

$app['name'] = lang('openldap_app_name');
$app['category'] = lang('base_category_server');
$app['subcategory'] = lang('base_subcategory_directory');
$app['menu_enabled'] = FALSE;

/////////////////////////////////////////////////////////////////////////////
// Packaging
/////////////////////////////////////////////////////////////////////////////

$app['core_only'] = TRUE;

$app['core_provides'] = array(
    'system-ldap-driver'
);

$app['core_requires'] = array(
    'app-certificate-manager-core',
    'app-ldap-core >= 1:1.6.1',
    'app-mode-core',
    'app-network-core >= 1:1.6.9',
    'openldap-servers >= 2.4.39',
    'openldap-clients >= 2.4.39',
    'openssl',
);

$app['core_directory_manifest'] = array(
    '/etc/openldap/cacerts' => array(),
    '/var/clearos/events/openldap_online' => array(),
    '/var/clearos/events/openldap_configuration' => array(),
    '/var/clearos/openldap' => array(),
    '/var/clearos/openldap/backup' => array(),
    '/var/clearos/openldap/provision' => array(),
    '/var/clearos/openldap/lock' => array(
        'mode' => '0775',
        'owner' => 'root',
        'group' => 'webconfig',
    ),
);

$app['core_file_manifest'] = array(
    'schema/clearfoundation.schema' => array( 'target' => '/etc/openldap/schema/clearfoundation.schema' ),
    'schema/clearcenter.schema' => array( 'target' => '/etc/openldap/schema/clearcenter.schema' ),
    'schema/horde.schema' => array( 'target' => '/etc/openldap/schema/horde.schema' ),
    'schema/kolab2.schema' => array( 'target' => '/etc/openldap/schema/kolab2.schema' ),
    'schema/owncloud.schema' => array( 'target' => '/etc/openldap/schema/owncloud.schema' ),
    'schema/pcn.schema' => array( 'target' => '/etc/openldap/schema/pcn.schema' ),
    'schema/RADIUS-LDAPv3.schema' => array( 'target' => '/etc/openldap/schema/RADIUS-LDAPv3.schema' ),
    'schema/rfc2307bis.schema' => array( 'target' => '/etc/openldap/schema/rfc2307bis.schema' ),
    'schema/rfc2739.schema' => array( 'target' => '/etc/openldap/schema/rfc2739.schema' ),
    'schema/samba.schema' => array( 'target' => '/etc/openldap/schema/samba3.schema' ),
    'schema/zarafa.schema' => array( 'target' => '/etc/openldap/schema/zarafa.schema' ),
    'slapd.php'=> array('target' => '/var/clearos/base/daemon/slapd.php'),
    'filewatch-openldap-online-event.conf'=> array('target' => '/etc/clearsync.d/filewatch-openldap-online-event.conf'),
    'filewatch-openldap-configuration-event.conf'=> array('target' => '/etc/clearsync.d/filewatch-openldap-configuration-event.conf'),
    'certificate-manager-event'=> array(
        'target' => '/var/clearos/events/certificate_manager/openldap',
        'mode' => '0755'
    ),
    'network-configuration-event'=> array(
        'target' => '/var/clearos/events/network_configuration/openldap',
        'mode' => '0755'
    ),
    'ldap-import'=> array(
        'target' => '/usr/sbin/ldap-import',
        'mode' => '0755'
    ),
);
