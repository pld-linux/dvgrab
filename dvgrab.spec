Summary:	DV grabbing utility
Summary(pl):	Narzêdzie do zgrywania DV
Name:		dvgrab
Version:	2.1
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/kino/%{name}-%{version}.tar.gz
# Source0-md5:	6793471d7b5c29788371d8102f013306
URL:		http://www.kinodv.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libavc1394-devel
BuildRequires:	libdv-devel
BuildRequires:	libstdc++-devel
BuildRequires:	quicktime4linux-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvgrab is an utility for grabbing video/audio from an
IEEE1394-compliant device as VCR or camcoder.

%description -l pl
dvgrab to narzêdzie do zgrywania obrazu i d¼wiêku z urz±dzeñ
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
