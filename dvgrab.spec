Summary:	DV grabbing utility
Summary(pl):	Narz�dzie do zgrywania DV
Name:		dvgrab
Version:	1.2
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://kino.schirmacher.de/filemanager/download/8/%{name}-%{version}.tar.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dvgrab is an utility for grabbing video/audio from an
IEEE1394-compliant device as VCR or camcoder.

%description -l pl
dvgrab to narz�dzie do zgrywania obrazu i d�wi�ku z urz�dze�
kompatybilnych z IEEE1394, takich jak VCR czy kamkodery.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
