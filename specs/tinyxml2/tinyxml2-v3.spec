# tinyml2 parses files potentially coming from untrusted sources.
%global         _hardened_build 1

%global         githubparent    leethomason
%global         commit          1977a7258cc66fd4da7f1e9da05a4933646a7803
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         commitdate      20140914
%global         gitversion      .%{commitdate}git%{shortcommit}

%global         origname        tinyxml2

Name:           tinyxml2-v3
Version:        3.0.0
Release:        2.101%{?dist}
Summary:        Simple, small and efficient C++ XML parser

Group:          Development/Libraries
License:        zlib
URL:            https://github.com/%{githubparent}/%{origname}
Source0:        https://github.com/%{githubparent}/%{origname}/archive/%{commit}/%{origname}-%{version}-%{shortcommit}.tar.gz

# EPEL has a too old CMake which is missing GNUInstallDirs (copied from Fedora 19 CMake)
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Source1:        GNUInstallDirs.cmake
Patch0:         tinyxml2-epelbuild.patch

BuildRequires:  cmake
Provides:       %{origname} = %{version}-%{release}
Provides:       %{origname}%{?_isa} = %{version}-%{release}

%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrated into other programs. It uses a Document Object Model
(DOM), meaning the XML data is parsed into a C++ objects that can be
browsed and manipulated, and then written to disk or another output stream.

TinyXML-2 doesn't parse or use DTDs (Document Type Definitions) nor XSLs
(eXtensible Stylesheet Language).

TinyXML-2 uses a similar API to TinyXML-1, But the implementation of the
parser was completely re-written to make it more appropriate for use in a
game. It uses less memory, is faster, and uses far fewer memory allocations.

%package devel
Summary:        Development files for %{origname}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{origname}%{?_isa} = %{version}-%{release}
Provides:       %{origname}-devel = %{version}-%{release}
Provides:       %{origname}-devel%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with the %{origname} library.

%prep
%setup -q -n %{origname}-%{commit}
chmod -c -x *.cpp *.h
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
%patch0 -p1 -b .epel
cp -p %{SOURCE1} .
%endif

%build
mkdir objdir
cd objdir
%cmake .. -DBUILD_STATIC_LIBS=OFF
make %{?_smp_mflags}

%check
cd objdir
export LD_LIBRARY_PATH=`pwd`
./xmltest

%install
rm -rf %{buildroot}
cd objdir
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc readme.md
%{_libdir}/lib%{origname}.so.%{version}
%{_libdir}/lib%{origname}.so.3

%files devel
%{_includedir}/%{origname}.h
%{_libdir}/lib%{origname}.so
%{_libdir}/pkgconfig/%{origname}.pc

%changelog
* Mon Mar 06 2017 Evgueni Souleimanov <esoule@100500.ca> - 3.0.0-2.101
- Re-enable tests
- Rebuild as package name tinyxml2-v3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 21 2016 Rich Mattes <richmattes@gmail.com> - 3.0.0-1
- Update to release 3.0.0 (rhbz#1202166)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4.20140914git5321a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3.20140914git5321a0e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-2.20140914git5321a0e
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 05 2015 François Cami <fcami@fedoraproject.org> - 2.2.0-1.20140914git5321a0e
- Update to 2.2.0.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4.20140406git6ee53e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3.20140406git6ee53e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 François Cami <fcami@fedoraproject.org> - 2.1.0-2.20140406git6ee53e7
- Bump release and make it build (switch GNUInstallDirs.cmake from sources to git).

* Sat May 17 2014 François Cami <fcami@fedoraproject.org> - 2.1.0-1.20140406git6ee53e7
- Update to 2.1.0.

* Mon Oct 14 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.11-4.20130805git0323851
- Patch to build in EPEL branches.

* Mon Aug 12 2013 François Cami <fcami@fedoraproject.org> - 1.0.11-3.20130805git0323851
- Fixes by Susi Lehtola: build in a separate directory and don't build anything static.

* Mon Aug 12 2013 François Cami <fcami@fedoraproject.org> - 1.0.11-2.20130805git0323851
- Fixes suggested by Ville Skyttä: drop -static, add check, etc.

* Sat Aug 10 2013 François Cami <fcami@fedoraproject.org> - 1.0.11-1.20130805git0323851
- Initial package.

