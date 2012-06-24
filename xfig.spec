Summary:	X11 drawing tool
Summary(de):	X11-Zeichen-Tool
Summary(fr):	Outil de dessin sous X11
Summary(pl):	Program do rysowania pod X11
Summary(tr):	X11 �izim arac�
Name:		xfig
Version:	3.2.3c
Release:	6
License:	Freeware
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	http://www.xfig.org/xfigdist/%{name}.%{version}.full.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-i18n.patch
Icon:		xfig.xpm
BuildRequires:	libjpeg-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	XFree86-devel
URL:		http://www.xfig.org/
Requires:	transfig >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program gives you all the features you need to create basic- to
intermediate-level vector graphics, including bezier curves, lines,
rulers, and more.

%description -l de
Dieses Programm bietet s�mtliche Funktionen, die Sie zum Erstellen von
elementaren und fortgeschrittenen Vektorgrafiken ben�tigen,
einschlie�lich Bezier-Kurven, Linien, Lineale und anderes.

%description -l fr
Ce programme vous offre tout ce dont vous avez besoin pour cr�er des
graphiques vectoriels, de base � moyennement complexes. Il comprend
les courbes de B�zier, les lignes, les r�gles etc.

%description -l pl
Program xfig udost�pnia Ci wszystkie narz�dzia grafik wektorowych
sk�adaj�cych si� z prostych i zaawansowanych element�w wektorowych jak
linie, krzywe bezier i wiele innych.

%description -l tr
Bu program, en temel olanlar�ndan ileri d�zeydekilere kadar t�m belli
ba�l� vekt�r grafikleri (do�rular, bezier e�risi vs) �izebilmenize
olanak verir.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} CDEBUGFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" \
	CXXDEBUGFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}" \
	LOCAL_LDFLAGS="%{!?debug:-s}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_datadir}/pixmaps}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

(
cat $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig
tail +2 $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig-color
echo 'Fig.inches: off'
) 	> $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig.new
mv -f $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig.new \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig

gzip -9nf README CHANGES FIGAPPS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,FIGAPPS}.gz
%attr(755,root,root) %{_bindir}/xfig
%dir %{_libdir}/X11/xfig
%{_libdir}/X11/xfig/CompKeyDB
%{_libdir}/X11/xfig/Libraries
%{_libdir}/X11/xfig/xfig*
%dir %{_libdir}/X11/xfig/html
%{_libdir}/X11/xfig/html/*.*
%{_libdir}/X11/xfig/html/images
%lang(ja) %{_libdir}/X11/xfig/html/japanese

%{_libdir}/X11/app-defaults/Fig
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
%{_applnkdir}/Graphics/xfig.desktop
