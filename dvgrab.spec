Summary:	DV grabbing utility
Summary(pl.UTF-8):	Narzędzie do zgrywania DV
Name:		dvgrab
Version:	3.5
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	https://downloads.sourceforge.net/kino/%{name}-%{version}.tar.gz
# Source0-md5:	b39a242ce63e80fc347ab59931f75649
URL:		https://www.kinodv.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libavc1394-devel >= 0.5.1
BuildRequires:	libdv-devel >= 0.103
BuildRequires:	libiec61883-devel >= 1.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libquicktime-devel >= 0.9.5
BuildRequires:	libraw1394-devel >= 1.1.0
BuildRequires:	libstdc++-devel
BuildRequires:	linux-libc-headers >= 2.6
BuildRequires:	pkgconfig
Requires:	libavc1394 >= 0.5.1
Requires:	libdv >= 0.103
Requires:	libiec61883 >= 1.0.0
Requires:	libquicktime >= 0.9.5
Requires:	libraw1394 >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvgrab is an utility for grabbing video/audio from an
IEEE1394-compliant device as VCR or camcoder.

%description -l pl.UTF-8
dvgrab to narzędzie do zgrywania obrazu i dźwięku z urządzeń
kompatybilnych z IEEE1394, takich jak magnetowidy czy kamkodery.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -Wno-narrowing"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
