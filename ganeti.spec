%define name ganeti
%define version 2.4.4

Name: %{name}
Summary: Ganeti is a cluster virtual server management software tool built on top of existing virtualization
Version: %{version}
Release: %mkrel 1
License: GPLv3
Group: System/Cluster
Source: http://ganeti.googlecode.com/files/%{name}-%{version}.tar.gz
URL:	http://code.google.com/p/ganeti/
BuildArch: noarch
BuildRequires: socat, pylint, python-simplejson, python-parsing, python-pyinotify, python-sphinx, python-curl, python-OpenSSL
BuildRequires: graphviz, python-paramiko
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
Ganeti is a cluster virtual server management software tool built on top of existing virtualization 
technologies such as Xen or KVM and other Open Source software

Ganeti requires pre-installed virtualization software on your servers in order to function.
Once installed, the tool will take over the management part of the virtual instances (Xen DomU),
e.g. disk creation management, operating system installation for these instances (in co-operation with OS-specific install scripts), 
and startup, shutdown, failover between physical systems. It has been designed to facilitate cluster management of virtual servers 
and to provide fast and simple recovery after physical failures using commodity hardware. 

%prep
rm -rf %{buildroot}
%setup -q -n %{name}-%{version}

%build
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
%{python_sitearch}
%{_libdir}
/usr/sbin/
%{_mandir}/man7
%{_mandir}/man8


%clean
rm -rf $RPM_BUILD_ROOT
