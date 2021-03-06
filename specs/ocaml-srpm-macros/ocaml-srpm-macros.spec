# OCaml has a bytecode backend that works on anything with a C
# compiler, and a native code backend available on a subset of
# architectures.  A further subset of architectures support native
# dynamic linking.
#
# This package contains a single file needed to define some RPM macros
# which are required before any SRPM is built.
#
# See also: https://bugzilla.redhat.com/show_bug.cgi?id=1087794

%if 0%{?rhel} && 0%{?rhel} <= 6
%global macros_dir %{_sysconfdir}/rpm
%else
%global macros_dir %{_rpmconfigdir}/macros.d
%endif

Name:           ocaml-srpm-macros
Version:        2
Release:        3.101%{?dist}

Summary:        OCaml architecture macros
License:        GPLv2+

BuildArch:      noarch

Source0:        macros.ocaml-srpm

# NB. This package MUST NOT Require anything (except for dependencies
# that RPM itself generates).

%description
This package contains macros needed by RPM in order to build
SRPMS.  It does not pull in any other OCaml dependencies.


%prep


%build


%install
mkdir -p $RPM_BUILD_ROOT%{macros_dir}
install -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{macros_dir}/macros.ocaml-srpm


%files
%{macros_dir}/macros.ocaml-srpm


%changelog
* Sun Apr 10 2016 Evgueni Souleimanov <esoule@100500.ca> - 2-3.101
- Add EL6 support

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  2 2014 Richard W.M. Jones <rjones@redhat.com> - 2-1
- Move macros to _rpmconfigdir (RHBZ#1093528).

* Tue Apr 22 2014 Richard W.M. Jones <rjones@redhat.com> - 1-1
- New package.
