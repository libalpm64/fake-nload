Summary        : A console application which monitors network traffic and bandwidth usage in real time
Name           : nload
Version        : 0.7.4
Release        : 1
Copyright      : GPL
Url            : http://www.roland-riegel.de/nload/index_en.html
Packager       : Helder Correia <helder.correia@netcabo.pt>
Group          : Applications/System
Source         : %{name}-%{version}.tar.gz
BuildRoot      : %{_tmppath}/%{name}-%{version}-root
Requires       : ncurses >= 5.0
BuildRequires  : ncurses-devel >= 5.0


%description
%{name} is a console application which monitors network traffic and bandwidth
usage in real time. It visualizes the in and outgoing traffic using two graphs
and provides additional info like total amount of transfered data and min/max
network usage.


%prep
%setup -q


%build
CFLAGS=${RPM_OPT_FLAGS} CXXFLAGS=${RPM_OPT_FLAGS} ./configure --prefix=%{_prefix} --mandir=%{_mandir}
make


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
* Wed Aug 14 2002 Helder Correia <helder.correia@netcabo.pt>
- Initial RPM release.
