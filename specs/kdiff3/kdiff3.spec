Name:           kdiff3
Version:        0.9.98
Release:        1.1.1%{?dist}
Summary:        Compare + merge 2 or 3 files or directories

Group:          Development/Tools
License:        GPLv2
URL:            http://kdiff3.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/kdiff3/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# No longer needed for 0.9.97
# Remove bogus MimeType tag from kdiff3part.desktop
# Patch0:         kdiff3part.desktop.diff
# No longer needed for 0.9.96
# Install kdiff3_part.rc into correct location
# Patch1:        kdiff3part.rc.diff
# No longer needed for 0.9.96
# fix build against kde-4.5 (pre)releases
# Patch2:        kdiff3-0.9.95-docbook_fixes.patch

# No longer needed for 0.9.98
# Patch0:         kdiff3-0.9.97-saving_files.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  kdebase4-devel
Requires:  oxygen-icon-theme

%description
KDiff3 is a program that
- compares and merges two or three input files or directories,
- shows the differences line by line and character by character (!),
- provides an automatic merge-facility and
- an integrated editor for comfortable solving of merge-conflicts
- has support for KDE-KIO (ftp, sftp, http, fish, smb)
- and has an intuitive graphical user interface.


%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf $RPM_BUILD_ROOT

make -C %{_target_platform} install/fast DESTDIR=$RPM_BUILD_ROOT

# locale's
%find_lang %{name} --with-kde || touch %{name}.lang
%find_lang %{name}plugin || touch %{name}plugin.lang
%find_lang kdiff3fileitemactionplugin || touch kdiff3fileitemactionplugin.lang
cat %{name}plugin.lang >> %{name}.lang
cat kdiff3fileitemactionplugin.lang >> %{name}.lang
# avoid warning "File listed twice" on packaging
cat %{name}.lang | LANG=C sort | uniq >%{name}.lang.1
mv %{name}.lang.1 %{name}.lang

# Desktop.
desktop-file-install  --vendor="" \
    --dir=$RPM_BUILD_ROOT%{_kde4_datadir}/applications/kde4  \
    --add-category=Development \
        $RPM_BUILD_ROOT%{_kde4_datadir}/applications/kde4/kdiff3.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
touch --no-create %{_kde4_iconsdir}/locolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null
  touch --no-create %{_kde4_iconsdir}/locolor &> /dev/null || :
  gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
  gtk-update-icon-cache %{_kde4_iconsdir}/locolor &> /dev/null || :
  update-desktop-database -q &> /dev/null
fi

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/locolor &> /dev/null || :
update-desktop-database -q &> /dev/null


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_kde4_bindir}/kdiff3
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
%{_kde4_libdir}/kde4/kdiff3fileitemaction.so
%else
%{_kde4_libdir}/kde4/libkdiff3plugin.so
%endif
%{_kde4_datadir}/applications/kde4/*.desktop
%{_kde4_appsdir}/kdiff3/
%{_kde4_appsdir}/kdiff3part/
%{_kde4_iconsdir}/hicolor/*/*/kdiff3.png
%{_kde4_iconsdir}/locolor/*/*/kdiff3.png
%{_kde4_datadir}/kde4/services/kdiff3*.desktop

%changelog
* Tue Jul 29 2014 Evgueni Souleimanov <esoule@100500.ca> - 0.9.98-1.1.1
- Update to 0.9.98

* Tue Jul 29 2014 Evgueni Souleimanov <esoule@100500.ca> - 0.9.97-7.1.1
- fix plugin packaging errors on EL6
- avoid warning "File listed twice" on packaging

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Neal Becker <ndbecker2@gmail.com> - 0.9.97-5
- bump version to match f17 version

* Wed Nov 21 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.97-4.trashy
- Fix for saving files on KDE with relative path specified
  via command line option -o.

* Mon Aug 13 2012 Neal Becker <ndbecker2@gmail.com> - 0.9.97-3
- Remove libkdiff3*.so

* Mon Aug 13 2012 Neal Becker <ndbecker2@gmail.com> - 0.9.97-1
- Update to 0.9.97

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.96-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 24 2012 Neal Becker <ndbecker2@gmail.com> - 0.9.96-6
- Add req: oxygen-icon-theme to close BR 771356

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.96-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-5
- added kdiff3fileitemactionplugin

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-4
- Remove patch2

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-3
- Remove patch1

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-2
- fix patch

* Sat Sep  3 2011 Neal Becker <ndbecker2@gmail.com> - 0.9.96-1
- Update to 0.9.96

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 13 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.9.95-5
- ftbfs against kde-4.5 (pre)releases
- optimize scriplets
- drop HTML doc hackery, use %%find_lang --with-kde

* Sun Mar 28 2010 Neal Becker <ndbecker2@gmail.com> - 0.9.95-4
- Install kdiff3_part.rc into correct location

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar  4 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.95-2
- Fix Changelog order

* Wed Mar  4 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.95-1
- Update to 0.9.95

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.94-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.94-1
- Update to 0.9.94

* Fri Jan  9 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-1.3%{?dist}
- Update to 0.9.93-3

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-2-1
- Update to 0.9.93-2

* Tue Jan  6 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.9.93-6
- use kde4 macros
- add scriptlets for locolor icons
- update d-f-i usage
- include khelpcenter handbook
- update Source0 URL

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-5
- Fix HTML_DIR and use kde4_ versions of datadir, libdir, bindir

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-4
- Remove /etc/profile.d/qt.sh, remove configure

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-3
- Change BR, no longer kde3

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-2
- Add br cmake

* Tue Jan  6 2009 Neal Becker <ndbecker2@gmail.com> - 0.9.93-1
- Update to 0.9.93

* Thu Jun 5 2008 Manuel Wolfshant <wolfy@fedoraproject.org> - 0.9.92-14
- add a conditional BR, allowing build in EPEL-5

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 0.9.92-13
- drop BR: qt-devel (broken)
- omit 64bit configure hack (invalid and not needed)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.92-12
- Autorebuild for GCC 4.3

* Sun Dec  2 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-11
- BR qt-devel
- source /etc/profile.d/qt.sh for mock

* Wed Nov  7 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-10
- Update desktop-file-install as suggest by Rex

* Wed Nov  7 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-8
- Use desktop-file-install for kdiff3plugin.desktop

* Tue Nov  6 2007 Neal Becker <ndbecker2@gmail.com> - 0.9.92-7
- Update to 0.9.92
- Add /usr/share/applnk/.hidden/kdiff3plugin.desktop

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.9.90-7
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sun Aug 27 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.90-6
- Untabify
- --add-category X-Fedora
- Add gtk-update-icon-cache

* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-5
- Remove ldconfig
* Fri May 12 2006 Laurent Rineau <laurent.rineau__fc_extra@normalesup.org> - 0.9.88-5
- Quote percent sign in %%changelog.
- Cleanup in %%files
- Removed Requires: tag.


* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-4
- Remove applnk stuff
- Add %%post + %%postun

* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-3
- Fix symlinks (from Rex Dieter)

* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-2
- Fix source0
- Fix E: kdiff3 standard-dir-owned-by-package /usr/share/icons
  E: kdiff3 standard-dir-owned-by-package /usr/share/man
  E: kdiff3 standard-dir-owned-by-package /usr/share/man/man1
- Fix Summary

* Thu May 11 2006 Neal Becker <ndbecker2@gmail.com> - 0.9.88-1
- Initial

