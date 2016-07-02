Name:           ttt
Version:        1.8.2
Release:        2%{?dist}
Summary:        Real-time, graphical, and remote traffic monitoring tool

Group:          Applications/Internet
License:        BSD
URL:            https://www.sonycsl.co.jp/person/kjc/software.html
Source0:        http://ftp.sunet.se/mirror/archive/ftp.sunet.se/pub/network/monitoring/kjc/%{name}-%{version}.tar.gz

Patch1:         ttt-0001-fix-error-invalid-storage-class-for-function-inet6_n.patch
Patch2:         ttt-0002-remove-stale-pcap_inet.c-as-per-README.patch
Patch3:         ttt-0003-tttrelay-fix-error-struct-sockaddr_in-has-no-member-.patch
Patch4:         ttt-0004-copy-config.guess-and-config.sub-from-usr-lib-rpm-to.patch
Patch5:         ttt-0005-configure-fix-configure.in-to-compile-on-x86_64-Linu.patch
Patch6:         ttt-0006-configure-add-with-cflags-support.patch
Patch7:         ttt-0007-fix-DESTDIR-support-in-make-install-remove-cruft.patch
Patch8:         ttt-0008-Makefile.in-fix-Makefile.in-seems-to-ignore-the-data.patch
Patch9:         ttt-0009-regenerate-configure-file-using-autoconf-2.63.patch
Patch10:        ttt-0010-Balance-braces-cut-by-ifdefs-part-1.patch
Patch11:        ttt-0011-Balance-braces-cut-by-ifdefs-part-2.patch
Patch12:        ttt-0012-Allocate-buffers-of-256-bytes-for-hostnames-47-bytes.patch
Patch13:        ttt-0013-Do-not-write-beyond-allocated-buffer-in-net_getname.patch
Patch14:        ttt-0014-set-fromlen-type-to-socklen_t.patch
Patch15:        ttt-0015-set-fromlen-type-to-socklen_t.patch

BuildRequires:  blt-devel
BuildRequires:  itcl-devel
BuildRequires:  itk-devel
BuildRequires:  libpcap-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel

%description
ttt (TTT: Tele Traffic Tapper) is yet another descendant of tcpdump but
it is capable of real-time, graphical, and remote traffic-monitoring. 
ttt won't replace tcpdump, rather, it helps you find out what to look
into with tcpdump.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1


%build
CFLAGS=" %optflags -Wall -Wextra -Wformat=2 -Wformat-security -fno-strict-aliasing"

%configure --enable-ipv6 --with-cflags="${CFLAGS}"
make all ttttextview tttrelay


%install
rm -rf %{buildroot}
make install install-man install-extra DESTDIR=%{buildroot}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/ttt/*
%{_mandir}/man1/*.1.gz


%changelog
* Sat Jul 02 2016 Evgueni Souleimanov <esoule@100500.ca> - 1.8.2-2
- Fix crash when IP resolves to long hostname
- Clean up spec file

* Wed May 20 2015 Evgueni Souleimanov <esoule@100500.ca> - 1.8.2-1
- Initial package
- Fix building under CentOS 6 x86_64
