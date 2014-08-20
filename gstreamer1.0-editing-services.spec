%define oname gstreamer-editing-services

%define api 1.0
%define major 0
%define libname %mklibname ges %{api} %{major}
%define devname %mklibname ges %{api} -d
%define girname %mklibname ges-gir %{api}

Summary:	Gstreamer editing services
Name:		gstreamer%{api}-editing-services
Version:	1.2.1
Release:	2
License:	GPLv2+ and LGPLv2+
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/gstreamer/gst-editing-services/
Source0:	http://gstreamer.freedesktop.org/src/%{oname}/%{oname}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	valgrind
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires: 	pkgconfig(gio-2.0) >= 2.16
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-controller-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-pbutils-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(gstreamer-video-%{api}) >= 1.2.0
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
Requires:	python-gstreamer%{api}

%description
This is a high-level library for facilitating the creation of audio/video
non-linear editors.

%files
%doc ChangeLog COPYING* README RELEASE NEWS AUTHORS
%{_bindir}/ges-launch-%{api}

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
make %{?_smp_mflags} CFLAGS="-Wall -Wdeclaration-after-statement -Wvla -Wpointer-arith -Wmissing-declarations -Wmissing-prototypes -Wredundant-decls -Wundef -Wwrite-strings -Wformat-nonliteral -Wformat-security -Wold-style-definition -Winit-self -Wmissing-include-dirs -Waddress -Waggregate-return -Wno-multichar -Wnested-externs" CXXFLAGS="-Wall" V=1
find . -name '.gitignore' | xargs rm -f

%install
%makeinstall_std
