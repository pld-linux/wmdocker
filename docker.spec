Summary:	A docking application
Summary(pl):	Program dokuj±cy
Name:		docker
Version:	1.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://icculus.org/openbox/docker/%{name}-%{version}.tar.gz
# Source0-md5:	349320bebd43babb8b43e11c7aae0293
Patch0:		%{name}-fix.patch
URL:		http://icculus.org/openbox/docker
BuildRequires:	XFree86-devel
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Docker is a docking application which acts as a system tray for KDE3
and GNOME2. It can be used to replace the panel in either environment,
allowing you to have a system tray without running the KDE/GNOME
panel.

%description -l pl
Docker jest programem dokuj±cym, dzia³aj±cym tak samo jak zasobnik
systemowy dla KDE3 i GNOME2. Mo¿e byæ u¿ywany w otoczeniu
jakiegokolwiek innego ¶rodowiska, umo¿liwiaj±c tym samym posiadanie
zasobnika systemowego bez uruchamiania paneli KDE/GNOME.

%prep
%setup -q

%build
%{__make} CFLAGS="-pedantic -Wall -W %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -c %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
