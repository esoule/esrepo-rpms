%global _prefix			/usr/fcompat
%global orig_prefix		/usr
%if %{_lib} == lib64
%global mib			mib64
%else
%global mib			mib
%endif

%define debug_package		%{nil}
%define __strip			/bin/true

%define glibcversion		2.22
%define glibcrelease		15.101%{?dist}
%define glibc_orig_release	15.fc23


Name:           fcompat-glibc-222
Epoch:          1
Version:        %{glibcversion}
Release:        %{glibcrelease}
Summary:        fcompat: The GNU libc libraries

Group:          System Environment/Libraries
License:        LGPLv2+ and LGPLv2+ with exceptions and GPLv2+
URL:            http://www.gnu.org/software/glibc/
Source101:      http://fedora.bhs.mirrors.ovh.net/linux/updates/23/x86_64/g/glibc-%{glibcversion}-%{glibc_orig_release}.i686.rpm
Source102:      http://fedora.bhs.mirrors.ovh.net/linux/updates/23/x86_64/g/glibc-%{glibcversion}-%{glibc_orig_release}.x86_64.rpm

BuildRequires:  cpio
Requires:       fcompat-filesystem >= 1.0

%description
The glibc package contains standard libraries which are used by
multiple programs on the system. In order to save disk space and
memory, as well as to make upgrading easier, common system code is
kept in one place and shared between programs. This particular package
contains the most important sets of shared libraries: the standard C
library and the standard math library. Without these two libraries, a
Linux system will not function.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%prep
%setup -c -T

mkdir t
cd t
/bin/cat %{_sourcedir}/glibc-%{glibcversion}-%{glibc_orig_release}.%{_target_cpu}.rpm | rpm2cpio | cpio -idmv

mv usr/share/licenses/glibc/* ../
rm -rf etc sbin var usr/libexec usr/sbin usr/share
rm -rf usr/%{_lib}/audit usr/%{_lib}/gconv
cd ..


%build
true


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_prefix}
mv t/%{_lib} %{buildroot}%{_libdir}
mv t/usr/%{_lib}/*.so %{buildroot}%{_libdir}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.LIB LICENSES
%dir %{_libdir}/rtkaio
%{_libdir}/*.so.*
%{_libdir}/*.so
%{_libdir}/rtkaio/*.so.*
%{_libdir}/rtkaio/*.so
%ifarch i686
%dir %{_libdir}/i686
%dir %{_libdir}/i686/nosegneg
%dir %{_libdir}/rtkaio/i686
%dir %{_libdir}/rtkaio/i686/nosegneg
%{_libdir}/i686/nosegneg/*.so.*
%{_libdir}/i686/nosegneg/*.so
%{_libdir}/rtkaio/i686/nosegneg/*.so.*
%{_libdir}/rtkaio/i686/nosegneg/*.so
%endif

%changelog
* Wed May 11 2016 Evgueni Souleimanov <esoule@100500.ca> - 2.22-15.101
- Initial package, on EL6
