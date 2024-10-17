%define major 8
%define libbase %mklibname openvas_base %{major}
%define libhg %mklibname openvas_hg %{major}
%define libmisc %mklibname openvas_misc %{major}
%define libnasl %mklibname openvas_nasl %{major}
%define libomp %mklibname openvas_omp %{major}
%define devname %mklibname openvas -d

Summary:	Support libraries for Open Vulnerability Assessment (OpenVAS) Server
Name:		openvas-libraries
Version:	8.0.4
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.openvas.org
Source0:	http://wald.intevation.org/frs/download.php/2125/%{name}-%{version}.tar.gz
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	gpgme-devel
BuildRequires:  libksba-devel
BuildRequires:  pcap-devel
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  hiredis-devel

Obsoletes:	openvas-libnasl < 3.0.0

%description
openvas-libraries is the base library for the OpenVAS network security scanner.

%files
%{_bindir}/openvas-nasl
%{_mandir}/man1/openvas-nasl.1.*
%{_datadir}/openvas

#----------------------------------------------------------------------------

%package -n %{libbase}
Summary:	Support libraries for Open Vulnerability Assessment (OpenVAS) Server
Group:		System/Libraries
Conflicts:	%{_lib}openvas4 < 4.0.7-2
Obsoletes:	%{_lib}openvas4 < 4.0.7-2

%description -n %{libbase}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%files -n %{libbase}
%doc ChangeLog CHANGES
%{_libdir}/libopenvas_base.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libhg}
Summary:	Support libraries for Open Vulnerability Assessment (OpenVAS) Server
Group:		System/Libraries
Conflicts:	%{_lib}openvas4 < 4.0.7-2

%description -n %{libhg}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%files -n %{libhg}
%{_libdir}/libopenvas_hg.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libmisc}
Summary:	Support libraries for Open Vulnerability Assessment (OpenVAS) Server
Group:		System/Libraries
Conflicts:	%{_lib}openvas4 < 4.0.7-2

%description -n %{libmisc}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%files -n %{libmisc}
%{_libdir}/libopenvas_misc.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libnasl}
Summary:	Support libraries for Open Vulnerability Assessment (OpenVAS) Server
Group:		System/Libraries
Conflicts:	%{_lib}openvas4 < 4.0.7-2

%description -n %{libnasl}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%files -n %{libnasl}
%{_libdir}/libopenvas_nasl.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libomp}
Summary:	Support libraries for Open Vulnerability Assessment (OpenVAS) Server
Group:		System/Libraries
Conflicts:	%{_lib}openvas4 < 4.0.7-2

%description -n %{libomp}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%files -n %{libomp}
%{_libdir}/libopenvas_omp.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for openvas-libraries
Group:		Development/C
Requires:	%{libbase} = %{EVRD}
Requires:	%{libhg} = %{EVRD}
Requires:	%{libmisc} = %{EVRD}
Requires:	%{libnasl} = %{EVRD}
Requires:	%{libomp} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	openvas-devel = %{EVRD}
Obsoletes:	%{_lib}openvas-libnasl-devel < 3.0.0

%description -n %{devname}
This package contains the development files (mainly C header files) for
openvas-libraries.

%files -n %{devname}
%{_includedir}/openvas
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

sed -i -e 's#-Werror##' `grep -rl Werror *|grep CMakeLists.txt`

%build
%cmake -DLOCALSTATEDIR:PATH=%{_var} -DBUILD_WITH_LDAP=ON
%make

%install
%makeinstall_std -C build

find %{buildroot} -name *.a -exec rm {} \;

