Summary:	X11 drawing tool
Summary(pl):	Program do rysowania pod X11
Name:		xfig
Version:	3.2.2
Release:	2
Copyright:	Freeware
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.x.org/contrib/applications/drawing_tools/xfig/%{name}.%{version}.tar.gz
Patch0:		xfig-config.patch
Requires:	transfig >= 3.2
Buildroot:	/tmp/%{name}-%{version}-root

%description
This program gives you all the features you need to create basic- to
intermediate-level vector graphics, including bezier curves, lines,
rulers, and more. 

%description
Program xfig udostêpnia Ci wszystkie narzêdzia grafik wektorowych
sk³adaj±cychj siê z od prostych do zaawansowanych elementów wektorowych
jak: linie, krzywe bezier czy inne.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	DESTDIRR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xfig <<EOF
xfig name "xfig"
xfig description "Drawing Tool"
xfig group Graphics
xfig exec "xfig &"
EOF

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/xfig
/usr/X11R6/lib/X11/xfig
/usr/X11R6/man/man1/*
%config /usr/X11R6/lib/X11/app-defaults/*
%config /etc/X11/wmconfig/xfig

%changelog
* Tue Dec  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.2.2-2]
- added -q %setup parameter,
- changed Group to X11/Applications/Graphics,
- added gzipping man pages,
- spec rewrited for using Buildroot,
- added using %%{name} and %%{version} in Source,
- added using $RPM_OPT_FLAGS during compile,
- added %attr and %defattr macros in %files (allows build package from
  non-root account).

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version
- messed with config for 5.0
- updated Requires and Copyright
- added wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
