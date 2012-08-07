%define		plugin	autom8
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Automate Creation of Graphs and Tree Entries
Name:		cacti-plugin-%{plugin}
Version:	0.35
Release:	5
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{version}.tgz
# Source0-md5:	a79e33fd85aff9e7e415771d9331ed9a
URL:		http://docs.cacti.net/plugin:autom8
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti
Requires:	cacti(pia) >= 2.4
Requires:	php(mysql)
Requires:	php(pcre)
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
Maintaining a quite decent Cacti installation with lots of devices,
graphs and tree items may result in quite a huge amount of
administrative work.

Using the CLI scripts allows you to write your own scripts to e.g.
create Cacti device entries, graphs, tree items and more. This helps
e.g. interfacing a CMDB or some other repository that holds
information about devices that shall be monitored.

%prep
%setup -qc
mv trunk %{plugin}
mv %{plugin}/{LICENSE,README,automate_manual.pdf} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README automate_manual.pdf
%{plugindir}
