Summary:	Tools for the Hughski Colorimeter
Name:		colorhug-client
Version:	0.2.1
Release:	2
License:	GPLv2+
Group:		Graphics
Url:		https://www.hughski.com/
Source0:	http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	docbook-to-man
BuildRequires:	docbook-utils
BuildRequires:	pkgconfig(colord)
BuildRequires:	pkgconfig(colord-gtk)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gusb)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libsoup-2.4)

%description
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

%files -f %{name}.lang
%doc README AUTHORS NEWS COPYING
%{_bindir}/colorhug*
%{_datadir}/%{name}
%{_datadir}/help/*/%{name}/
%{_libexecdir}/colorhug*
%{_datadir}/appdata/colorhug-*.appdata.xml
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*.1*
%config %{_sysconfdir}/bash_completion.d/*-completion.bash
%{_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/*/mimetypes/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

