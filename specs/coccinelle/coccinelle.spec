%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Name:           coccinelle
Version:        1.0.4
Release:        4%{?dist}
Summary:        Semantic patching for Linux (spatch)

Group:          Development/Libraries
License:        GPLv2

ExcludeArch:    sparc64 s390 s390x ppc64

URL:            http://coccinelle.lip6.fr/
Source0:        http://coccinelle.lip6.fr/distrib/%{name}-%{version}.tgz

Patch1:         0001-Build-failure-on-ppc64le-Failure-dump-impossible-tag.patch

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  ocaml-menhir-devel
BuildRequires:  latexmk
BuildRequires:  /usr/bin/pdflatex
BuildRequires:  hevea
BuildRequires:  python-devel
BuildRequires:  chrpath

# This stops the automatic dependency generator adding some bogus
# OCaml dependencies.  Unfortunately we have to keep adding modules to
# this list every time there is some change in coccinelle.  There
# should be a better way, but I don't know what.
%global __ocaml_requires_opts \
-i ANSITerminal \
-i Ast0_cocci \
-i Ast_c \
-i Ast_cocci \
-i Commands \
-i Common \
-i Config \
-i Control_flow_c \
-i Cpp_token_c \
-i Dumper \
-i Exposed_modules \
-i Externalanalysis \
-i Flag \
-i Iteration \
-i Lexer_c \
-i Lexer_parser \
-i Lib_parsing_c \
-i Mapb \
-i Oassoc \
-i Oassoc_buffer \
-i Oassocb \
-i Oassoch \
-i Objet \
-i Ocollection \
-i Ograph2way \
-i Ograph_extended \
-i Oset \
-i Osetb \
-i Oseti \
-i Parse_c \
-i Parser_c \
-i Parsing_stat \
-i Pretty_print_c \
-i Regexp \
-i SetPt \
-i Setb \
-i Seti \
-i Sexplib \
-i Token_annot \
-i Token_c \
-i Token_views_c \
-i Type_cocci \
-i Type_annoter_c \
-i Visitor_c \
%{nil}

# RHBZ#725415.
Requires:       ocaml-findlib

# Bundled libraries.
#
# We could unbundle both of these, but it would require packaging them
# in Fedora.  I don't know which version of the library is included.
Provides:       bundled(ocaml-pycaml)
Provides:       bundled(ocaml-parmap)


%description
Coccinelle is a tool to utilize semantic patches for manipulating C
code.  It was originally designed to ease maintenance of device
drivers in the Linux kernel.


%package doc
Summary:        Documentation for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description doc
The %{name}-doc package contains documentation for %{name}.


%package examples
Summary:        Examples for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description examples
The %{name}-examples package contains examples for %{name}.



%prep
%setup -q -n %{name}-%{version}

%patch1 -p1

# Remove .cvsignore files.
find -name .cvsignore -delete

# Convert a few files to UTF-8 encoding.
for f in demos/demo_rule9/sym53c8xx.res demos/demo_rule9/sym53c8xx.c; do
  mv $f $f.orig
  iconv -f iso-8859-1 -t utf-8 < $f.orig > $f
  rm $f.orig
done


%build
%configure --enable-release=yes    \
    --enable-dynlink=yes    \
    --enable-menhirLib=yes    \
    --enable-parmap=no    \
    --enable-ocaml=yes    \
    --enable-python=yes    \
    --enable-pycaml=no    \
    --enable-camlp4=yes    \
    --enable-pcre-syntax=yes    \
    --enable-pcre=yes    \
    --enable-opt=yes    \
    --without-pkg-config    \
    --with-ocamllex=%{_bindir}/ocamllex    \
    --with-ocamlyacc=%{_bindir}/ocamlyacc    \
    --with-ocamlfind=%{_bindir}/ocamlfind    \
    --with-ocamlprof=%{_bindir}/ocamlprof    \
    --with-menhir=%{_bindir}/menhir    \
    --without-pdflatex

%{__sed} -i \
  -e 's,LIBDIR=.*,LIBDIR=%{_libdir},' \
  -e 's,MANDIR=.*,MANDIR=%{_mandir},' \
  -e 's,SHAREDIR=.*,SHAREDIR=%{_libdir}/%{name},' \
  -e 's,DYNLINKDIR=.*,DYNLINKDIR=%{_libdir}/ocaml,' \
  Makefile.config

%if !%opt
make byte EXTLIBDIR=`ocamlc -where`/extlib %{_smp_mflags}
%else
make world EXTLIBDIR=`ocamlc -where`/extlib %{_smp_mflags}
%endif


%install
make DESTDIR=$RPM_BUILD_ROOT install

# Remove these (they are just wrapper scripts).
rm -f $RPM_BUILD_ROOT%{_bindir}/spatch.byte
rm -f $RPM_BUILD_ROOT%{_bindir}/spatch.opt

# Move the libdir stuff into a subdirectory.
pushd $RPM_BUILD_ROOT%{_libdir}
mkdir coccinelle
for f in standard.h standard.iso spatch spatch.byte spatch.opt; do
  if [ -f $f ]; then
    mv $f coccinelle/$f
  fi
done
popd

# Move Python libraries to python sitelib directory.
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}
mv $RPM_BUILD_ROOT%{_libdir}/python/coccilib \
  $RPM_BUILD_ROOT%{python_sitelib}

rmdir $RPM_BUILD_ROOT%{_libdir}/python

# Move OCaml libraries.
pushd $RPM_BUILD_ROOT%{_libdir}
rm ocaml/*.cmi
mkdir ocaml/stublibs
mv dllpycaml_stubs.so ocaml/stublibs
popd


%check
export COCCINELLE_HOME=$RPM_BUILD_ROOT%{_libdir}/coccinelle
export LD_LIBRARY_PATH=.

# Run --help to check the command works in general.
$RPM_BUILD_ROOT%{_bindir}/spatch --help

# Test fails with "Fatal error: Out of memory".
# Seems to be a bug in coccinelle, so it's unlikely that this
# package really functions properly.
$RPM_BUILD_ROOT%{_bindir}/spatch -sp_file demos/simple.cocci demos/simple.c


%files
%doc authors.txt bugs.txt changes.txt copyright.txt
%doc credits.txt install.txt license.txt readme.txt
%{_bindir}/pycocci
%{_bindir}/spatch
%{_libdir}/%{name}/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{python_sitelib}/coccilib/
%{_libdir}/ocaml/stublibs/*.so
%if !%opt
%config(noreplace) /etc/prelink.conf.d/%{name}.conf
%endif


%files doc
%doc docs


%files examples
%doc demos


%changelog
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Richard Jones <rjones@redhat.com> - 1.0.4-3
- Apply patch to fix ppc64le builds (thanks Julia Lawall) (RHBZ#1297855).
  See also: https://systeme.lip6.fr/pipermail/cocci/2016-January/thread.html#2742

* Wed Jan 06 2016 Richard Jones <rjones@redhat.com> - 1.0.4-2
- Remove bogus python_sitelib definition.

* Tue Nov  3 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-1
- New upstream version 1.0.4.
- Remove the spgen program as it is not meant to be packaged.
- Do not need to delete menhir files.
- Do not install OCaml *.cmi files.

* Tue Oct 27 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-1
- New upstream version 1.0.3.
- Set DYNLINKDIR.
- Unbundle ocaml-menhir, regenerate intermediate parser files.
- Declare that pycaml and parmap are bundled.
- Use 'make world' install of 'make all opt' (see install.txt).
- Add spgen to package.  It's broken at the moment - reported upstream.
- Various BRs required to build the documentation.

* Tue Sep 01 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-1
- New upstream version 1.0.2.
- Use standard configure macro instead of ./configure.
- Various fixes to configuration.
- Package OCaml bindings.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-5
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-4
- ocaml-4.02.2 final rebuild.

* Tue Jun 23 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-3
- Put coccinelle data into libdir (instead of /usr/share) since it
  contains the binaries.
- Remove all the code which moved the binaries around.
- Fix the spatch wrapper script to contain the correct directory (RHBZ#1234812)

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-1
- New upstream version 1.0.1 (RHBZ#1233198).

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-4
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-2
- Ignore some more internal module names when generating dependencies.

* Thu Apr 23 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-1
- Version 1.0.0(!)

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.5
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.4
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.3
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc21.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.1
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1
- New upstream version 1.0.0-rc21.
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc20.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc20.1
- New upstream version 1.0.0-rc20.

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc18.1
- New upstream version 1.0.0-rc18.
- OCaml 4.01.0 rebuild.
- Enable debuginfo.
- Remove strip & prelink hacks.
- Enable test.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc17.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 27 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc17.2
- Ignore a lot more symbols leaked by the library.

* Fri Apr 26 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc17.1
- New upstream version 1.0.0-rc17.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc14.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 1.0.0-0.rc14.6
- Rebuild for ocaml 4.0.1.

* Tue Jul 31 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc14.5
- Remove sexplib patch which is no longer required by upstream.
- Enable parallel building.

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc14.3
- Confirmed with upstream that *.so files are no longer required.
- Re-enable move of python libs to python library dir.

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc14.2
- New upstream version 1.0.0-rc14.
- +BR ocaml-camlp4-devel

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc12.3
- New upstream version 1.0.0-rc12.
- Rebuild for OCaml 4.00.0.
- Remove buildroot, defattr, clean for modern RPM.
- Includes bundled extlib.  Disable this by adding BR ocaml-extlib-devel.
- Remove bytecode binary (spatch.byte).
- Fix check rule so it sets COCCINELLE_HOME.
- NB: TEST DISABLED.  UNLIKELY THAT SPATCH FUNCTIONS CORRECTLY.
  + Disable _libdir/*.so stripping.  Why is it not installed?
  + Disable Python stuff.  Why is it not installed?

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc9.6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.0.0-0.rc9.6.1
- Rebuild against PCRE 8.30

* Wed Feb  1 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc9.6
- Update to 1.0.0-rc9 (requested by Julia Lawall).

* Thu Jan 12 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc8.5
- Ignore Regexp (internal module).

* Sat Jan  7 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc8.3
- Update to 1.0.0-rc8.
- Rebuild for OCaml 3.12.1.
- Use Fedora ocaml-sexplib, ocaml-pcre instead of forked embedded one.

* Mon Jul 25 2011 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc4.2
- Update to 1.0.0-rc4.
- Requires ocaml-findlib (RHBZ#725415).
- Non-upstream patch to remove use of a couple of functions from the
  forked ocaml sexpr project, so we can use the Fedora one instead.
  See: http://lists.diku.dk/pipermail/cocci/2011-January/001439.html
- Include a new manpage in section 3.

* Wed Mar 30 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc9.1
- Update to 0.2.5-rc9.
- Ignore a bunch more false dependencies.

* Sat Mar  5 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc4.3
- Bump and rebuild to try to fix dependency issue.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-0.rc4.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc4.2
- New upstream version 0.2.5-rc4.

* Mon Jan 10 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc1.2
- Bump and rebuild.

* Fri Jan  7 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc1.1
- New upstream version 0.2.5-rc1.
- Remove upstream patch for Python 2.7.
- Rebuild for OCaml 3.12.0.

* Wed Jul 28 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.2.3-0.rc6.3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 24 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.3-0.rc6.2
- Ignore some bogus generated requires.

* Fri Jul 23 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.3-0.rc6.1
- Fix for Python 2.7.

* Fri Jul 23 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.3-0.rc6
- New upstream version 0.2.3rc6.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-0.rc1.2.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jan 12 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.0-0.rc1.2
- New upstream version 0.2.0rc1.

* Thu Nov  5 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-2
- Upstream URL and Source0 changed.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-1
- New upstream version 0.1.10.
- Removed patch, since fix to CVE-2009-1753 (RHBZ#502174) is now upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.8-4
- New upstream version 0.1.8.
- Include patch from Debian to fix CVE-2009-1753 (RHBZ#502174).
- Segfaults on PPC64, so added to ExcludeArch.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Mar 17 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.5-3
- Make the documentation subpackage "-doc" not "-docs".
- Comment about patch0 and send upstream.

* Mon Mar 16 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.5-2
- BR python-devel.

* Mon Mar 16 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.5-1
- New upstream version 0.1.5.
- Use the correct method to get Python sitelib (Michal Schmidt).

* Wed Jan 28 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-8
- Remove useless Makefiles from python/coccilib.
- License is GPLv2 (not GPLv2+).
- Include documentation and demos in subpackages.
- Move python library to a more sensible path.
- Add a check section.

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-6
- Install the shared library in _libdir.
- Install the native code version if we have the optimizing compiler.

* Wed Jan 21 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-3
- Patch for Python 2.6.

* Wed Jan 21 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-2
- Initial RPM release.
