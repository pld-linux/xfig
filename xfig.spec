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
Version:	3.2.5
Release:	2
License:	Freeware
Group:		X11/Applications/Graphics
#Source0Download: http://xfig.org/art15.html
Source0:	http://files.xfig.org/%{name}.%{version}.full.tar.gz
# Source0-md5:	fae0c67a3951bd41c057deb63b6aa47a
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
Patch1:		%{name}-i18n.patch
Patch2:		%{name}-mkstemp.diff
Patch3:		%{name}-debian.patch
URL:		http://www.xfig.org/
BuildRequires:	Xaw3d-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	xorg-cf-files
BuildRequires:	xorg-lib-libXaw-devel
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
%patch3 -p1

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
	XFIGLIBDIR=%{_datadir}/xfig

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a Libraries $RPM_BUILD_ROOT%{_datadir}/xfig
rm -f $RPM_BUILD_ROOT%{_datadir}/xfig/Libraries/*/README

(
cat $RPM_BUILD_ROOT%{_appdefsdir}/Fig
tail -n +2 $RPM_BUILD_ROOT%{_appdefsdir}/Fig-color
echo 'Fig.inches: off'
) 	> $RPM_BUILD_ROOT%{_appdefsdir}/Fig.new
mv -f $RPM_BUILD_ROOT%{_appdefsdir}/Fig.new $RPM_BUILD_ROOT%{_appdefsdir}/Fig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc/html/ Doc/*.html README CHANGES FIGAPPS Doc/TODO Doc/FORMAT*
%attr(755,root,root) %{_bindir}/xfig
%{_datadir}/xfig
%{_appdefsdir}/Fig
%{_appdefsdir}/Fig-color
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
