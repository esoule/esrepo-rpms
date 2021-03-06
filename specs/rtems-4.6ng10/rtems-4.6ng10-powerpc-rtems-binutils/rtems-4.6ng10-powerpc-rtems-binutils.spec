#
# Please send bugfixes or comments to
# 	http://www.rtems.org/bugzilla
#

%define _prefix                 /opt/rtems-4.6ng10
%define _exec_prefix            %{_prefix}
%define _bindir                 %{_exec_prefix}/bin
%define _sbindir                %{_exec_prefix}/sbin
%define _libexecdir             %{_exec_prefix}/libexec
%define _datarootdir            %{_prefix}/share
%define _datadir                %{_datarootdir}
%define _sysconfdir             %{_prefix}/etc
%define _sharedstatedir         %{_prefix}/com
%define _localstatedir          %{_prefix}/var
%define _includedir             %{_prefix}/include
%define _libdir                 %{_exec_prefix}/%{_lib}
%define _mandir                 %{_prefix}/man
%define _infodir                %{_prefix}/info
%define _localedir              %{_datarootdir}/locale

%ifos cygwin cygwin32 mingw mingw32
%define _exeext .exe
%define debug_package           %{nil}
%define _libdir                 %{_exec_prefix}/lib
%else
%define _exeext %{nil}
%endif

%ifos cygwin cygwin32
%define optflags -O3 -pipe -march=i486 -funroll-loops
%endif

%ifos mingw mingw32
%if %{defined _mingw32_cflags}
%define optflags %{_mingw32_cflags}
%else
%define optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -mms-bitfields
%endif
%endif

%if "%{_build}" != "%{_host}"
%define _host_rpmprefix %{_host}-
%else
%define _host_rpmprefix %{nil}
%endif

%{?!el5:%global _with_noarch_subpackages 1}
%define binutils_pkgvers 2.24
%define binutils_version 2.24
%define binutils_rpmvers %{expand:%(echo "2.24" | tr - _ )}

Name:		rtems-4.6ng10-powerpc-rtems-binutils
Summary:	Binutils for target powerpc-rtems
Group:		Development/Tools
Version:	%{binutils_rpmvers}
Release:	9.1.2%{?dist}
License:	GPL/LGPL
URL: 		http://sourceware.org/binutils
%{?el5:BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}

BuildRequires:	%{_host_rpmprefix}gcc

%if "%{binutils_version}" >= "2.18"
# Bug in bfd: Doesn't build without texinfo installed
BuildRequires:	%{?suse:makeinfo}%{!?suse:texinfo} >= 4.2
%else
# Required for building the infos
BuildRequires:	/sbin/install-info
BuildRequires:	%{?suse:makeinfo}%{!?suse:texinfo} >= 4.2
%endif
BuildRequires:	flex
BuildRequires:	bison

Requires:	rtems-4.6ng10-binutils-common

Source0: ftp://ftp.gnu.org/gnu/binutils/binutils-%{binutils_pkgvers}.tar.bz2
%if "%{binutils_version}" == "2.23.2"
Patch0:  ftp://ftp.rtems.org/pub/rtems/SOURCES/4.11/binutils-2.23.2-rtems4.11-20130326.diff
%endif

%description
Cross binutils for target powerpc-rtems
%prep
%setup -q -c -T -n %{name}-%{version}

%setup -q -D -T -n %{name}-%{version} -a0
cd binutils-%{binutils_pkgvers}
%{?PATCH0:%patch0 -p1}
cd ..

%build
  export PATH="%{_bindir}:${PATH}"
  mkdir -p build
  cd build
%if "%{_build}" != "%{_host}"
  CFLAGS_FOR_BUILD="-g -O2 -Wall" \
%endif
  CFLAGS="$RPM_OPT_FLAGS" \
  ../binutils-%{binutils_pkgvers}/configure \
    --build=%_build --host=%_host \
    --target=powerpc-rtems \
    --verbose --disable-nls \
    --without-included-gettext \
    --disable-win32-registry \
    --disable-werror \
    --prefix=%{_prefix} --bindir=%{_bindir} \
    --exec-prefix=%{_exec_prefix} \
    --includedir=%{_includedir} --libdir=%{_libdir} \
    --mandir=%{_mandir} --infodir=%{_infodir}

  make %{?_smp_mflags} all
  make info
  cd ..

%install
  export PATH="%{_bindir}:${PATH}"
  rm -rf $RPM_BUILD_ROOT

  cd build
  make DESTDIR=$RPM_BUILD_ROOT install

  make prefix=$RPM_BUILD_ROOT%{_prefix} \
    bindir=$RPM_BUILD_ROOT%{_bindir} \
    includedir=$RPM_BUILD_ROOT%{_includedir} \
    libdir=$RPM_BUILD_ROOT%{_libdir} \
    infodir=$RPM_BUILD_ROOT%{_infodir} \
    mandir=$RPM_BUILD_ROOT%{_mandir} \
    exec_prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
    install-info

# Dropped in FSF-binutils-2.9.5, but Cygwin still ships it.
  rm -rf $RPM_BUILD_ROOT%{_infodir}/configure.info*

  rm -f $RPM_BUILD_ROOT%{_infodir}/dir
  touch $RPM_BUILD_ROOT%{_infodir}/dir

# binutils does not install share/locale, however it uses it
  mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/locale

# We don't ship host files
  rm -f ${RPM_BUILD_ROOT}%{_libdir}/libiberty*

# manpages without corresponding tools
  if test ! -f ${RPM_BUILD_ROOT}%{_bindir}/powerpc-rtems-dlltool%{_exeext}; then
    rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/powerpc-rtems-dlltool*
  fi
  if test ! -f ${RPM_BUILD_ROOT}%{_bindir}/powerpc-rtems-nlmconv%{_exeext}; then
    rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/powerpc-rtems-nlmconv*
  fi
  if test ! -f ${RPM_BUILD_ROOT}%{_bindir}/powerpc-rtems-windres%{_exeext}; then
    rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/powerpc-rtems-windres*
  fi
  if test ! -f ${RPM_BUILD_ROOT}%{_bindir}/powerpc-rtems-windmc%{_exeext}; then
    rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/powerpc-rtems-windmc*
  fi

  cd ..

# Extract %%__os_install_post into os_install_post~
cat << \EOF > os_install_post~
%__os_install_post
EOF

# Generate customized brp-*scripts
cat os_install_post~ | while read a x y; do
case $a in
# Prevent brp-strip* from trying to handle foreign binaries
*/brp-strip*)
  b=$(basename $a)
  sed -e 's,find $RPM_BUILD_ROOT,find $RPM_BUILD_ROOT%_bindir $RPM_BUILD_ROOT%_libexecdir,' $a > $b
  chmod a+x $b
  ;;
# Fix up brp-compress to handle %%_prefix != /usr
*/brp-compress*)
  b=$(basename $a)
  sed -e 's,\./usr/,.%{_prefix}/,g' < $a > $b
  chmod a+x $b
  ;;
esac
done

sed -e 's,^\s*/usr/lib/rpm.*/brp-strip,./brp-strip,' \
  -e 's,^\s*/usr/lib/rpm.*/brp-compress,./brp-compress,' \
< os_install_post~ > os_install_post
%define __os_install_post . ./os_install_post

%clean
  rm -rf $RPM_BUILD_ROOT

# ==============================================================
# powerpc-rtems-binutils
# ==============================================================
# %package -n rtems-4.6ng10-powerpc-rtems-binutils
# Summary:      rtems binutils for powerpc-rtems
# Group: Development/Tools
# %if %build_infos
# Requires: rtems-4.6ng10-binutils-common
# %endif

%description -n rtems-4.6ng10-powerpc-rtems-binutils
GNU binutils targetting powerpc-rtems.

%files -n rtems-4.6ng10-powerpc-rtems-binutils
%defattr(-,root,root)
%dir %{_prefix}
%dir %{_datarootdir}

%dir %{_mandir}
%dir %{_mandir}/man1
%{_mandir}/man1/powerpc-rtems-*.1*

%dir %{_bindir}
%{_bindir}/powerpc-rtems-*

%dir %{_exec_prefix}/powerpc-rtems
%dir %{_exec_prefix}/powerpc-rtems/bin
%{_exec_prefix}/powerpc-rtems/bin/*

%dir %{_exec_prefix}/powerpc-rtems/lib
%{_exec_prefix}/powerpc-rtems/lib/ldscripts
# ==============================================================
# rtems-4.6ng10-binutils-common
# ==============================================================
%package -n rtems-4.6ng10-binutils-common
Summary:      Base package for RTEMS binutils
Group: Development/Tools
%{?_with_noarch_subpackages:BuildArch: noarch}

Requires(post):		/sbin/install-info
Requires(preun):	/sbin/install-info

%description -n rtems-4.6ng10-binutils-common

RTEMS is an open source operating system for embedded systems.

This is the base for binutils regardless of target CPU.

%post -n rtems-4.6ng10-binutils-common
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/as.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/bfd.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/binutils.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/ld.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/standards.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/gprof.info.gz || :

%preun -n rtems-4.6ng10-binutils-common
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/as.info.gz || :
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/bfd.info.gz || :
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/binutils.info.gz || :
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/ld.info.gz || :
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/standards.info.gz || :
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gprof.info.gz || :
fi

%files -n rtems-4.6ng10-binutils-common
%defattr(-,root,root)
%dir %{_prefix}
%dir %{_infodir}
%ghost %{_infodir}/dir
%{_infodir}/as.info*
%{_infodir}/bfd.info*
%{_infodir}/binutils.info*
%{_infodir}/ld.info*
%{_infodir}/standards.info*
%{_infodir}/gprof.info*

%dir %{_prefix}/share
%dir %{_prefix}/share/locale

%changelog
* Sat Aug 09 2014 Evgueni Souleimanov <esoule@100500.ca> - 2.24-9.1.2
- update to binutils 2.24

* Thu Aug 07 2014 Evgueni Souleimanov <esoule@100500.ca> - 2.20.1-9.1.1
- build binutils 2.20.1 for rtems-4.6 (rtems-4.6ng10)
- place manpages to /opt/rtems-4.6ng10/man
- place info pages to /opt/rtems-4.6ng10/info

* Fri Feb 14 2014 RTEMS Project - 2.20.1-9
- Original Package, as provided by RTEMS Project for RTEMS 4.10
