Summary:	X11 drawing tool
Summary(de):	X11-Zeichen-Tool
Summary(es):	Herramienta para dise�o X11
Summary(fr):	Outil de dessin sous X11
Summary(pl):	Program do rysowania pod X11
Summary(pt_BR):	Ferramenta para desenho X11
Summary(tr):	X11 �izim arac�
Name:		xfig
Version:	3.2.3d
Release:	6
License:	Freeware
Group:		X11/Applications/Graphics
Source0:	http://www.xfig.org/xfigdist/%{name}.%{version}.full.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-i18n.patch
Icon:		xfig.xpm
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
URL:		http://www.xfig.org/
Requires:	transfig >= 3.2.3c-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xfig-doc

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

%description -l es
Este programa ofrece todo lo que necesitas para crear gr�ficos con
vectores, incluyendo curvas, l�neas, reglas, y m�s.

%description -l fr
Ce programme vous offre tout ce dont vous avez besoin pour cr�er des
graphiques vectoriels, de base � moyennement complexes. Il comprend
les courbes de B�zier, les lignes, les r�gles etc.

%description -l pl
Program xfig udost�pnia Ci wszystkie narz�dzia grafik wektorowych
sk�adaj�cych si� z prostych i zaawansowanych element�w wektorowych jak
linie, krzywe bezier i wiele innych.

%description -l pt_BR
Este programa oferece tudo o que voc� precisa para criar gr�ficos com
vetores, incluindo curvas, linhas, r�guas, e mais.

%description -l tr
Bu program, en temel olanlar�ndan ileri d�zeydekilere kadar t�m belli
ba�l� vekt�r grafikleri (do�rular, bezier e�risi vs) �izebilmenize
olanak verir.

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1

%build
xmkmf -a
perl -p -i -e 's-LN. Doc/-LN) -' Makefile
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags} `pkg-config --cflags libpng12 2>/dev/null`" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}" \
	XFIGDOCDIR="%{_docdir}/%{name}-doc-%{version}/"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_datadir}/pixmaps}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -ar Examples/Libraries $RPM_BUILD_ROOT%{_libdir}/X11/xfig
rm -f $RPM_BUILD_ROOT%{_libdir}/X11/xfig/Libraries/*/README

(
cat $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig
tail +2 $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig-color
echo 'Fig.inches: off'
) 	> $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig.new
mv -f $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig.new \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Fig

gzip -9nf README CHANGES FIGAPPS Doc/TODO Doc/FORMAT*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz Doc/*.gz Doc/html/ Doc/*.html
%attr(755,root,root) %{_bindir}/xfig
%{_libdir}/X11/xfig
%{_libdir}/X11/app-defaults/Fig
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/xfig.desktop
