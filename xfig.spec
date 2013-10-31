Summary:	X11 drawing tool
Summary(de.UTF-8):	X11-Zeichen-Tool
Summary(es.UTF-8):	Herramienta para diseño X11
Summary(fr.UTF-8):	Outil de dessin sous X11
Summary(pl.UTF-8):	Program do rysowania pod X11
Summary(pt_BR.UTF-8):	Ferramenta para desenho X11
Summary(ru.UTF-8):	Инструмент для рисования простой векторной графики
Summary(tr.UTF-8):	X11 çizim aracı
Summary(uk.UTF-8):	Інструмент для малювання простої векторної графіки
Name:		xfig
Version:	3.2.5c
Release:	1
License:	Freeware
Group:		X11/Applications/Graphics
#Source0Download: http://xfig.org/art15.html
#Source0:	http://files.xfig.org/%{name}.%{version}.full.tar.gz
Source0:	http://downloads.sourceforge.net/mcj/%{name}.%{version}.full.tar.gz
# Source0-md5:	210851330fa4bb3581bec1f8448a4db8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-i18n.patch
Patch2:		38_formatstring.patch

Patch5:		%{name}-3.2.5b-zoom-during-edit.patch
Patch6:		%{name}-3.2.5b-urwfonts.patch

Patch8:		%{name}-3.2.5b-pdfimport_mediabox.patch
Patch9:		%{name}-3.2.5b-papersize_b1.patch
Patch10:	%{name}-3.2.5b-network_images.patch
Patch11:	%{name}-3.2.5b-mkstemp.patch

Patch13:	%{name}-3.2.5b-app-defaults.patch
URL:		http://www.xfig.org/
BuildRequires:	Xaw3d-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-util-gccmakedep
BuildRequires:	xorg-util-imake
Requires:	netpbm-progs
Requires:	transfig >= 3.2.4-3
Requires:	xorg-lib-libXt >= 1.0.0
Obsoletes:	xfig-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	%{_datadir}/X11/app-defaults

%description
This program gives you all the features you need to create basic- to
intermediate-level vector graphics, including Bezier curves, lines,
rulers, and more.

%description -l de.UTF-8
Dieses Programm bietet sämtliche Funktionen, die Sie zum Erstellen von
elementaren und fortgeschrittenen Vektorgrafiken benötigen,
einschließlich Bezier-Kurven, Linien, Lineale und anderes.

%description -l es.UTF-8
Este programa ofrece todo lo que necesitas para crear gráficos con
vectores, incluyendo curvas, líneas, reglas, y más.

%description -l fr.UTF-8
Ce programme vous offre tout ce dont vous avez besoin pour créer des
graphiques vectoriels, de base à moyennement complexes. Il comprend
les courbes de Bézier, les lignes, les règles etc.

%description -l pl.UTF-8
Program xfig udostępnia wszystkie możliwości potrzebne do tworzenia
prostych i średniozaawansowanych grafik wektorowych składających się z
linie, krzywych Beziera i podobnych elementów.

%description -l pt_BR.UTF-8
Este programa oferece tudo o que você precisa para criar gráficos com
vetores, incluindo curvas, linhas, réguas, e mais.

%description -l ru.UTF-8
Xfig - это инструмент для создания базовой векторной графики, включая
кривые Безье, линии и многое другое. Полученную графику можно
сохранить, распечатать на PostScript принтерах или сконвертировать в
другие форматы (например, X11 bitmaps, Encapsulated PostScript,
LaTeX).

%description -l tr.UTF-8
Bu program, en temel olanlarından ileri düzeydekilere kadar tüm belli
başlı vektör grafikleri (doğrular, bezier eğrisi vs) çizebilmenize
olanak verir.

%description -l uk.UTF-8
Xfig - це інструмент для створення базової векторної графіки,
включаючи криві Без'є, лінії та інше. Отриману графіку можна зберегти,
роздрукувати на PostScript принтерах чи зконвертувати в інші формати
(наприклад, X11 bitmaps, Encapsulated PostScript, LaTeX).

%prep
%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%patch5 -p2
%patch6 -p0

%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p0

%patch13 -p0

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	LOCAL_LDFLAGS="%{rpmldflags}" \
	XFIGLIBDIR=%{_datadir}/xfig \
	XFIGDOCDIR=%{_docdir}/%{name}-%{version} \
	XPMINC="-I/usr/include/X11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_libdir}}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	CONFDIR=%{_datadir}/X11 \
	MANPATH=%{_mandir} \
	MANSUFFIX="1" \
	XFIGLIBDIR=%{_datadir}/xfig

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a Libraries $RPM_BUILD_ROOT%{_datadir}/xfig
%{__rm} $RPM_BUILD_ROOT%{_datadir}/xfig/Libraries/*/README

(
cat $RPM_BUILD_ROOT%{_appdefsdir}/Fig
echo 'Fig.inches: off'
) 	> $RPM_BUILD_ROOT%{_appdefsdir}/Fig.new
mv -f $RPM_BUILD_ROOT%{_appdefsdir}/Fig.new $RPM_BUILD_ROOT%{_appdefsdir}/Fig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/html/ README CHANGES FIGAPPS Doc/TODO Doc/FORMAT*
%attr(755,root,root) %{_bindir}/xfig
# top dir belongs to transfig, which is required by xfig
%{_datadir}/xfig/CompKeyDB
%{_datadir}/xfig/Libraries
%{_appdefsdir}/Fig
#%{_appdefsdir}/Fig-color
%{_mandir}/man1/xfig.1*
%{_pixmapsdir}/xfig.png
%{_desktopdir}/xfig.desktop
