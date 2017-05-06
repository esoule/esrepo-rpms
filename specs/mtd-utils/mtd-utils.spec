Name:    mtd-utils
Version: 1.5.2
Release: 1%{?dist}
License: GPLv2+
Summary: Utilities for dealing with MTD (flash) devices
Group:   Applications/System
URL:     http://www.linux-mtd.infradead.org/
Source0: ftp://ftp.infradead.org/pub/mtd-utils/%{name}-%{version}.tar.bz2

BuildRequires: libacl-devel
BuildRequires: libuuid-devel
BuildRequires: lzo-devel
BuildRequires: zlib-devel

%description
The mtd-utils package contains utilities related to handling MTD devices,
and for dealing with FTL, NFTL JFFS2 etc.

%package ubi
Summary: Utilities for dealing with UBI
Group: Applications/System

%description ubi
The mtd-utils-ubi package contains utilities for manipulating UBI on 
MTD (flash) devices.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" make V=1

%install
make DESTDIR=$RPM_BUILD_ROOT SBINDIR=%{_sbindir} MANDIR=%{_mandir} install
#make DESTDIR=$RPM_BUILD_ROOT SBINDIR=%{_sbindir} MANDIR=%{_mandir} install -C ubi-utils


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc device_table.txt
%{_sbindir}/doc*
%{_sbindir}/flash*
%{_sbindir}/ftl*
%{_sbindir}/jffs2dump
%{_sbindir}/jffs2reader
%{_sbindir}/mkfs.jffs2
%{_sbindir}/mtd_debug
%{_sbindir}/nand*
%{_sbindir}/nftl*
%{_sbindir}/recv_image
%{_sbindir}/rfd*
%{_sbindir}/serve_image
%{_sbindir}/sumtool
%{_sbindir}/mkfs.ubifs
%{_sbindir}/mtdinfo
%{_sbindir}/mtdpart
%{_mandir}/*/*


%files ubi
%{_sbindir}/ubi*

%changelog
* Tue Aug 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.5.2-1
- Update to 1.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.5.1-5
- Append -stdc=gnu89 to CFLAGS (Work-around to c11 compatibility
  issues. Fix F23FTBFS, RHBZ#1239701).
- Append V=1 to make-call to make building verbose.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Josh Boyer <jwboyer@fedoraproject.org>
- Update to 1.5.1 (#1087285)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 11 2012 Josh Boyer <jwboyer@redhat.com>
- Update to 1.5.0 (#820903)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Josh Boyer <jwboyer@gmail.com>
- Update to 1.4.9 (#755183)

* Sun Aug 21 2011 Josh Boyer <jwboyer@gmail.com>
- Update to 1.4.6 (#693323)

* Sun Mar 20 2011 Josh Boyer <jwboyer@gmail.com>
- Update to 1.4.3 (#684374)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 01 2010 David Woodhouse <David.Woodhouse@intel.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 02 2008 David Woodhouse <david.woodhouse@intel.com> - 1.2.0-1
- Update to 1.2.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-3
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 David Woodhouse <dwmw2@infradead.org> - 1.1.0-2
- Build ubi-utils

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> - 1.1.0-1
- Update to 1.1.0 + nandtest + multicast utils

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> - 1.0.1-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 David Woodhouse <dwmw2@infradead.org> - 1.0.1-1
- Update to 1.0.1

* Tue May  2 2006 David Woodhouse <dwmw2@infradead.org> - 1.0.0-2
- Fixes from review (include COPYING), BR zlib-devel
- Include device_table.txt

* Sun Apr 30 2006 David Woodhouse <dwmw2@infradead.org> - 1.0.0-1
- Initial build.

