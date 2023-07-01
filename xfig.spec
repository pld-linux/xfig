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
Version:	3.2.8b
Release:	1
License:	Freeware
Group:		X11/Applications/Graphics
Source0:	https://downloads.sourceforge.net/mcj/%{name}-%{version}.tar.xz
# Source0-md5:	049dcf9dc53d6bb7012e716d15d0d512
Patch0:		%{name}-i18n.patch
Patch1:		%{name}-3.2.5b-zoom-during-edit.patch
Patch2:		%{name}-3.2.5b-urwfonts.patch
Patch3:		%{name}-3.2.5b-app-defaults.patch
Patch4:		%{name}-desktop.patch
URL:		https://mcj.sourceforge.net/
BuildRequires:	Xaw3d-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
Requires:	fig2dev >= 3.2.6
Requires:	netpbm-progs
Requires:	xorg-lib-libXt >= 1.0.0
Obsoletes:	xfig-doc < 3.2.3d-6
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
%setup -q
%patch0 -p1
%patch1 -p2
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a Libraries $RPM_BUILD_ROOT%{_datadir}/xfig
%{__rm} $RPM_BUILD_ROOT%{_datadir}/xfig/Libraries/*/README

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/xfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES FIGAPPS README doc/{FORMAT*,TODO,html}
%attr(755,root,root) %{_bindir}/xfig
%{_datadir}/xfig
%{_appdefsdir}/Fig
%{_mandir}/man1/xfig.1*
%{_pixmapsdir}/xfig.png
%{_desktopdir}/xfig.desktop
