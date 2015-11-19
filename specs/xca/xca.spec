Summary:	Graphical X.509 certificate management tool
Name:		xca
Version:	1.3.2
Release:	1%{?dist}
License:	BSD
Group:		Applications/Productivity
URL:		http://xca.hohnstaedt.de/
Source0:	http://downloads.sourceforge.net/sourceforge/xca/%{version}/%{name}-%{version}.tar.gz
Patch1:		xca-1.3.2-oidfieldcursor.patch
BuildRequires:	qt4-devel openssl-devel
BuildRequires:	xdg-utils
BuildRequires:	ImageMagick
BuildRequires:	linuxdoc-tools
BuildRequires:	libtool-ltdl-devel
BuildRequires:	translate-toolkit
Requires:	hicolor-icon-theme


%description
  X Certificate and Key management is a graphic interface for managing
asymmetric keys like RSA or DSA, certificates and revocation lists. It is
intended as a small CA for creation and signing certificates. It uses the
OpenSSL library for the cryptographic operations.
  Certificate signing requests (PKCS#10), certificates (X509v3), the signing
of requests, the creation of self-signed certificates, certificate revocation
lists and SmartCards are supported. For an easy company-wide use, customizable
templates can be used for certificate and request generation. The PKI structures
can be imported and exported in several formats like PKCS#7, PKCS#12, PEM,
DER, PKCS#8. All cryptographic data are stored in a byte order agnostic file
format, portable across operating systems.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q
%patch1 -p 1 -b .oidfieldcursor


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

%configure CXXFLAGS="${RPM_OPT_FLAGS}					\
	-DXCA_DEFAULT_QT_TRANSLATE=\"\\\"%{_datadir}/qt4/translations\\\"\"" \
	STRIP=:								\
	LIBS="-Wl,-as-needed"
make %{?_smp_mflags}

convert img/xca.ico xca.png
touch -r img/xca.ico xca.png
convert img/xdb.ico xdb.png
touch -r img/xdb.ico xdb.png


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

make destdir="${RPM_BUILD_ROOT}" install

# HACK: check whether workarounds below are still necessary
if test ! -e "${RPM_BUILD_ROOT}%{_datadir}/xca/crl.png"
then	install -d -m 755						\
    "${RPM_BUILD_ROOT}%{_datadir}/"{applications,mime/packages,icons/hicolor}
	install -p -m 644 img/*.png "${RPM_BUILD_ROOT}%{_datadir}/xca"
fi

install -p -m 644 misc/xca.xml "${RPM_BUILD_ROOT}%{_datadir}/mime/packages/"

export XDG_DATA_DIRS="${RPM_BUILD_ROOT}%{_datadir}"
export XDG_UTILS_INSTALL_MODE=system

xdg-icon-resource install --noupdate --context mimetypes		\
	--size 32 xdb.png application-x-xca-database
xdg-icon-resource install --noupdate --size 32 xca.png fedora-xca

#	Replace the desktop icon.
rm -rf "${RPM_BUILD_ROOT}%{_datadir}/pixmaps/xca-32x32.xpm"
cp -a img/key.xpm "${RPM_BUILD_ROOT}%{_datadir}/pixmaps/xca.xpm"

desktop-file-install --mode 0644			\
	--dir "${RPM_BUILD_ROOT}%{_datadir}/applications"		\
	--delete-original						\
	--add-mime-type application/x-xca-database			\
	--remove-category QT						\
	--set-icon=xca							\
	"${RPM_BUILD_ROOT}%{_datadir}/applications/xca.desktop"

#	Will build the doc directory ourself.

rm -rf "${RPM_BUILD_ROOT}%{_docdir}/xca"

#	Tag translation files.

(
	cd "${RPM_BUILD_ROOT}"
	find '.%{_datadir}/xca' -name 'xca_[a-z][a-z].qm'
)									|
	sed -e 's/^\.//'						\
	    -e 's/.*\([a-z][a-z]\).qm$/%lang(\1) &/' > langfiles


#-------------------------------------------------------------------------------
%post
#-------------------------------------------------------------------------------

touch --no-create %{_datadir}/icons/hicolor || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :


#-------------------------------------------------------------------------------
%posttrans
#-------------------------------------------------------------------------------

gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database &> /dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


#-------------------------------------------------------------------------------
%postun
#-------------------------------------------------------------------------------

if [ "${1}" -eq 0 ]
then	touch --no-create %{_datadir}/icons/hicolor || :
	gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
	touch --no-create %{_datadir}/mime/packages &> /dev/null || :
	update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
fi


#-------------------------------------------------------------------------------
%files -f langfiles
#-------------------------------------------------------------------------------

%defattr(-, root, root, -)
%doc AUTHORS COPYRIGHT
%doc doc/*.html
%{_bindir}/*
%exclude %{_bindir}/xca_db_stat
%dir %{_datadir}/xca
%{_datadir}/xca/*.png
%{_datadir}/xca/*.txt
%{_datadir}/xca/*.xca
%{_datadir}/pixmaps/*.xpm
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/mime/packages/%{name}.*
%{_datadir}/applications/*
%attr(0644, root, root) %{_mandir}/*/*


#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------

* Mon Oct 26 2015 Patrick Monnerat <patrick.monnerat@dh.com> 1.3.2-1
- New upstream release.
- Patch "oidfieldcursor" to restore normal cursor behavior on OID resolver
  input field.
- Drop README.update.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Nov 24 2014 Patrick Monnerat <pm@datasphere.ch> 1.1.0-1
- New upstream release

* Mon Nov 17 2014 Patrick Monnerat <pm@datasphere.ch> 1.0.0-2
- Patch "nonstdext" avoids segfault when viewing cert with
  non-standard extension.
  https://bugzilla.redhat.com/show_bug.cgi?id=1164340

* Tue Oct 28 2014 Patrick Monnerat <pm@datasphere.ch> 1.0.0-1
- New upstream release.
  Set-up a larger desktop icon.

* Wed Oct 15 2014 Patrick Monnerat <pm@datasphere.ch> 0.9.3-9
- Patch "openssl101i" for openssl-1.0.1i compatibility.
  https://bugzilla.redhat.com/show_bug.cgi?id=1152043
- Patch "desktopicon" removes the icon file extension in desktop entry file.
  https://sourceforge.net/p/xca/patches/15/

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.3-7
- fix/update scriptlets

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Patrick Monnerat <pm@datasphere.ch> - 0.9.3-5
- Rebuild for elliptic curves inclusion.
  https://bugzilla.redhat.com/show_bug.cgi?id=1089245

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.3-3
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Patrick Monnerat <pm@datasphere.ch> 0.9.3-1
- New upstream release.

* Mon May  7 2012 Patrick Monnerat <pm@datasphere.ch> 0.9.2-1
- New upstream release.
- Patch "french" to update french translation.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Patrick Monnerat <pm@datasphere.ch> 0.9.1-1
- New upstream release: all previous patches included in new code.

* Mon Feb 28 2011 Patrick Monnerat <pm@datasphere.ch> 0.9.0-2
- Fix Exec parameter in desktop file.

* Mon Feb 28 2011 Patrick Monnerat <pm@datasphere.ch> 0.9.0-1
- New upstream release.
- Suppress "includes" patch (went upstream).
- Suppress "openssl10" patch (new release is openssl 10 compatible).
- Patches "locale" and "noec" port to new release.
- French localization added.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-1401
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Apr 18 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8.1-1400
- fixed implicit DSO linking (#565073)

* Sat Jan 16 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8.1-1300
- updated to 0.8.1
- reenabled ppc64

* Sun Jan  3 2010 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.8.0-1301
- updated to 0.8.0
- added patch to disable elliptic curve code because these algorithms
  are removed in Fedora's openssl

* Sun Sep 13 2009 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.7.0-0
- updated to 0.7.0; rediffed patches

* Wed Aug 26 2009 Tomas Mraz <tmraz@redhat.com> - 0.6.4-9
- rebuilt with new openssl

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.6.4-7
- include stdint.h for uint32_t

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Tomas Mraz <tmraz@redhat.com> - 0.6.4-5
- rebuild with new openssl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.4-4
- Autorebuild for GCC 4.3

* Sat Jan  5 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.6.4-3
- Add patch by Caolan McNamara (#427619) to build against new openssl

* Sat Aug 25 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.4-1
- updated to 0.6.4
- optimized scriptlets which are dealing with the desktop stuff

* Sat Jun 30 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-2
- improved desktop-integration by registering MIME type and icons
- disabled ppc64 build (bz #246324)

* Thu Jun 14 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.3-1
- updated to 0.6.3; rediffed patches
- fixed build
- added BR on linuxdoc-tools

* Mon Apr  9 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.1-1
- updated to 0.6.1

* Sat Mar 17 2007 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.6.0-1
- updated to 0.6.0
- removed old patches

* Fri Sep 15 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-6
- rebuilt

* Sat Feb 18 2006 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-5
- rebuilt for FC5

* Sun Dec 25 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-4
- fixed compilation with gcc41 and openssl098
- use SHA1 instead of MD5 as the default hashalgo

* Sat May 21 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-3
- generalized db4 detection
- fixed x86_64 builds

* Thu May 19 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1-2
- use %%dist instead of %%disttag

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Mar  8 2005 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0.5.1
- updated to 0.5.1
- (re)enabled parallel build
- applied -langinst patch and other ideas from
  https://bugzilla.fedora.us/show_bug.cgi?id=2019 (Ville Skyttä)
- fixed build with gcc4 and db43
- removed old cruft from the specfile

* Sat Dec 13 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> - 0:0.4.6-0.fdr.1
- changed compile/install commands to work with the new, yet-another configure system
- removed libpthread test since it went upstream
- do not package README anymore; it contains installation/build instructions only
- applied gcc3 patch
- updated to 0.4.6
- removed desktop patch which went upstream

* Fri Aug 15 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.5-0.fdr.2
- applied Ville Skyttä's patch to add categories and to fix encoding of desktop-file
  (http://sourceforge.net/tracker/index.php?func=detail&aid=789374&group_id=62274&atid=500027)
- removed '--add-category ...' options which become obsoleted by this
  patch

* Fri Aug 15 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.5-0.fdr.1
- updated to 0.4.5

* Thu Aug  7 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.4-0.fdr.1
- updated to 0.4.4
- use generic download address for Source0

* Sat Jul 26 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.2-0.fdr.1.1
- changed Summary: accordingly the suggestion in Fedora bug #494

* Mon Jul 21 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.2-0.fdr.1
- updated to 0.4.2

* Sun Jul 20 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.1-0.fdr.2
- removed the %%{smp_mflags} since parallel builds are not supported
  by the QT makefiles

* Tue Jul 15 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.1-0.fdr.1
- updated to 0.4.1
- added debian/changelog to %%doc-list

* Tue Jul  8 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.4.0-0.fdr.1
- updated to 0.4.0
- removed patches which went upstream

* Fri Jul  4 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.3.2-0.fdr.2.1
- fixed Summary

* Tue Jul  1 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0:0.3.2-0.fdr.2
- added icon
- made minor fixes in the %%description
- added explicit epoch
- created a separate .desktop file

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.3.2-0.fdr.1
- prepared for fedora.us

* Tue Jun 10 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de> 0.3.2-0.0.3
- added dbpriv patch
- added desktop entry

* Fri Jun  6 2003 Enrico Scholz <enrico.scholz@informatik.tu-chemnitz.de>
- Initial build.
