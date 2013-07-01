Name:    ganeti
Summary: Cluster virtual server management software tool
Version: 2.6.0
Release: 2
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
%{python_sitelib}
%{_sbindir}/g*
%{_libdir}/%{name}
%{_mandir}/man7/*
%{_mandir}/man1/*
%{_mandir}/man8/*


%changelog
* Wed Aug 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.6.0-1mdv2012.0
+ Revision: 814893
- version update 2.6.0

* Thu Jul 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5.2-1
+ Revision: 811148
- version update 2.5.2

* Tue Oct 04 2011 Leonardo Coelho <leonardoc@mandriva.org> 2.4.4-1
+ Revision: 702949
- first mandriva version
- Created package structure for ganeti.

