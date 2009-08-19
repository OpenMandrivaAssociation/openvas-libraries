%define major 2
%define libname %mklibname openvas %{major}
%define libhg %mklibname openvas_hg %{major}
%define develname %mklibname -d openvas

Name:           openvas-libraries
Version:        2.0.4
Release:        %mkrel 1
License:        LGPLv2+
Group:          System/Libraries
URL:            http://www.openvas.org
Source:         http://wald.intevation.org/frs/download.php/572/%{name}-%{version}.tar.gz
Patch0:		openvas-libraries-2.0.3-strfmt.patch
Patch1:		openvas-libraries-2.0.3-libs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libpcap-devel glib2-devel gnutls-devel
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server

%description
openvas-libraries is the base library for the OpenVAS network security scanner.

%package -n %{libname}
Group:		System/Libraries
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server

%description -n %{libname}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%package -n %{libhg}
Group:          System/Libraries
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server

%description -n %{libhg}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%package -n %{develname}
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{libhg} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	openvas-devel = %{version}-%{release}
Summary:	Development files for openvas-libraries

%description -n %{develname}
This package contains the development files (mainly C header files) for openvas-libraries.

%prep
%setup -qn openvas-libraries-%{version}
%patch0 -p1 -b .strfmt
%patch1 -p1 -b .libs

%build
autoconf
%configure2_5x --disable-static
%make all

%install
rm -fr %buildroot
%makeinstall_std
find %{buildroot} -name *.la -exec %__rm {} \;

%multiarch_binaries %{buildroot}%{_bindir}/libopenvas-config

%clean
rm -fr %buildroot

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog CHANGES TODO
%{_libdir}/libopenvas.so.%{major}
%{_libdir}/libopenvas.so.%{major}.*

%files -n %{libhg}
%defattr(-,root,root)
%{_libdir}/libopenvas_hg.so.%{major}
%{_libdir}/libopenvas_hg.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/libopenvas-config
%multiarch %{multiarch_bindir}/libopenvas-config
%{_includedir}/openvas
%{_libdir}/libopenvas.so
%{_libdir}/libopenvas_hg.so
%{_mandir}/man1/libopenvas-config.1*
