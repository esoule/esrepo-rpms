Name: cppunit
Version: 1.13.2
Release: 16%{?dist}

Summary: C++ unit testing framework
# no license in files
License: LGPLv2+
Group: Development/Libraries
Url: https://wiki.freedesktop.org/www/Software/cppunit/
Source: http://dev-www.libreoffice.org/src/cppunit-%{version}.tar.gz
Patch0: cppunit-1.12.0-nolibdir.patch
#https://sourceforge.net/tracker/?func=detail&aid=2912630&group_id=11795&atid=311795
Patch2: cppunit-warnings-sf2912630.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: doxygen, graphviz

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised
tests.

This is the LibreOffice-maintained version.

%package devel
Summary: Libraries and headers for cppunit development
Group: Development/Libraries
Requires: pkgconfig, automake
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the libraries and headers necessary for developing
programs that use cppunit.

%package doc
Summary: HTML formatted API documention for cppunit
Group: Documentation

%description doc
The cppunit-doc package contains HTML formatted API documention generated by
the popular doxygen documentation generation tool.

%package demos
Summary: Tests and example programs for cppunit
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description demos
This package contains the example programs that were built as part of
testing the cppunit library.

%prep
%setup -q
%patch0 -p1 -b .nolibdir
for file in THANKS ChangeLog NEWS; do
   iconv -f latin1 -t utf8 < $file > ${file}.utf8
   touch -c -r $file ${file}.utf8
   mv ${file}.utf8 $file
done
%patch2 -p1 -b .warnings-sf2912630

# clean up examples
rm -rf __dist-examples __dist-examples-dir
cp -a examples __dist-examples
# Makefile.am files are left as documentation
find __dist-examples \( -name Makefile.in -o -name .cvsignore -o -name '*.dsw' -o -name '*.dsp' \) -exec rm {} \;
chmod a-x __dist-examples/qt/run.bat
mkdir __dist-examples-dir
mv __dist-examples __dist-examples-dir/examples


%build
export LDFLAGS=-ldl
%configure --enable-doxygen --disable-static 
make %{?_smp_mflags}
# XXX need to run this here to generate the example executables
make %{?_smp_mflags} -C examples/simple simple
make %{?_smp_mflags} -C examples/cppunittest cppunittestmain
make %{?_smp_mflags} -C examples/hierarchy hierarchy
make %{?_smp_mflags} -C examples/money MoneyApp

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
rm $RPM_BUILD_ROOT%{_libdir}/*.la
# remove double of doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/cppunit

# ensure that timestamp of cppunit-config is the same for all arches
touch -c -r cppunit-config.in.nolibdir $RPM_BUILD_ROOT%{_bindir}/cppunit-config

# install the example executables
install -d -m 0755 $RPM_BUILD_ROOT%{_libexecdir}/cppunit/examples
install -p -m 0755 ./examples/simple/.libs/simple $RPM_BUILD_ROOT%{_libexecdir}/cppunit/examples/
install -p -m 0755 ./examples/cppunittest/.libs/cppunittestmain $RPM_BUILD_ROOT%{_libexecdir}/cppunit/examples/
install -p -m 0755 ./examples/hierarchy/.libs/hierarchy $RPM_BUILD_ROOT%{_libexecdir}/cppunit/examples/
install -p -m 0755 ./examples/money/.libs/MoneyApp $RPM_BUILD_ROOT%{_libexecdir}/cppunit/examples/

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README THANKS ChangeLog TODO BUGS doc/FAQ
%{_bindir}/DllPlugInTester
%{_libdir}/libcppunit*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/cppunit-config
%{_includedir}/cppunit
%{_libdir}/libcppunit.so
%{_datadir}/aclocal/cppunit.m4
%{_mandir}/man1/cppunit-config.1*
%{_libdir}/pkgconfig/cppunit.pc

%files doc
%defattr(-,root,root,-)
%doc __dist-examples-dir/examples/
%doc doc/html

%files demos
%defattr(-,root,root,-)
%{_libexecdir}/cppunit

%changelog
* Sun Jul 19 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.13.2-16
- Add cppunit-demos package

* Sun Jul 19 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.13.2-14
- Update to 1.13.2.
- Switch to Freedesktop upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 David Tardon <dtardon@redhat.com> - 1.12.1-11
- rhbz#925193 add support for aarch64

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 05 2011 Caolán McNamara <caolanm@redhat.com> - 1.12.1-6
- add sf#2912630 fix for unused argument warnings

* Tue Jun 28 2011 Steven M. Parrish <smparrish@gmail.com> - 1.12.1-5
- Fix for bug 452340

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 18 2008 Patrice Dumas <pertusus@free.fr> 1.12.1-1
- Update to 1.12.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.12.0-5
- Autorebuild for GCC 4.3

* Mon Dec 17 2007 Patrice Dumas <pertusus@free.fr> 1.12.0-4
- remove libdir reference to cppunit-config, should fix multiarch conflict
  (#340951)
- fix encoding and remove windows related files in examples
- keep timestamps

* Mon Jan 29 2007 Patrice Dumas <pertusus@free.fr> 1.12.0-3
- add rightly files to -devel (#224106)
- add necessary requires for -devel (#224106)
- ship examples

* Sun Sep 10 2006 Patrice Dumas <pertusus@free.fr> 1.12.0-2
- rebuild for FC6

* Wed Jul  5 2006 Patrice Dumas <pertusus@free.fr> 1.12.0-1
- update to 1.12

* Sun May 21 2006 Patrice Dumas <pertusus@free.fr> 1.11.6-1
- update to 1.11.6

* Wed Dec 21 2005 Patrice Dumas <pertusus@free.fr> 1.11.4-1
- update

* Mon Aug 15 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.11.0-2
- various cleanups

* Mon Jul  4 2005 Patrice Dumas <pertusus@free.fr> 1.11.0-1
- update using the fedora template 
 
* Sat Apr 14 2001 Bastiaan Bakker <bastiaan.bakker@lifeline.nl>
- Initial release
