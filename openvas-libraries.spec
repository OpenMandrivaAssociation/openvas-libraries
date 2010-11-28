%define major 3
%define libname %mklibname openvas %{major}
%define develname %mklibname -d openvas

Name:           openvas-libraries
Version:        3.1.4
Release:        %mkrel 1
License:        LGPLv2+
Group:          System/Libraries
URL:            http://www.openvas.org
Source:         http://wald.intevation.org/frs/download.php/572/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libpcap-devel glib2-devel gnutls-devel gpgme-devel
BuildRequires:	cmake bison
Obsoletes:	openvas-libnasl < 3.0.0
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server

%description
openvas-libraries is the base library for the OpenVAS network security scanner.

%package -n %{libname}
Group:		System/Libraries
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server

%description -n %{libname}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%package -n %{develname}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	openvas-devel = %{version}-%{release}
Obsoletes:	%{_lib}openvas-libnasl-devel < 3.0.0
Summary:	Development files for openvas-libraries

%description -n %{develname}
This package contains the development files (mainly C header files) for openvas-libraries.

%prep
%setup -qn openvas-libraries-%{version}

%build
export CFLAGS="%{optflags} -fPIC"
export CXXPPFLAGS="%{optflags} -fPIC"
%configure2_5x --disable-static
%make

%install
rm -fr %buildroot
%makeinstall_std
find %{buildroot} -name *.la -exec %__rm {} \;
find %{buildroot} -name *.a -exec %__rm {} \;

%multiarch_binaries %{buildroot}%{_bindir}/libopenvas-config

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%{_bindir}/openvas-nasl
%{_mandir}/man1/openvas-nasl.1.*
%{_datadir}/openvas

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog CHANGES TODO
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/libopenvas-config
%multiarch %{multiarch_bindir}/libopenvas-config
%{_includedir}/openvas
%{_libdir}/*.so
%{_mandir}/man1/libopenvas-config.1*
