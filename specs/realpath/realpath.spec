# Authority: dag

Summary: Return the canonicalized absolute pathname
Name: realpath
Version: 1.17
Release: 1.101%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://anonscm.debian.org/gitweb/?p=users/robert/realpath.git

Source: http://www.lmona.de/files/distfiles/realpath_%{version}.tar.gz
## from https://tracker.debian.org/news/310448
Source2: realpath-sha1sums.txt
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: e2fsprogs
BuildRequires: gettext
BuildRequires: ncurses-devel
BuildRequires: zlib-devel

%description
The package contains a small utility realpath, which converts each
pathname argument to an absolute pathname, which has no components
that are symbolic links or the special .  or ..  directory entries.

This utility provides mostly the same functionality as
`/bin/readlink -f' in the coreutils package.

%prep
%setup

%build
#%{__make} %{?_smp_flags}
%{__make} %{?_smp_flags} -C src
%{__make} %{?_smp_flags} -C po/bin

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 src/_build/realpath %{buildroot}%{_bindir}/realpath
%{__install} -Dp -m0644 man/realpath.1 %{buildroot}%{_mandir}/man1/realpath.1

for file in po/bin/_build/*.mo; do
    lang=$(basename $file .mo)
    %{__install} -Dp -m0644 $file %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/realpath.mo
done
%find_lang realpath

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc debian/changelog debian/copyright
%doc %{_mandir}/man1/realpath.1*
%{_bindir}/realpath

%changelog
* Mon Oct 17 2016 Evgueni Souleimanov <esoule@100500.ca> - 1.17-1.101
- update URL to source tarball
- add checksum for the source tarball
- add gettext to BuildRequires

* Sun Sep 02 2012 Dag Wieers <dag@wieers.com> - 1.17-1
- Initial package. (using DAR)
