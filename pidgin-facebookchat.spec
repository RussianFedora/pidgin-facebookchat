%define library_name libfacebook
%define library_target %{library_name}.so
%ifarch x86_64
%define library_target %{library_name}64.so
%endif

Name:		pidgin-facebookchat
Version:	1.69
Release:	1%{?dist}
Summary:	Facebook Chat for Pidgin

Group:		Applications/Communications
License:	GPLv3+
URL:		http://code.google.com/p/pidgin-facebookchat/
Source0:	http://pidgin-facebookchat.googlecode.com/files/%{name}-source-%{version}.tar.bz2
Patch1:		%{name}-makefile.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	glib2-devel
BuildRequires:	libpurple-devel
BuildRequires:	json-glib-devel
BuildRequires:	zlib-devel
Requires:	pidgin
Requires:	libpurple

%description
This is a Facebook chat plugin for Pidgin and libpurple messengers. It connects to the new Facebook Chat IM service without the need for an API key.
It was created by Eion Robb in May 2008 and has had major code additions by Casey Ho and Mark Doliner who joined the project at the end of 2008.


%prep
%setup -q -n %{name}
chmod 0644 *.c *.h COPYING *.png
%patch1 -p0 -b .makefile-fix

%build
make %{?_smp_mflags} %{library_target}

%install
rm -rf %{buildroot}
install -D -m 755 %{library_target} %{buildroot}%{_libdir}/purple-2/%{library_target}
install -D -m 644 facebook16.png %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/16/facebook.png
install -D -m 644 facebook22.png %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/22/facebook.png
install -D -m 644 facebook48.png %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/48/facebook.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/facebook.png


%changelog
* Mon Dec  6 2010 Alexei Panov <elemc@atisserv.ru> - 1.69-1
- new release
* Thu Nov 18 2010 Alexei Panov <elemc@atisserv.ru> - 1.68-1
- Initial build