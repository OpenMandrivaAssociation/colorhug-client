Summary:   Tools for the Hughski Colorimeter
Name:      colorhug-client
Version:   0.1.2
Release:   1
License:   GPLv2+
Group:     Graphics
URL:       http://www.hughski.com/
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz

BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: gtk+3-devel
BuildRequires: intltool
BuildRequires: libgusb-devel >= 0.1.2
BuildRequires: colord-devel >= 0.1.15
BuildRequires: lcms2-devel
BuildRequires: libsoup-devel
BuildRequires: docbook-utils
BuildRequires: docbook-to-man

%description
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

%prep
%setup -q

%build
%configure --disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS NEWS COPYING
%dir %{_datadir}/colorhug-client
%{_datadir}/colorhug-client
%{_libexecdir}/colorhug*
%{_bindir}/colorhug*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/colorhug.png
%{_datadir}/icons/hicolor/scalable/apps/colorhug.svg
%{_mandir}/man1/*.1*
%config %{_sysconfdir}/bash_completion.d/*-completion.bash
