%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%if %opt
%global target native
%else
%global target byte
%global debug_package %{nil}
%endif

Name:           ocaml-menhir
Version:        20150914
Release:        1%{?dist}
Summary:        LR(1) parser generator for OCaml

# The generator is QPL, with an exception granted to clause 6c.
License:        QPL with exceptions
URL:            http://gallium.inria.fr/~fpottier/menhir/
Source0:        http://gallium.inria.fr/~fpottier/menhir/menhir-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib

%description
Menhir is a LR(1) parser generator for the Objective Caml programming
language.  That is, Menhir compiles LR(1) grammar specifications down to
OCaml code.  Menhir was designed and implemented by François Pottier and
Yann Régis-Gianas.

%package        devel
Summary:        Development files for %{name}
# The library is LGPLv2+ with a linking exception.
License:        LGPLv2+ with exceptions
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
%setup -q -n menhir-%{version}

# Fix encodings
for f in AUTHORS menhir.1 src/standard.mly src/*.ml src/*.mli; do
  iconv -f ISO8859-1 -t UTF-8 $f > $f.fixed
  touch -r $f $f.fixed
  mv -f $f.fixed $f
done

# Enable debuginfo
sed -i 's/-j 0/-cflag -g -lflag -g &/' src/Makefile

# Do not ship the obsolete demos
rm -fr demos/obsolete

%build
make PREFIX=%{_prefix} TARGET=%{target}
make -C demos clean

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install PREFIX=%{buildroot}%{_prefix} TARGET=%{target}
rm -fr %{buildroot}%{_docdir}/menhir

%files
%doc AUTHORS CHANGES manual.pdf demos
%license LICENSE
%{_bindir}/menhir
%{_mandir}/man1/menhir.1*
%{_datadir}/menhir/

%files devel
%{_libdir}/ocaml/menhirLib/

%changelog
* Sat Sep 19 2015 Jerry James <loganjerry@gmail.com> - 20150914-1
- New upstream version

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-5
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-4
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-3
- ocaml-4.02.2 rebuild.

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 20141215-2
- ocaml-4.02.1 rebuild.

* Mon Jan  5 2015 Jerry James <loganjerry@gmail.com> - 20141215-1
- New upstream version

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 20140422-7
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 20140422-6
- ocaml-4.02.0+rc1 rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140422-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 20140422-4
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.
- Fix license handling

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 20140422-3
- OCaml 4.02.0 beta rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140422-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Jerry James <loganjerry@gmail.com> - 20140422-1
- New upstream version
- Fix standard.mly character encoding

* Fri Apr 18 2014 Jerry James <loganjerry@gmail.com> - 20130911-3
- Remove ocaml_arches macro (bz 1087794)

* Mon Sep 16 2013 Jerry James <loganjerry@gmail.com> - 20130911-2
- Rebuild for OCaml 4.01.0

* Thu Sep 12 2013 Jerry James <loganjerry@gmail.com> - 20130911-1
- New upstream version
- Allow debuginfo generation since ocaml 4 supports it

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Jerry James <loganjerry@gmail.com> - 20130116-1
- New upstream version

* Wed Oct 17 2012 Jerry James <loganjerry@gmail.com> - 20120123-5
- Rebuild for OCaml 4.00.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120123-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Richard W.M. Jones <rjones@redhat.com> - 20120123-3
- Rebuild for OCaml 4.00.0.

* Fri Jun  8 2012 Jerry James <loganjerry@gmail.com> - 20120123-2
- Rebuild for OCaml 4.00.0

* Mon Jan 23 2012 Jerry James <loganjerry@gmail.com> - 20120123-1
- New upstream version

* Fri Jan  6 2012 Jerry James <loganjerry@gmail.com> - 20111019-3
- Rebuild for ocaml 3.12.1

* Mon Dec 19 2011 Jerry James <loganjerry@gmail.com> - 20111019-2
- Change the subpackages to match Debian
- Add patch to allow building demos outside of the menhir source tree

* Wed Nov  9 2011 Jerry James <loganjerry@gmail.com> - 20111019-1
- Initial RPM
