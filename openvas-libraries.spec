%define major 4
%define libname %mklibname openvas %{major}
%define develname %mklibname -d openvas

Name:           openvas-libraries
Version:        4.0.7
Release:        1
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server
License:        LGPLv2+
Group:          System/Libraries
URL:            http://www.openvas.org
Source0:         http://wald.intevation.org/frs/download.php/979/openvas-libraries-%{version}.tar.gz
source1:				.abf.yml
Patch0:		openvas-libraries-4.0.4-build.patch
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  gpgme-devel
BuildRequires:  pkgconfig(uuid)
BuildRequires:	cmake
BuildRequires:	bison
buildrequires:	libgcrypt-devel
Obsoletes:	openvas-libnasl < 3.0.0

%description
openvas-libraries is the base library for the OpenVAS network security scanner.

%package -n %{libname}
Group:		System/Libraries
Summary:        Support libraries for Open Vulnerability Assessment (OpenVAS) Server

%description -n %{libname}
The support libraries for Open Vulnerability Assessment (OpenVAS) Server.

%package -n %{develname}
Summary:	Development files for openvas-libraries
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	openvas-devel = %{version}-%{release}
Obsoletes:	%{_lib}openvas-libnasl-devel < 3.0.0

%description -n %{develname}
This package contains the development files (mainly C header files) for
openvas-libraries.

%prep

%setup -qn openvas-libraries-%{version}
%patch0 -p 1


sed -i -e 's#-Werror##' `grep -rl Werror *|grep CMakeLists.txt`

%build
%cmake -DLOCALSTATEDIR:PATH=%{_var}
%make

%install

%makeinstall_std -C build

find %{buildroot} -name *.a -exec %__rm {} \;

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


%changelog
* Thu Nov 17 2011 Oden Eriksson <oeriksson@mandriva.com> 4.0.6-1mdv2012.0
+ Revision: 731339
- 4.0.6
- various fixes

* Thu Sep 08 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 4.0.5-1
+ Revision: 698890
- 4.0.5

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.0.4-1
+ Revision: 677430
- new version

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 4.0.3-1
+ Revision: 649792
- more patches
- disable weeor
- disable Wall
- New version 4.0.3

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 3.1.4-1mdv2011.0
+ Revision: 602180
- br uuid
- drop old patches
- new version 3.1.4

* Sun Apr 18 2010 Funda Wang <fwang@mandriva.org> 3.0.5-1mdv2010.1
+ Revision: 536368
- New version 3.0.5

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 3.0.0-3mdv2010.1
+ Revision: 480351
- obsoletes openvas-libnasl

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 3.0.0-2mdv2010.1
+ Revision: 480325
- obsoletes old libnasl

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 3.0.0-1mdv2010.1
+ Revision: 480324
- fix BR
- new version 3.0.0

* Wed Aug 19 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.4-1mdv2010.0
+ Revision: 418247
- Update to new version 2.0.4
- Remove Makefile patch (not needed)
- Add patch to link with libgcrypt
- Add patch to fix format string errors

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2009.1
+ Revision: 366567
- import openvas-libraries


