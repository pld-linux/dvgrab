Summary:	DV grabbing utility
Summary(pl):	Narzêdzie do zgrywania DV
Name:		dvgrab
Version:	1.6
Release:	1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://kino.schirmacher.de/filemanager/download/20/%{name}-%{version}.tar.gz
# Source0-md5:	1bddb6bcda3835d96b96b5c440991114
# Source0-size:	152654
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libavc1394-devel
BuildRequires:	libdv-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvgrab is an utility for grabbing video/audio from an
IEEE1394-compliant device as VCR or camcoder.

%description -l pl
dvgrab to narzêdzie do zgrywania obrazu i d¼wiêku z urz±dzeñ
kompatybilnych z IEEE1394, takich jak magnetowidy czy kamkodery.

%prep
%setup -q -n %{name}-1.5

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
