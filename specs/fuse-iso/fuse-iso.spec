# $Id$
# Authority: dag

%define real_name fuseiso
%define real_version 20070708

Summary: FUSE module to mount ISO filesystem images
Name: fuse-iso
Version: 0.0.20070708
Release: 2.101%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://fuse.sourceforge.net/wiki/index.php/FuseIso

Source: http://ubiz.ru/dm/fuseiso-%{real_version}.tar.bz2
# https://bugzilla.redhat.com/show_bug.cgi?id=440436
# https://bugzilla.redhat.com/attachment.cgi?id=300266
# https://searchcode.com/codesearch/view/7611423/
# https://searchcode.com/codesearch/raw/7611423
Patch0: fuseiso-20070708-largeiso.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fuse-devel, zlib-devel, glib2-devel
Requires: fuse

Obsoletes: fuseiso <= %{version}-%{release}
Provides: fuseiso = %{version}-%{release}

%description
Allow normal users to mount iso images with fuse. 
Supported image types are .iso, .img, .bin, .mdf and .nrg.

%prep
%setup -n %{real_name}-%{real_version}
%patch0 -p1

%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/fuseiso

%changelog
* Mon Oct 17 2016 Evgueni Souleimanov <esoule@100500.ca> - 0.0.20070708-2.101
- add fuseiso-20070708-largeiso.patch file

* Thu Apr 10 2008 Dag Wieers <dag@wieers.com> - 0.0.20070708-2
- Added largeiso patch to support ISO's larger than 4GB. (Thomas Bittermann)

* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 0.0.20070708-1
- Updated to release 20070708.

* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 0.0.20061017-1
- Initial package. (using DAR)
