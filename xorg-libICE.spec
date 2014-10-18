Summary:	Inter Client Exchange library
Name:		xorg-libICE
Version:	1.0.9
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libICE-%{version}.tar.bz2
# Source0-md5:	addfb1e897ca8079531669c7c7711726
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-proto >= 7.6
BuildRequires:	xorg-util-macros
BuildRequires:	xorg-xtrans-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inter Client Exchange library.

%package devel
Summary:	Header files for libICE library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto >= 7.6

%description devel
Inter Client Exchange library.

This package contains the header files needed to develop programs that
use libICE.

%prep
%setup -qn libICE-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--enable-specs=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libICE.so.?
%attr(755,root,root) %{_libdir}/libICE.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libICE.so
%dir %{_includedir}/X11/ICE
%{_includedir}/X11/ICE/*.h
%{_pkgconfigdir}/ice.pc

