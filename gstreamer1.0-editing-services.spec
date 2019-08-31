%define oname gstreamer-editing-services

%define api 1.0
%define major 0
%define libname %mklibname ges %{api} %{major}
%define devname %mklibname ges %{api} -d
%define girname %mklibname ges-gir %{api}
%define plugname gstreamer%{api}-nle

Summary:	Gstreamer editing services
Name:		gstreamer%{api}-editing-services
Version:	1.16.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/gstreamer/gst-editing-services/
Source0:	http://gstreamer.freedesktop.org/src/%{oname}/%{oname}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:  flex-devel
BuildRequires:	valgrind
BuildRequires:	gettext-devel
BuildRequires:  pkgconfig(gio-2.0) >= 2.16
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-controller-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-pbutils-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-video-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-audio-%{api})
BuildRequires:	pkgconfig(gstreamer-tag-%{api})
BuildRequires:	pkgconfig(gstreamer-base-%{api})
BuildRequires:	gstreamer1.0-plugins-good
BuildRequires:	gstreamer1.0-plugins-base
BuildRequires:	gstreamer1.0-plugins-bad
BuildRequires:	gstreamer1.0-plugins-ugly
BuildRequires:	gstreamer1.0-libav
BuildRequires:	gstreamer1.0-soup
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(gio-2.0)

%description
This is a high-level library for facilitating the creation of audio/video
non-linear editors.

%files
%doc ChangeLog COPYING* README RELEASE NEWS AUTHORS
%{_bindir}/ges-launch-%{api}
%{_datadir}/bash-completion/completions/ges-launch-%{api}
%{_libdir}/gstreamer-1.0/libgstges.so
%{_mandir}/man1/ges-launch-%{api}.1*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Gstreamer editing services shared library
Group:		System/Libraries

%description -n %{libname}
This is a high-level library for facilitating the creation of audio/video
non-linear editors.

%files -n %{libname}
%{_libdir}/libges-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{plugname}
Summary:	GStreamer Non Linear Engine plugin
Group:		Video/Utilities
Obsoletes:	gstreamer1.0-gnonlin < 1.6.0

%description -n %{plugname}
GStreamer Non Linear Engine plugin.

%files -n %{plugname}
%{_libdir}/gstreamer-%{api}/libgstnle.so

#----------------------------------------------------------------------------

%package python
Summary:	Python bindings for %{name}
Group:		Development/Python
Requires:	gstreamer1.0-python

%description python
Python bindings for %{name}.

%files python
%{python2_sitearch}/gstreamer-editing-services/

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	Gstreamer editing services gobject-introspection files
Group:		System/Libraries

%description -n %{girname}
Gstreamer editing services gobject-introspection files.

%files -n %{girname}
%{_libdir}/girepository-1.0/GES-%{api}.typelib

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains libraries and header files for developing applications
that use %{name}.

%files -n %{devname}
%doc docs/
%{_libdir}/libges-%{api}.so
%{_includedir}/gstreamer-%{api}/ges/
%{_libdir}/pkgconfig/gst-editing-services-%{api}.pc
%{_datadir}/gir-1.0/GES-%{api}.gir

#----------------------------------------------------------------------------

%prep
%setup -qn %{oname}-%{version}

%build
%configure --with-gtk=3.0 --disable-examples
%make_build V=1

%install
%make_install

