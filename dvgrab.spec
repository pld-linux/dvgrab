Summary:	DV grabbing utility
Summary(pl):	Narzêdzie do zgrywania DV
Name:		dvgrab
Version:	1.5
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://kino.schirmacher.de/filemanager/download/20/%{name}-%{version}.tar.gz
# Source0-md5:	1bddb6bcda3835d96b96b5c440991114
BuildRequires:	libavc1394-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvgrab is an utility for grabbing video/audio from an
IEEE1394-compliant device as VCR or camcoder.

%description -l pl
dvgrab to narzêdzie do zgrywania obrazu i d¼wiêku z urz±dzeñ
kompatybilnych z IEEE1394, takich jak VCR czy kamkodery.

%prep
%setup -q

%build
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
