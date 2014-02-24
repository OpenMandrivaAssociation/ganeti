Summary:	Ganeti is a cluster virtual server management software tool
Name:		ganeti
Version:	2.9.4
Release:	1
License:	GPLv3+
Group:		System/Cluster
Source0:	http://ganeti.googlecode.com/files/%{name}-%{version}.tar.gz
Url:		http://code.google.com/p/ganeti/
BuildArch:	noarch
BuildRequires:	graphviz
BuildRequires:	python-curl
BuildRequires:	python-OpenSSL
BuildRequires:	python-paramiko
BuildRequires:	python-parsing
BuildRequires:	python-pyinotify
BuildRequires:	python-simplejson
BuildRequires:	python-sphinx
BuildRequires:	socat

%description
Ganeti is a cluster virtual server management software tool built on top of
existing virtualization technologies such as Xen or KVM and other Open Source
software.

Ganeti requires pre-installed virtualization software on your servers in order
to function. Once installed, the tool will take over the management part of the
virtual instances (Xen DomU), e.g. disk creation management, operating system
installation for these instances (in co-operation with OS-specific install
scripts), and startup, shutdown, failover between physical systems.

It has been designed to facilitate cluster management of virtual servers and
to provide fast and simple recovery after physical failures using commodity
hardware.

%files
%{python_sitelib}
%{_sbindir}/g*
%{_libdir}/%{name}
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
export PATH=$PATH:/sbin/
./configure \
	--localstatedir=%{buildroot}%{_var} \
	--sysconfdir=%{buildroot}%{_sysconfdir}
%make

%install
mkdir -p %{buildroot}/%{_var}
mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/srv/%{name}/export
mkdir -p %{buildroot}/srv/%{name}/os
mkdir -p %{buildroot}/srv/%{name}/file-storage
%makeinstall_std

