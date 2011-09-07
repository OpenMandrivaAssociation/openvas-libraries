%define major 4
%define libname %mklibname openvas %{major}
%define develname %mklibname -d openvas

Name:           openvas-libraries
Version:        4.0.5
Release:        %mkrel 1
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server
License:        LGPLv2+
Group:          System/Libraries
URL:            http://www.openvas.org
Source:         http://wald.intevation.org/frs/download.php/572/%{name}-%{version}.tar.gz
Patch0:		openvas-libraries-4.0.4-build.patch
BuildRequires:  libpcap-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gpgme-devel
BuildRequires:  libuuid-devel
BuildRequires:	cmake
BuildRequires:	bison
Obsoletes:	openvas-libnasl < 3.0.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%patch0 -p 1

sed -i -e 's#-Werror##' `grep -rl Werror *|grep CMakeLists.txt`

%build
%cmake
%make

%install
rm -fr %buildroot
%makeinstall_std -C build
find %{buildroot} -name *.la -exec %__rm {} \;
find %{buildroot} -name *.a -exec %__rm {} \;

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%{_bindir}/openvas-nasl
%{_mandir}/man1/openvas-nasl.1.*
%{_datadir}/openvas

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog CHANGES
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/openvas
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
