Summary:	X11 drawing tool
Summary(de):	X11-Zeichen-Tool
Summary(es):	Herramienta para diseño X11
Summary(fr):	Outil de dessin sous X11
Summary(pl):	Program do rysowania pod X11
Summary(pt_BR):	Ferramenta para desenho X11
Summary(ru):	éÎÓÔÒÕÍÅÎÔ ÄÌÑ ÒÉÓÏ×ÁÎÉÑ ÐÒÏÓÔÏÊ ×ÅËÔÏÒÎÏÊ ÇÒÁÆÉËÉ
Summary(tr):	X11 çizim aracý
Summary(uk):	¶ÎÓÔÒÕÍÅÎÔ ÄÌÑ ÍÁÌÀ×ÁÎÎÑ ÐÒÏÓÔÏ§ ×ÅËÔÏÒÎÏ§ ÇÒÁÆ¦ËÉ
Name:		xfig
Version:	3.2.5
%define	_pre	alpha5
Release:	0.%{_pre}.1
License:	Freeware
Group:		X11/Applications/Graphics
#Source0:	http://www.xfig.org/xfigdist/%{name}.%{version}.full.tar.gz
Source0:	http://www.xfig.org/alpha/%{name}.%{version}-%{_pre}.full.tar.gz
# Source0-md5:	7547b66232569e3c12e4a0639bd92629
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-i18n.patch
Patch2:		%{name}-mkstemp.diff
Icon:		xfig.xpm
URL:		http://www.xfig.org/
BuildRequires:	XFree86-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
Requires:	transfig >= 3.2.3c-3
Requires:	netpbm-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xfig-doc

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This program gives you all the features you need to create basic- to
intermediate-level vector graphics, including bezier curves, lines,
rulers, and more.

%description -l de
Dieses Programm bietet sämtliche Funktionen, die Sie zum Erstellen von
elementaren und fortgeschrittenen Vektorgrafiken benötigen,
einschließlich Bezier-Kurven, Linien, Lineale und anderes.

%description -l es
Este programa ofrece todo lo que necesitas para crear gráficos con
vectores, incluyendo curvas, líneas, reglas, y más.

%description -l fr
Ce programme vous offre tout ce dont vous avez besoin pour créer des
graphiques vectoriels, de base à moyennement complexes. Il comprend
les courbes de Bézier, les lignes, les règles etc.

%description -l pl
Program xfig udostêpnia Ci wszystkie narzêdzia grafik wektorowych
sk³adaj±cych siê z prostych i zaawansowanych elementów wektorowych jak
linie, krzywe bezier i wiele innych.

%description -l pt_BR
Este programa oferece tudo o que você precisa para criar gráficos com
vetores, incluindo curvas, linhas, réguas, e mais.

%description -l ru
Xfig - ÜÔÏ ÉÎÓÔÒÕÍÅÎÔ ÄÌÑ ÓÏÚÄÁÎÉÑ ÂÁÚÏ×ÏÊ ×ÅËÔÏÒÎÏÊ ÇÒÁÆÉËÉ, ×ËÌÀÞÁÑ
ËÒÉ×ÙÅ âÅÚØÅ, ÌÉÎÉÉ É ÍÎÏÇÏÅ ÄÒÕÇÏÅ. ðÏÌÕÞÅÎÎÕÀ ÇÒÁÆÉËÕ ÍÏÖÎÏ
ÓÏÈÒÁÎÉÔØ, ÒÁÓÐÅÞÁÔÁÔØ ÎÁ PostScript ÐÒÉÎÔÅÒÁÈ ÉÌÉ ÓËÏÎ×ÅÒÔÉÒÏ×ÁÔØ ×
ÄÒÕÇÉÅ ÆÏÒÍÁÔÙ (ÎÁÐÒÉÍÅÒ, X11 bitmaps, Encapsulated PostScript,
LaTeX).

%description -l tr
Bu program, en temel olanlarýndan ileri düzeydekilere kadar tüm belli
baþlý vektör grafikleri (doðrular, bezier eðrisi vs) çizebilmenize
olanak verir.

%description -l uk
Xfig - ÃÅ ¦ÎÓÔÒÕÍÅÎÔ ÄÌÑ ÓÔ×ÏÒÅÎÎÑ ÂÁÚÏ×Ï§ ×ÅËÔÏÒÎÏ§ ÇÒÁÆ¦ËÉ,
×ËÌÀÞÁÀÞÉ ËÒÉ×¦ âÅÚ'¤, Ì¦Î¦§ ÔÁ ¦ÎÛÅ. ïÔÒÉÍÁÎÕ ÇÒÁÆ¦ËÕ ÍÏÖÎÁ ÚÂÅÒÅÇÔÉ,
ÒÏÚÄÒÕËÕ×ÁÔÉ ÎÁ PostScript ÐÒÉÎÔÅÒÁÈ ÞÉ ÚËÏÎ×ÅÒÔÕ×ÁÔÉ × ¦ÎÛ¦ ÆÏÒÍÁÔÉ
(ÎÁÐÒÉËÌÁÄ, X11 bitmaps, Encapsulated PostScript, LaTeX).

%prep
%setup -q -n %{name}.%{version}-%{_pre}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}" \
	XFIGDOCDIR="%{_docdir}/%{name}-%{version}/"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_pixmapsdir},%{_libdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -ar Libraries $RPM_BUILD_ROOT%{_prefix}/lib/X11/xfig
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/X11/xfig/Libraries/*/README

(
cat $RPM_BUILD_ROOT%{_prefix}/lib/X11/app-defaults/Fig
tail -n +2 $RPM_BUILD_ROOT%{_prefix}/lib/X11/app-defaults/Fig-color
echo 'Fig.inches: off'
) 	> $RPM_BUILD_ROOT%{_prefix}/lib/X11/app-defaults/Fig.new
mv -f $RPM_BUILD_ROOT%{_prefix}/lib/X11/app-defaults/Fig.new \
	$RPM_BUILD_ROOT%{_prefix}/lib/X11/app-defaults/Fig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/html/ Doc/*.html README CHANGES FIGAPPS Doc/TODO Doc/FORMAT*
%attr(755,root,root) %{_bindir}/xfig
%{_prefix}/lib/X11/xfig
%{_prefix}/lib/X11/app-defaults/Fig
%{_prefix}/lib/X11/app-defaults/Fig-color
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_applnkdir}/Graphics/xfig.desktop
