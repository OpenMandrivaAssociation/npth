%define major 0
%define oldlibname %mklibname %{name} 0
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d

Summary:	New Portable Threads Library
Name:		npth
Version:	1.6
Release:	6
License:	LGPLv2+
Group:		System/Libraries
Url:		git://git.gnupg.org/npth.git
Source0:	https://www.gnupg.org/ftp/gcrypt/npth/%{name}-%{version}.tar.bz2

%description
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth.  It has been designed as a replacement of
GNU Pth for non-ancient operating systems.  In contrast to GNU Pth is is
based on the system's standard threads implementation.

%package -n %{libname}
Summary:	New Portable Threads Library
Group:		System/Libraries
%rename %{oldlibname}

%description -n %{libname}
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth.  It has been designed as a replacement of
GNU Pth for non-ancient operating systems.  In contrast to GNU Pth is is
based on the system's standard threads implementation.

This package provides the main %{name} library.

%package -n %{devname}
Summary:	New Portable Threads Library (Headers and Static Libs)
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
nPth is a non-preemptive threads implementation using an API very similar
to the one known from GNU Pth.  It has been designed as a replacement of
GNU Pth for non-ancient operating systems.  In contrast to GNU Pth is is
based on the system's standard threads implementation.

This package provides all necessary files to develop or compile any
applications or libraries that use %{name} library.

%prep
%autosetup -p1

%build
%configure
%make_build

%if ! %{cross_compiling}
%check
%make check
%endif

%install
%make_install

%files -n %{libname}
%{_libdir}/libnpth.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS README
%{_bindir}/npth-config
%{_datadir}/aclocal/npth.m4
%{_includedir}/npth.h
%{_libdir}/libnpth.so
