Summary:	X11 drawing tool
Summary(pl):	Program do rysowania pod X11
Name:		xfig
Version:	3.2.2
Release:	7
Copyright:	Freeware
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.x.org/contrib/applications/drawing_tools/xfig/%{name}.%{version}.tar.gz
Source1:	xfig.desktop
Patch0:		xfig-config.patch
Patch1:		xfig-vararg.patch
BuildRequires:	libjpeg-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
Requires:	transfig >= 3.2
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program gives you all the features you need to create basic- to
intermediate-level vector graphics, including bezier curves, lines,
rulers, and more. 

%description -l pl
Program xfig udostêpnia Ci wszystkie narzêdzia grafik wektorowych
sk³adaj±cych siê z prostych i zaawansowanych elementów wektorowych
jak linie, krzywe bezier i wiele innych.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics

make install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics

(cat $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig
tail +2 $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig-color) \
	> $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig.new
mv -f $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig.new \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README CHANGES FIGAPPS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,FIGAPPS}.gz
%attr(755,root,root) %{_bindir}/xfig
%dir %{_libdir}/X11/xfig
%{_libdir}/X11/xfig/CompKeyDB
%{_libdir}/X11/xfig/Libraries
%dir %{_libdir}/X11/xfig/html
%{_libdir}/X11/xfig/html/*.*
%{_libdir}/X11/xfig/html/images
%lang(ja) %{_libdir}/X11/xfig/html/japanese

%{_libdir}/X11/app-defaults/Fig

%{_mandir}/man1/*

%{_datadir}/applnk/Graphics/xfig.desktop
