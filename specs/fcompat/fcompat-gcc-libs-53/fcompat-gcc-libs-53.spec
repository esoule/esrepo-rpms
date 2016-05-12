%global _prefix			/usr/fcompat
%global orig_prefix		/usr
%if %{_lib} == lib64
%global mib			mib64
%else
%global mib			mib
%endif

%define debug_package		%{nil}
%define __strip			/bin/true

%global fc_ver_suffix		53
%global gcc_version		5.3.1
# Note, gcc_release must be integer, if you want to add suffixes to
# %{release}, append them after %{gcc_release} on Release: line.
%global gcc_release		6
%global up_orig_rel		6.fc23
%global src_dir_url		http://fedora.bhs.mirrors.ovh.net/linux/updates/23/x86_64

%global build_libgccjit		0

%global subpkgs_all		libgcc libstdc++ libobjc libgfortran \
				libgomp \
				libquadmath libitm \
				libatomic libasan libubsan libcilkrts \
				libmpx libgnat libgo \
				%{nil}
%ifarch x86_64
%global subpkgs_64		libtsan liblsan
%else
%global subpkgs_64		%{nil}
%endif

%if %{build_libgccjit}
%global subpkgs_libgccjit	libgccjit
%else
%global subpkgs_libgccjit	%{nil}
%endif

Name:           fcompat-gcc-libs-%{fc_ver_suffix}
Version:        %{gcc_version}
Release:        %{gcc_release}.101%{?dist}
Summary:        fcompat: Various compilers (C, C++, Objective-C, Java, ...)

Group:          Development/Languages
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
URL:            http://gcc.gnu.org
Source101:      %{src_dir_url}/l/libasan-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source102:      %{src_dir_url}/l/libatomic-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source103:      %{src_dir_url}/l/libcilkrts-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source104:      %{src_dir_url}/l/libgcc-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source105:      %{src_dir_url}/l/libgccjit-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source106:      %{src_dir_url}/l/libgfortran-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source107:      %{src_dir_url}/l/libgnat-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source108:      %{src_dir_url}/l/libgo-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source109:      %{src_dir_url}/l/libgomp-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source110:      %{src_dir_url}/l/libitm-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source111:      %{src_dir_url}/l/libmpx-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source112:      %{src_dir_url}/l/libobjc-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source113:      %{src_dir_url}/l/libquadmath-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source114:      %{src_dir_url}/l/libstdc++-%{gcc_version}-%{up_orig_rel}.i686.rpm
Source115:      %{src_dir_url}/l/libubsan-%{gcc_version}-%{up_orig_rel}.i686.rpm

Source201:      %{src_dir_url}/l/libasan-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source202:      %{src_dir_url}/l/libatomic-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source203:      %{src_dir_url}/l/libcilkrts-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source204:      %{src_dir_url}/l/libgcc-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source205:      %{src_dir_url}/l/libgccjit-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source206:      %{src_dir_url}/l/libgfortran-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source207:      %{src_dir_url}/l/libgnat-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source208:      %{src_dir_url}/l/libgo-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source209:      %{src_dir_url}/l/libgomp-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source210:      %{src_dir_url}/l/libitm-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source211:      %{src_dir_url}/l/libmpx-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source212:      %{src_dir_url}/l/libobjc-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source213:      %{src_dir_url}/l/libquadmath-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source214:      %{src_dir_url}/l/libstdc++-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source215:      %{src_dir_url}/l/libubsan-%{gcc_version}-%{up_orig_rel}.x86_64.rpm

Source251:      %{src_dir_url}/l/libtsan-%{gcc_version}-%{up_orig_rel}.x86_64.rpm
Source252:      %{src_dir_url}/l/liblsan-%{gcc_version}-%{up_orig_rel}.x86_64.rpm

BuildRequires:  cpio
Requires:       fcompat-filesystem >= 1.0
Requires:       fcompat-glibc-222
Requires:       fcompat-gcc-libgcc-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libstdc++-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libobjc-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libgfortran-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libgomp-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
%if %{build_libgccjit}
Requires:       fcompat-gcc-libgccjit-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
%endif
Requires:       fcompat-gcc-libquadmath-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libitm-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libatomic-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libasan-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libubsan-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libcilkrts-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libmpx-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libgnat-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-libgo-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
%ifarch x86_64
Requires:       fcompat-gcc-libtsan-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
Requires:       fcompat-gcc-liblsan-%{fc_ver_suffix}%{?_isa} = %{version}-%{release}
%endif

%description
The gcc package contains the GNU Compiler Collection version 5.
You'll need this package in order to compile C code.

Binaries (libraries) re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libgcc-%{fc_ver_suffix}
Summary:        fcompat: GCC version 5 shared support library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libgcc-%{fc_ver_suffix}
This package contains GCC shared support library which is needed
e.g. for exception handling support.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libstdc++-%{fc_ver_suffix}
Summary:        fcompat: GNU Standard C++ Library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libstdc++-%{fc_ver_suffix}
The libstdc++ package contains a rewritten standard compliant GCC Standard
C++ Library.


%package -n     fcompat-gcc-libobjc-%{fc_ver_suffix}
Summary:        fcompat: Objective-C runtime
Group:          System Environment/Libraries

%description -n fcompat-gcc-libobjc-%{fc_ver_suffix}
This package contains Objective-C shared library which is needed to run
Objective-C dynamically linked programs.


%package -n     fcompat-gcc-libgfortran-%{fc_ver_suffix}
Summary:        fcompat: Fortran runtime
Group:          System Environment/Libraries

%description -n fcompat-gcc-libgfortran-%{fc_ver_suffix}
This package contains Fortran shared library which is needed to run
Fortran dynamically linked programs.


%package -n     fcompat-gcc-libgomp-%{fc_ver_suffix}
Summary:        fcompat: GCC OpenMP v3.0 shared support library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libgomp-%{fc_ver_suffix}
This package contains GCC shared support library which is needed
for OpenMP v3.0 support.

Binaries re-packaged for use on EL6 in alternate location (fcompat).

%if %{build_libgccjit}
%package -n     fcompat-gcc-libgccjit-%{fc_ver_suffix}
Summary:        fcompat: Library for embedding GCC inside programs and libraries
Group:          System Environment/Libraries

%description -n fcompat-gcc-libgccjit-%{fc_ver_suffix}
This package contains shared library with GCC JIT front-end.

Binaries re-packaged for use on EL6 in alternate location (fcompat).

%endif

%package -n     fcompat-gcc-libquadmath-%{fc_ver_suffix}
Summary:        fcompat: GCC __float128 shared support library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libquadmath-%{fc_ver_suffix}
This package contains GCC shared support library which is needed
for __float128 math support and for Fortran REAL*16 support.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libitm-%{fc_ver_suffix}
Summary:        fcompat: The GNU Transactional Memory library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libitm-%{fc_ver_suffix}
This package contains the GNU Transactional Memory library
which is a GCC transactional memory support runtime library.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libatomic-%{fc_ver_suffix}
Summary:        fcompat: The GNU Atomic library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libatomic-%{fc_ver_suffix}
This package contains the GNU Atomic library
which is a GCC support runtime library for atomic operations not supported
by hardware.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libasan-%{fc_ver_suffix}
Summary:        fcompat: The Address Sanitizer runtime library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libasan-%{fc_ver_suffix}
This package contains the Address Sanitizer library
which is used for -fsanitize=address instrumented programs.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libubsan-%{fc_ver_suffix}
Summary:        fcompat: The Undefined Behavior Sanitizer runtime library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libubsan-%{fc_ver_suffix}
This package contains the Undefined Behavior Sanitizer library
which is used for -fsanitize=undefined instrumented programs.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libcilkrts-%{fc_ver_suffix}
Summary:        fcompat: The Cilk+ runtime library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libcilkrts-%{fc_ver_suffix}
This package contains the Cilk+ runtime library.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libmpx-%{fc_ver_suffix}
Summary:        fcompat: The Memory Protection Extensions runtime libraries
Group:          System Environment/Libraries

%description -n fcompat-gcc-libmpx-%{fc_ver_suffix}
This package contains the Memory Protection Extensions runtime libraries
which is used for -fcheck-pointer-bounds -mmpx instrumented programs.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libgnat-%{fc_ver_suffix}
Summary:        fcompat: GNU Ada 83, 95, 2005 and 2012 runtime shared libraries
Group:          System Environment/Libraries

%description -n fcompat-gcc-libgnat-%{fc_ver_suffix}
GNAT is a GNU Ada 83, 95, 2005 and 2012 front-end to GCC. This package includes
shared libraries, which are required to run programs compiled with the GNAT.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-libgo-%{fc_ver_suffix}
Summary:        fcompat: Go runtime
Group:          System Environment/Libraries

%description -n fcompat-gcc-libgo-%{fc_ver_suffix}
This package contains Go shared library which is needed to run
Go dynamically linked programs.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%ifarch x86_64
%package -n     fcompat-gcc-libtsan-%{fc_ver_suffix}
Summary:        fcompat: The Thread Sanitizer runtime library
Group:          System Environment/Libraries

%description -n fcompat-gcc-libtsan-%{fc_ver_suffix}
This package contains the Thread Sanitizer library
which is used for -fsanitize=thread instrumented programs.

Binaries re-packaged for use on EL6 in alternate location (fcompat).


%package -n     fcompat-gcc-liblsan-%{fc_ver_suffix}
Summary:        fcompat: The Leak Sanitizer runtime library
Group:          System Environment/Libraries

%description -n fcompat-gcc-liblsan-%{fc_ver_suffix}
This package contains the Leak Sanitizer library
which is used for -fsanitize=leak instrumented programs.

Binaries re-packaged for use on EL6 in alternate location (fcompat).

%endif


%prep
%setup -c -T

subpkgs="%{subpkgs_all} %{subpkgs_libgccjit} %{subpkgs_64}"

mkdir t
cd t
for n in ${subpkgs} ; do
	/bin/cat %{_sourcedir}/${n}-%{gcc_version}-%{up_orig_rel}.%{_target_cpu}.rpm | rpm2cpio | cpio -idmv
done
mv usr/share/licenses/libgcc ../licenses-libgcc
mv usr/share/licenses/libquadmath/COPYING.LIB.libquadmath ../

rm -rf usr/share
mv %{_lib}/*.so* usr/%{_lib}/
find . ! -type d | sort
cd ..

%build
true



%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}%{_prefix}

mv t/usr/%{_lib} %{buildroot}%{_libdir}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)


%files -n fcompat-gcc-libgcc-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license licenses-libgcc/COPYING*
%{_libdir}/libgcc_s-%{gcc_version}-*.so.1
%{_libdir}/libgcc_s.so.1


%files -n fcompat-gcc-libstdc++-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libstdc++.so.6*


%files -n fcompat-gcc-libobjc-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libobjc.so.4*


%files -n fcompat-gcc-libgfortran-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libgfortran.so.3*


%files -n fcompat-gcc-libgomp-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libgomp.so.1*
%{_libdir}/libgomp-plugin-host_nonshm.so.1*


%if %{build_libgccjit}
%files -n fcompat-gcc-libgccjit-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libgccjit.so.*

%endif

%files -n fcompat-gcc-libquadmath-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license COPYING.LIB.libquadmath
%{_libdir}/libquadmath.so.0*


%files -n fcompat-gcc-libitm-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libitm.so.1*


%files -n fcompat-gcc-libatomic-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libatomic.so.1*


%files -n fcompat-gcc-libasan-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libasan.so.2*


%files -n fcompat-gcc-libubsan-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libubsan.so.0*


%files -n fcompat-gcc-libcilkrts-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libcilkrts.so.5*


%files -n fcompat-gcc-libmpx-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libmpx.so.0*
%{_libdir}/libmpxwrappers.so.0*


%files -n fcompat-gcc-libgnat-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libgnat-*.so
%{_libdir}/libgnarl-*.so


%files -n fcompat-gcc-libgo-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libgo.so.7*


%ifarch x86_64
%files -n fcompat-gcc-libtsan-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/libtsan.so.0*


%files -n fcompat-gcc-liblsan-%{fc_ver_suffix}
%defattr(-,root,root,-)
%{_libdir}/liblsan.so.0*
%endif


%changelog
