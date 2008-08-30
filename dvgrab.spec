Summary:	DV grabbing utility
Summary(pl.UTF-8):	Narzędzie do zgrywania DV
Name:		dvgrab
Version:	3.2
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/kino/%{name}-%{version}.tar.gz
# Source0-md5:	3c2af59a3b8b76473b557adf4793cebd
URL:		http://www.kinodv.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libavc1394-devel
BuildRequires:	libdv-devel
BuildRequires:	libiec61883-devel
BuildRequires:	libstdc++-devel
BuildRequires:	quicktime4linux-devel
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
%{__automake}
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
