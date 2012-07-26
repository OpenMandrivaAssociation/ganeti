%define name ganeti
%define version 2.5.2

Name: %{name}
Summary: Ganeti is a cluster virtual server management software tool
Version: %{version}
Release: %mkrel 1
License: GPLv3
Group: System/Cluster
Source0: http://ganeti.googlecode.com/files/%{name}-%{version}.tar.gz
URL:	http://code.google.com/p/ganeti/
BuildArch: noarch
BuildRequires: socat, python-simplejson, python-parsing, python-pyinotify, python-sphinx, python-curl, python-OpenSSL
BuildRequires: graphviz, python-paramiko

%description
Ganeti is a cluster virtual server
management software tool built on
top of existing virtualization 
technologies such as Xen or KVM
and other Open Source software

Ganeti requires pre-installed virtualization
software on your servers in order to function.
Once installed, the tool will take over the
management part of the virtual instances (Xen DomU),
e.g. disk creation management, operating system installation
for these instances (in co-operation with OS-specific install scripts), 
and startup, shutdown, failover between physical systems.
It has been designed to facilitate cluster management of virtual servers 
and to provide fast and simple recovery after physical
failures using commodity hardware. 

%prep
%setup -q -n %{name}-%{version}

%build
export PATH=$PATH:/sbin/
./configure --localstatedir=%{buildroot}%_var --sysconfdir=%{buildroot}%_sysconfdir 
%make

%install
mkdir -p %{buildroot}/%_var
mkdir -p %{buildroot}/%_sysconfdir
mkdir -p %{buildroot}/srv/%{name}/export
mkdir -p %{buildroot}/srv/%{name}/os
mkdir -p %{buildroot}/srv/%{name}/file-storage
%makeinstall

%files
%defattr(0755,root,root)
%_var/*
%{python_sitelib}
%{_libdir}
/usr/sbin/
%{_mandir}/man7
%{_mandir}/man1
%{_mandir}/man8
