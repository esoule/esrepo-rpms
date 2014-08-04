#
# Please send bugfixes or comments to
# 	http://www.rtems.org/bugzilla
#

%define _prefix                 /opt/rtems-4.11
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
%define _mandir                 %{_datarootdir}/man
%define _infodir                %{_datarootdir}/info
%define _localedir              %{_datarootdir}/locale

%ifos cygwin cygwin32 mingw mingw32
%define _exeext .exe
%define debug_package           %{nil}
%define _libdir                 %{_exec_prefix}/lib
%else
%define _exeext %{nil}
%endif

%ifos cygwin cygwin32
%if "%{_host}" == "x86_64-pc-cygwin"
%define optflags -O2 -pipe
%else
%define optflags -O3 -pipe -march=i486 -funroll-loops
%endif
%endif

%ifos mingw mingw32
%if %{defined _mingw32_cflags}
%define optflags %{_mingw32_cflags}
%else
%define optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4
%endif
%endif

%ifos mingw mingw64
%if %{defined _mingw64_cflags}
%define optflags %{_mingw64_cflags}
%else
%define optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4
%endif
%endif

%if "%{_build}" != "%{_host}"
%define _host_rpmprefix %{_host}-
%else
%define _host_rpmprefix %{nil}
%endif

%{?!el5:%global _with_noarch_subpackages 1}
%define gdb_version 7.7.1
%define gdb_rpmvers %{expand:%(echo 7.7.1 | tr - _)}

Name:		rtems-4.11-powerpc-rtems4.11-gdb
Summary:	Gdb for target powerpc-rtems4.11
Group:		Development/Tools
Version:	%{gdb_rpmvers}
Release:	1%{?dist}
License:	GPL/LGPL
URL: 		http://sourceware.org/gdb
%{?el5:BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}

BuildRequires:  %{_host_rpmprefix}gcc

%global build_sim --enable-sim

# Whether to build against system readline
# Default: yes, except on EL5
%if "%{gdb_version}" >= "7.3.91"
# gdb >= 7.3.91 requires readline6
# EL5's readline is too old
%{?el5:%bcond_with system_readline}
%{!?el5:%bcond_without system_readline}
%else
%bcond_without system_readline
%endif

# Whether to build python support
%if "%{_build}" != "%{_host}"
# Can't build python Cdn-X
%bcond_with python
%else
%bcond_without python
%endif
%{?with_python:BuildRequires: %{_host_rpmprefix}python-devel}

%if "%{_build}" != "%{_host}"
# psim doesn't support Cdn-X
%global build_sim --disable-sim
%else
%global build_sim --enable-sim --enable-sim-trace
%endif

# suse
%if %{defined suse}
BuildRequires: libexpat-devel
%else
# Fedora/CentOS/Cygwin/MinGW
BuildRequires: %{_host_rpmprefix}expat-devel
%endif

%{?with_system_readline:BuildRequires: %{_host_rpmprefix}readline-devel}
BuildRequires:  %{_host_rpmprefix}ncurses-devel

# Required for building the infos
BuildRequires:	/sbin/install-info
Requires:	rtems-4.11-gdb-common
BuildRequires:	%{?suse:makeinfo}%{!?suse:texinfo}

%if "%{gdb_version}" == "7.7.1"
Source0:  ftp://ftp.gnu.org/gnu/gdb/gdb-7.7.1.tar.bz2
Patch0: ftp://ftp.rtems.org/pub/rtems/SOURCES/4.11/gdb-7.7.1-rtems4.11-20140506.diff
%endif
%if "%{gdb_version}" == "7.7"
Source0:  ftp://ftp.gnu.org/gnu/gdb/gdb-7.7.tar.bz2
Patch0: ftp://ftp.rtems.org/pub/rtems/SOURCES/4.11/gdb-7.7-rtems4.11-20140206.diff
%endif

%description
GDB for target powerpc-rtems4.11
%prep
%setup -q -c -T -n %{name}-%{version}

%setup -q -D -T -n %{name}-%{version} -a0
cd gdb-%{gdb_version}
%{?PATCH0:%patch0 -p1}
cd ..

# Force using a system-provided libreadline
%{?with_system_readline:rm -f gdb-%{gdb_version}/readline/configure}
%build
  export PATH="%{_bindir}:${PATH}"
  mkdir -p build
  cd build
%if "%{_build}" != "%{_host}"
  CFLAGS_FOR_BUILD="-g -O2 -Wall" \
%endif
  CFLAGS="$RPM_OPT_FLAGS" \
  INSTALL="install -p" \
  ../gdb-%{gdb_version}/configure \
    --build=%_build --host=%_host \
    --target=powerpc-rtems4.11 \
    --verbose --disable-nls \
    --without-included-gettext \
    --disable-win32-registry \
    --disable-werror \
    %{build_sim} \
    %{?with_system_readline:--with-system-readline} \
    --with-expat \
    %{?with_python:--with-python}%{!?with_python:--without-python} \
    --with-gdb-datadir=%{_datadir}/powerpc-rtems4.11-gdb-%{gdb_version} \
    --prefix=%{_prefix} --bindir=%{_bindir} \
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

  rm -f $RPM_BUILD_ROOT%{_infodir}/dir
  touch $RPM_BUILD_ROOT%{_infodir}/dir

# These come from other packages
  rm -rf $RPM_BUILD_ROOT%{_infodir}/bfd*
  rm -rf $RPM_BUILD_ROOT%{_infodir}/configure*
  rm -rf $RPM_BUILD_ROOT%{_infodir}/standards*

# We don't ship host files
  rm -f ${RPM_BUILD_ROOT}%{_libdir}/libiberty*

# host library, installed to a bogus directory
  rm -f ${RPM_BUILD_ROOT}%{_libdir}/libpowerpc-rtems4.11-sim.a

# Bug in gdb-7.0, bogusly installs linux-only files
  somethinguseful=0
  for f in ${RPM_BUILD_ROOT}%{_datadir}/powerpc-rtems4.11-gdb-%{gdb_version}/syscalls/*.xml; do
    case $f in
    *linux.xml) rm -f $f;;
    *.xml) somethinguseful=1;;
    esac
  done
  if test $somethinguseful -eq 0; then
    rm -rf "${RPM_BUILD_ROOT}%{_datadir}/powerpc-rtems4.11-gdb-%{gdb_version}/syscalls"
  fi

%if "{gdb_version}" >= "7.3"
%if ! %{with python}
# gdb-7.3 doesn't honor --without-python correctly
  rm -rf ${RPM_BUILD_ROOT}%{_datadir}/powerpc-rtems4.11-gdb-%{gdb_version}/python
%endif
%endif

%if "%{gdb_version}" >= "7.3.91"
# gdb >= 7.3.91 installs host files, we don't want
  rm ${RPM_BUILD_ROOT}%{_includedir}/gdb/jit-reader.h
%endif

  cd ..

%if ("%{gdb_version}" == "7.7") || ("%{gdb_version}" == "7.7.1")
# gdb-7.7 misses to canonicalize man-pages
  mv ${RPM_BUILD_ROOT}%{_mandir}/man1/gdb.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/powerpc-rtems4.11-gdb.1
  mv ${RPM_BUILD_ROOT}%{_mandir}/man1/gdbserver.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/powerpc-rtems4.11-gdbserver.1
  mv ${RPM_BUILD_ROOT}%{_mandir}/man5/gdbinit.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/powerpc-rtems4.11-gdbinit.5

# not useful for us.
  rm -f ${RPM_BUILD_ROOT}%{_datadir}/powerpc-rtems4.11-gdb-%{gdb_version}/system-gdbinit/{wrs-linux,elinos}.*
  rmdir ${RPM_BUILD_ROOT}%{_datadir}/powerpc-rtems4.11-gdb-%{gdb_version}/system-gdbinit
%endif

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
  %{?el5:rm -rf $RPM_BUILD_ROOT}

# ==============================================================
# powerpc-rtems4.11-gdb
# ==============================================================
# %package -n rtems-4.11-powerpc-rtems4.11-gdb
# Summary:      rtems gdb for powerpc-rtems4.11
# Group: Development/Tools
# %if %build_infos
# Requires: rtems-4.11-gdb-common
# %endif

%description -n rtems-4.11-powerpc-rtems4.11-gdb
GNU gdb targetting powerpc-rtems4.11.

%files -n rtems-4.11-powerpc-rtems4.11-gdb
%{?el5:%defattr(-,root,root)}
%dir %{_prefix}
%dir %{_prefix}/share
%{?with_python:%{_datadir}/powerpc-rtems4.11-gdb-%{gdb_version}}

%dir %{_mandir}
%dir %{_mandir}/man1
%{_mandir}/man1/powerpc-rtems4.11-*.1*

%if "%{gdb_version}" >= "7.7"
%dir %{_mandir}/man5
%{_mandir}/man5/powerpc-rtems4.11-*.5*
%endif

%dir %{_bindir}
%{_bindir}/powerpc-rtems4.11-*

# ==============================================================
# rtems-4.11-gdb-common
# ==============================================================
%package -n rtems-4.11-gdb-common
Summary:      Base package for RTEMS gdbs
Group: Development/Tools
Requires(post):		/sbin/install-info
Requires(preun):	/sbin/install-info
%{?_with_noarch_subpackages:BuildArch: noarch}

%description -n rtems-4.11-gdb-common

GDB files shared by all targets.

%post -n rtems-4.11-gdb-common
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
%if "%{gdb_version}" < "7.7"
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/gdbint.info.gz || :
%endif
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/stabs.info.gz || :
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :

%preun -n rtems-4.11-gdb-common
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gdb.info.gz || :
%if "%{gdb_version}" < "7.7"
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/gdbint.info.gz || :
%endif
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/stabs.info.gz || :
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/annotate.info.gz || :
fi

%files -n rtems-4.11-gdb-common
%{?el5:%defattr(-,root,root)}
%dir %{_prefix}
%dir %{_prefix}/share

%dir %{_infodir}
%ghost %{_infodir}/dir
%{_infodir}/gdb.info*

%if "%{gdb_version}" < "7.7"
%{_infodir}/gdbint.info*
%endif
%{_infodir}/stabs.info*
%{_infodir}/annotate.info*

%changelog
* Tue May 06 2014 RTEMS Project - 7.7.1-1
- Original Package, as provided by RTEMS Project for RTEMS 4.11

