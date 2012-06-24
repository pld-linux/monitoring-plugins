#
# TODO:
# - see anything useful from contrib/
# - package requisites for unifished packages -nsclient and -nwstat
#   REQUIREMENTS explains the dependencies.
#
Summary:	Host/service/network monitoring program plugins for Nagios
Summary(pl):	Wtyczki do monitorowania host�w/us�ug/sieci dla Nagiosa
Name:		nagios-plugins
Version:	1.4
Release:	0.1
License:	GPL v2
Group:		Networking
Source0:	http://dl.sourceforge.net/nagiosplug/%{name}-%{version}.tar.gz
# Source0-md5:	9b21b92acc4b2b0dbb2d12bca6b27582
Patch0:		%{name}-configure.patch
Patch1:		%{name}-fping.patch
Patch2:		%{name}-subst.patch
Patch3:		%{name}-check_swap.c.patch
URL:		http://nagiosplug.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-utils
BuildRequires:	net-snmp-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	gettext-devel
# Not really neccesary at build time
BuildRequires:	iputils-ping
BuildRequires:	postgresql-devel
BuildRequires:	perl-Net-SNMP
BuildRequires:	radiusclient-devel
BuildRequires:	fping
BuildRequires:	qstat
BuildRequires:	samba-client
# for rpcinfo
BuildRequires:	glibc-misc
# for host and nslookup
BuildRequires:	bind-utils
BuildRequires:	ntp
Requires:	nagios
Conflicts:	iputils-ping < 1:ss020124
Obsoletes:	netsaint-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_plugindir	%{_libdir}/nagios/plugins

%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a Unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
nagios package.

%description -l pl
Nagios to program monitoruj�cy hosty i us�ugi w sieci i powiadamiaj�cy
poczt� elektroniczn� lub na pager o wyst�pieniu lub rozwi�zaniu
problem�w. Nagios dzia�a na serwerze uniksowym w tle lub jako demon,
regularnie przeprowadzaj�c kontrol� r�nych podanych mu us�ug. Sama
kontrola us�ug jest wykonywana poprzez oddzielne "wtyczki" - programy
zwracajace stan danej us�ugi do Nagiosa.

Ten pakiet zawiera podstawowe wtyczki do u�ywania z pakietem nagios.

%package snmp
Summary:	Nagios plugins using SNMP protocol to query information
Summary(pl):	Wtyczki Nagiosa u�ywaj�ce protoko�u SNMP w celu uzyskania informacji
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	net-snmp-utils
Requires:	perl-Net-SNMP

%description snmp
Nagios plugins using SNMP protocol to query information.

%description snmp -l pl
Wtyczki Nagiosa u�ywaj�ce protoko�u SNMP w celu uzyskania informacji.

%package samba
Summary:	Nagios plugin to check remote disk using smbclient
Summary(pl):	Wtyczka Nagiosa do zdalnego sprawdzania dysku z u�yciem smbclienta
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	samba-client

%description samba
Perl Check SMB Disk plugin for Nagios.

%description samba -l pl
Perlowa wtyczka dla Nagiosa sprawdzaj�ca dyski SMB.

%package sensors
Summary:	Nagios plugin to check hardware status using the lm_sensors package
Summary(pl):	Wtyczka Nagiosa do sprawdzania stanu sprz�tu przy u�yciu pakietu lm_sensors
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	lm_sensors

%description sensors
This plugin checks hardware status using the lm_sensors package.

%description sensors -l pl
Ta wtyczka sprawdza stan sprz�tu przy u�yciu pakietu lm_sensors.

%package mysql
Summary:	Nagios plugin to test a MySQL DBMS
Summary(pl):	Wtyczka Nagiosa do sprawdzania systemu baz danych MySQL
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mysql-libs

%description mysql
This plugin tests a MySQL DBMS to determine whether it is active and
accepting queries.

%description mysql -l pl
Ta wtyczka sprawdza serwer baz danych MySQL, aby okre�li�, czy jest
aktywny i przyjmuje zapytania.

%package pgsql
Summary:	Nagios plugin to test a PostgreSQL DBMS
Summary(pl):	Wtyczka Nagiosa do sprawdzania systemu baz danych PostgreSQL
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	postgresql-libs

%description pgsql
This plugin tests a PostgreSQL DBMS to determine whether it is active
and accepting queries. In its current operation, it simply connects to
the specified database, and then disconnects. If no database is
specified, it connects to the template1 database, which is present in
every functioning PostgreSQL DBMS.

%description pgsql -l pl
Ta wtyczka sprawdza serwer baz danych PostgreSQL, aby okre�li�, czy
jest aktywny i przyjmuje zapytania. Aktualnie po prostu ��czy si� do
okre�lonej bazy danych i roz��cza. Je�li nie podano bazy danych, ��czy
si� do bazy danych template1, obecnej w ka�dym dzia�aj�cym systemie
PostgreSQL.

%package radius
Summary:	Nagios plugin to test a radius server to see if it is accepting connections
Summary(pl):	Wtyczka Nagiosa do sprawdzania serwera radius pod k�tem przyjmowania po��cze�
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	radiusclient

%description radius
This plugin tests a radius server to see if it is accepting connections.

%description radius -l pl
Ta wtyczka sprawdza serwer us�ugi radius, aby zobaczy�, czy przyjmuje
po��czenia.

%package qstat
Summary:	Nagios plugin to check status of Internet game servers
Summary(pl):	Wtyczka Nagiosa do sprawdzania stanu serwer�w gier internetowych
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	qstat

%description qstat
This plugin uses the 'qstat' command, the popular game server status
query tool.

QStat is a command-line program that displays information about
Internet game servers.

The servers are either down, non-responsive, or running a game. For
servers running a game, the server name, map name, current number of
players, and response time are displayed. Server rules and player
information may also be displayed.

%description qstat -l pl
Ta wtyczka u�ywa polecenia 'qstat' - popularnego narz�dzia do
zapyta� o stan serwer�w gier.

QStat to program dzia�aj�cy z linii polece� wy�wietlaj�cy informacje o
serwerach gier internetowych.

Serwery mog� by� wy��czone, nie odpowiada�, b�d� mie� uruchomion� gr�.
Dla serwer�w z grami wy�wietlanea s�: nazwa serwera, nazwa mapy,
aktualna liczba graczy i czas odpowiedzi. Mog� by� dodatkowo
wy�wietlone regu�y serwera i informacje o graczach.

%package ldap
Summary:	Nagios plugin to check LDAP servers
Summary(pl):	Wtyczka Nagiosa do sprawdzania serwer�w LDAP
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	openldap-libs

%description ldap
Nagios plugin to check LDAP servers.

%description ldap -l pl
Wtyczka Nagiosa do sprawdzania serwer�w LDAP.

# nsclient not packaged in PLD
#%package nsclient
#Summary:	Nagios plugin to check NT server with NSClient
#Summary(pl):	Wtyczka Nagiosa do sprawdzania serwera NT przy u�yciu NSClienta
#Group:		Networking
#Requires:	%{name} = %{version}-%{release}
#Requires:	nsclient
#
#%description nsclient
#Nagios plugin to check NT server with NSClient.
#
#%description nsclient -l pl
#Wtyczka Nagiosa do sprawdzania serwera NT przy u�yciu NSClienta.

# requisite not packaged in PLD
#%package nwstat
#Summary:	Nagios plugin nwstat
#Summary(pl):	Wtyczka nwstat do Nagiosa
#Group:		Networking
#Requires:	%{name} = %{version}-%{release}
#Requires:	mrtgext
#
#%description nsclient
#Nagios plugin using MRTGEXT module
#(http://forge.novell.com/modules/xfmod/project/?mrtgext).
#
#%description nsclient -l pl
#Wtyczka nagiosa u�ywaj�ca modu�u MRTGEXT
#(http://forge.novell.com/modules/xfmod/project/?mrtgext).

%package contrib
Summary:	Contributed nagios plugins
Group:		Networking
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description contrib
Contributed nagios plugins. Some of them work, some do

%prep
%setup -q
#%patch0 -p0
%patch1 -p0
#%patch2 -p0
#%patch3 -p0

# bring contribs into shape...
mv contrib/check_compaq_insight.pl{,msg}
sed -ne '/--- cut ---/,/--- cut ---/{/--- cut ---/!p}' < \
	contrib/check_compaq_insight.pl.msg > contrib/check_compaq_insight.pl

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

# need /usr/sbin in PATH,
# otherwise configure will fail locating ntpq and few others.
%configure \
	PATH=${PATH}:/usr/sbin \
	--libexecdir=%{_plugindir} \
	--with-cgiurl=/nagios/cgi-bin \
	--with-ping_command='/bin/ping -n %%s -c %%d' \
	--with-df-command="/bin/df" \
	--with-mailq-command="/usr/bin/mailq" \
	--with-host-command="/usr/bin/host" \
	--with-nslookup-command="/usr/bin/nslookup -sil" \
	--with-uptime-command="/usr/bin/uptime" \
	--with-smbclient-command="/usr/bin/smbclient" \
	--with-ps-command="/bin/ps -weo 'vsz comm'" \
	--with-ps-format="%d %s" \
	--with-ps-raw-command="/bin/ps -weo 'stat user ppid args'" \
	--with-ps-varlist="procstat,&procuid,&procppid,procprog,&pos" \
	--with-rss-command="/bin/ps -weo \'vsz comm\' -weo \'rss comm'" \
	--with-rss-format="%d %s" \
	--with-vsz-command="/bin/ps -weo 'vsz comm' -weo 'vsz comm'" \
	--with-vsz-format="%d %s" \
	--with-ssh-command="/usr/bin/ssh" \
	--with-mysql \
	--with-pgsql \

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd contrib
# work in progress, currently in install section for faster testing (--short-circuit is my friend)

%{__cc} %{rpmcflags} check_cluster.c -o check_cluster
%{__cc} %{rpmcflags} check_cluster2.c -o check_cluster2
#%{__cc} %{rpmcflags} check_hltherm.c -o check_hltherm
#%{__cc} %{rpmcflags} check_http-with-client-certificate.c -o check_http-with-client-certificate
#%{__cc} %{rpmcflags} check_ipxping.c -o check_ipxping
#%{__cc} %{rpmcflags} check_logins.c -o check_logins

%{__cc} %{rpmcflags} check_mysql.o -o check_mysql $(mysql_config --libs)
%{__cc} %{rpmcflags} check_mysql.c -c $(mysql_config --cflags) -I../plugins -I.. -I../lib
mv check_mysql check_mysql2

%{__cc} %{rpmcflags} -I../plugins -I.. -I../lib -c check_rbl.c
%{__cc} %{rpmcflags} check_rbl.o -o check_rbl ../plugins/popen.o ../plugins/utils.o ../plugins/netutils.o

%{__cc} %{rpmcflags} check_timeout.c -o check_timeout

%{__cc} %{rpmcflags} -I../plugins -I.. -I../lib -c check_uptime.c
%{__cc} %{rpmcflags} check_uptime.o -o check_uptime ../plugins/popen.o ../plugins/utils.o

chmod a+x check_*.{pl,sh,py}
chmod a+x check_{fan_{cpq,fsc}_present,frontpage,oracle_tbs,pfstate,temp_{cpq,fsc}}

sed -i -e "s,use lib '/usr/local/nagios/libexec/',use lib '/usr/lib/nagios/plugins'," *.pl

find -name 'check_*' -type f -perm +1 | xargs -ri install {} $RPM_BUILD_ROOT/%{_plugindir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS AUTHORS BUGS CHANGES CODING ChangeLog
%doc FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS

%defattr(755,root,root,755)
# utils
%{_plugindir}/negate
%{_plugindir}/urlize
%{_plugindir}/utils.pm
%{_plugindir}/utils.sh

# plugins
%{_plugindir}/check_by_ssh
%{_plugindir}/check_dig
%{_plugindir}/check_disk
%{_plugindir}/check_dns
%{_plugindir}/check_dummy
%{_plugindir}/check_fping
%{_plugindir}/check_ftp
%{_plugindir}/check_http
%{_plugindir}/check_imap
%{_plugindir}/check_ircd
%{_plugindir}/check_load
%{_plugindir}/check_log
%{_plugindir}/check_mailq
%{_plugindir}/check_mrtg
%{_plugindir}/check_mrtgtraf
%{_plugindir}/check_nntp
%{_plugindir}/check_ntp
%{_plugindir}/check_overcr
%{_plugindir}/check_ping
%{_plugindir}/check_pop
%{_plugindir}/check_real
%{_plugindir}/check_rpc
%{_plugindir}/check_simap
%{_plugindir}/check_smtp
%{_plugindir}/check_spop
%{_plugindir}/check_ssh
%{_plugindir}/check_tcp
%{_plugindir}/check_time
%{_plugindir}/check_udp
%{_plugindir}/check_ups
%{_plugindir}/check_users
#%{_plugindir}/check_vsz
%{_plugindir}/check_swap

# segfaults under 2.6
%{_plugindir}/check_procs

# requries license.dat
%{_plugindir}/check_flexlm

# Cannot determine ORACLE_HOME for sid
# probably needs some external programs. can't test
%{_plugindir}/check_oracle

%{_plugindir}/check_nagios

# new
%{_plugindir}/check_dhcp
%{_plugindir}/check_file_age
%{_plugindir}/check_icmp

# Not to be confused with nagios-snmp-plugins
%files snmp
%defattr(755,root,root,755)
%{_plugindir}/check_snmp
%{_plugindir}/check_hpjd
%{_plugindir}/check_ifoperstatus
%{_plugindir}/check_ifstatus

# syntax errors, incomplete file paths
%{_plugindir}/check_wave
# syntax errors
%{_plugindir}/check_breeze

%files samba
%defattr(755,root,root,755)
%{_plugindir}/check_disk_smb

%files sensors
%defattr(755,root,root,755)
%{_plugindir}/check_sensors

%files mysql
%defattr(755,root,root,755)
%{_plugindir}/check_mysql

%files pgsql
%defattr(755,root,root,755)
%{_plugindir}/check_pgsql

%files radius
%defattr(755,root,root,755)
%{_plugindir}/check_radius

%files qstat
%defattr(755,root,root,755)
%{_plugindir}/check_game

%files ldap
%defattr(755,root,root,755)
%{_plugindir}/check_ldap

#%files nsclient
#%defattr(755,root,root,755)
#%{_plugindir}/check_nt

#%files nwstat
#%defattr(755,root,root,755)
#%{_plugindir}/check_nwstat

%files contrib
%defattr(755,root,root,755)
%{_plugindir}/check_adptraid.sh
%{_plugindir}/check_apache.pl
%{_plugindir}/check_apc_ups.pl
%{_plugindir}/check_appletalk.pl
%{_plugindir}/check_arping.pl
%{_plugindir}/check_asterisk.pl
%{_plugindir}/check_axis.sh
%{_plugindir}/check_backup.pl
%{_plugindir}/check_bgpstate.pl
%{_plugindir}/check_breeze.pl
%{_plugindir}/check_cluster
%{_plugindir}/check_cluster2
%{_plugindir}/check_compaq_insight.pl
#%{_plugindir}/check_cpqarray
%{_plugindir}/check_digitemp.pl
%{_plugindir}/check_disk_snmp.pl
%{_plugindir}/check_dl_size.pl
%{_plugindir}/check_dlswcircuit.pl
%{_plugindir}/check_dns_random.pl
%{_plugindir}/check_email_loop.pl
%{_plugindir}/check_fan_cpq_present
%{_plugindir}/check_fan_fsc_present
%{_plugindir}/check_flexlm.pl
%{_plugindir}/check_frontpage
%{_plugindir}/check_ftpget.pl
#%{_plugindir}/check_hltherm.c
%{_plugindir}/check_hprsc.pl
#%{_plugindir}/check_http-with-client-certificate.c
%{_plugindir}/check_hw.sh
%{_plugindir}/check_ica_master_browser.pl
%{_plugindir}/check_ica_metaframe_pub_apps.pl
%{_plugindir}/check_ica_program_neigbourhood.pl
%{_plugindir}/check_inodes-freebsd.pl
%{_plugindir}/check_inodes.pl
#%{_plugindir}/check_ipxping.c
%{_plugindir}/check_javaproc.pl
%{_plugindir}/check_joy.sh
%{_plugindir}/check_linux_raid.pl
%{_plugindir}/check_lmmon.pl
%{_plugindir}/check_log2.pl
#%{_plugindir}/check_logins.c
%{_plugindir}/check_lotus.pl
%{_plugindir}/check_maxchannels.pl
%{_plugindir}/check_maxwanstate.pl
%{_plugindir}/check_mem.pl
%{_plugindir}/check_ms_spooler.pl
%{_plugindir}/check_mssql.sh
#%{_plugindir}/check_mysql.c
%{_plugindir}/check_mysql.pl
%{_plugindir}/check_mysqlslave.pl
%{_plugindir}/check_nagios.pl
%{_plugindir}/check_nagios_db.pl
%{_plugindir}/check_nagios_db_pg.pl
%{_plugindir}/check_netapp.pl
%{_plugindir}/check_nmap.py
%{_plugindir}/check_nt
%{_plugindir}/check_nwstat
%{_plugindir}/check_nwstat.pl
%{_plugindir}/check_ora_table_space.pl
%{_plugindir}/check_oracle_instance.pl
%{_plugindir}/check_oracle_tbs
%{_plugindir}/check_pcpmetric.py
%{_plugindir}/check_pfstate
%{_plugindir}/check_pop3.pl
%{_plugindir}/check_procl.sh
%{_plugindir}/check_procr.sh
%{_plugindir}/check_qmailq.pl
%{_plugindir}/check_rbl
%{_plugindir}/check_remote_nagios_status.pl
%{_plugindir}/check_rrd_data.pl
%{_plugindir}/check_sap.sh
%{_plugindir}/check_smart.pl
%{_plugindir}/check_smb.sh
%{_plugindir}/check_snmp_disk_monitor.pl
%{_plugindir}/check_snmp_printer.pl
%{_plugindir}/check_snmp_process_monitor.pl
%{_plugindir}/check_snmp_procs.pl
%{_plugindir}/check_sockets.pl
%{_plugindir}/check_sybase
%{_plugindir}/check_temp_cpq
%{_plugindir}/check_temp_fsc
%{_plugindir}/check_timeout
%{_plugindir}/check_traceroute-pure_perl.pl
%{_plugindir}/check_traceroute.pl
%{_plugindir}/check_uptime
%{_plugindir}/check_vcs.pl
%{_plugindir}/check_wave.pl

%{_plugindir}/check_mysql2
%{_plugindir}/check_wins.pl
