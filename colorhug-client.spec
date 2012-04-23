%define major 1
%define libname %mklibname colorhug %{major}
%define develname %mklibname colorhug -d

Summary:   Tools for the Hughski Colorimeter
Name:      colorhug-client
Version:   0.1.8
Release:   1
License:   GPLv2+
Group:     Graphics
URL:       http://www.hughski.com/
Source0:   http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
Patch0:    colorhug-client-0.1.7-mdv-linkage.patch

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
BuildRequires: gobject-introspection-devel

%description
The Hughski ColorHug colorimeter is a low cost open-source hardware
sensor used to calibrate screens.

This package includes the client tools which allows the user to upgrade
the firmware on the sensor or to access the sensor from command line
scripts.

%package -n %{libname}
Summary: ColorHug client shared libraries
Group:   System/Libraries

%description -n %{libname}
This package contains shared libraries for colorhug-client.

%package -n %{develname}
Summary: ColorHug client development files
Group:   System/Libraries
Requires: %{libname} = %{version}

%description -n %{develname}
This package contains development files for colorhug-client.


%prep
%setup -q
#patch0 -p1
#autoreconf

%build
%configure --disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README AUTHORS NEWS COPYING
%{_datadir}/colorhug-client
%{_libexecdir}/colorhug*
%{_bindir}/colorhug*
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*.1*
%config %{_sysconfdir}/bash_completion.d/*-completion.bash
%{_datadir}/glib-2.0/schemas/com.hughski.colorhug-client.gschema.xml
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/*/mimetypes/*

%files -n %{libname}
%{_libdir}/libcolorhug.so.%{major}*

%files -n %{develname}
%{_includedir}/libcolorhug/
%{_libdir}/girepository-1.0/ColorHug-1.0.typelib
%{_libdir}/libcolorhug.so
%{_libdir}/pkgconfig/colorhug.pc
%{_datadir}/gir-1.0/ColorHug-1.0.gir
