Name: kexec-tools
Version: 2.0.0 
Release: 286.1.101%{?dist}
License: GPLv2
Group: Applications/System
Summary: The kexec/kdump userspace component.
Source0: http://www.kernel.org/pub/linux/kernel/people/horms/kexec-tools/%{name}-%{version}.tar.bz2
Source1: kdump.init
Source2: kdump.sysconfig
Source3: kdump.sysconfig.x86_64
Source4: kdump.sysconfig.i386
Source5: kdump.sysconfig.ppc64
Source6: kdump.sysconfig.ia64
Source7: mkdumprd
Source8: kdump.conf
Source9: http://downloads.sourceforge.net/project/makedumpfile/makedumpfile/1.3.5/makedumpfile-1.3.5.tar.gz
Source10: kexec-kdump-howto.txt
Source11: firstboot_kdump.py
Source12: mkdumprd.8
Source13: kexec-tools-po.tar.gz
Source14: 98-kexec.rules
Source15: kdump.conf.5
Source16: kdump.sysconfig.s390x
Source17: eppic_030413.tar.gz

#######################################
# These are sources for mkdumprd2
# Which is currently in development
#######################################
Source100: dracut-files.tbz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(pre): coreutils chkconfig sed zlib 
Requires: busybox >= 1.2.0, dracut, bc, kpartx, mdadm, 
BuildRequires: dash 
BuildRequires: zlib-devel zlib zlib-static elfutils-devel-static glib2-devel bzip2-devel lzo-devel snappy-devel
BuildRequires: ncurses-devel bison flex
BuildRequires: pkgconfig intltool gettext 
%ifarch %{ix86} x86_64 ppc64 ia64 ppc s390x
Obsoletes: diskdumputils netdump
%endif
ExcludeArch: s390

#START INSERT

#
# Patches 0 through 100 are meant for x86 kexec-tools enablement
#
Patch1: kexec-tools-2.0.0-i686-64G-limit.patch
Patch2: kexec-tools-2.0.0-efi-bootdata.patch

#
# Patches 101 through 200 are meant for x86_64 kexec-tools enablement
#
Patch101: kexec-tools-2.0.0-fix-page-offset.patch
Patch102: kexec-tools-2.0.0-x86_64-exclude-gart.patch
Patch103: kexec-tools-2.0.0-x86-e820-acpi-reserved-add.patch
Patch104: kexec-tools-2.0.0-x86_64-ksize.patch

#
# Patches 201 through 300 are meant for ia64 kexec-tools enablement
#

#
# Patches 301 through 400 are meant for ppc64 kexec-tools enablement
#
Patch301: kexec-tools-2.0.0-ppc64-reloc.patch
Patch302: kexec-tools-2.0.0-ppc64-omnibus.patch
Patch303: kexec-tools-2.0.0-treewords.patch
Patch304: kexec-tools-2.0.0-ppc64-Respect-memory-limit-while-building-crash-memo.patch

#
# Patches 401 through 500 are meant for s390 kexec-tools enablement
#
Patch401: kexec-tools-2.0.0-makedumpfile-s390x-port.patch
Patch402: kexec-tools-2.0.0-s390x-port-full.patch
Patch403: kexec-tools-2.0.0-makedumpfile-s390x-dumb-term.patch

#
# Patches 501 through 600 are meant for ppc kexec-tools enablement
#
Patch501: kexec-tools-2.0.0-ppc-execshield.patch

#
# Patches 601 onward are generic patches
#
Patch601: kexec-tools-2.0.0-disable-kexec-test.patch
Patch602: kexec-tools-2.0.0-makedumpfile-dynamic-build.patch
Patch603: kexec-tools-2.0.0-makedumpfile-2.6.32-utsname.patch
Patch604: kexec-tools-2.0.0-makedumpfile-boption.patch
Patch605: kexec-tools-2.0.0-makedumpfile-2.6.32-sparsemem.patch
Patch606: kexec-tools-2.0.0-makedumpfile-add-missing-opts-help.patch
Patch607: kexec-tools-2.0.0-makedumpfile-use-tmpdir.patch
Patch608: kexec-tools-2.0.0-increase-segments-max.patch
Patch609: kexec-tools-2.0.0-extend-for-large-cpu-memory.patch
Patch610: kexec-tools-2.0.0-extend-kcore-elf-headers-size.patch
Patch611: kexec-tools-2.0.0-makedumpfile-remove--V-option.patch
Patch612: kexec-tools-2.0.0-x86-uv-support-many-cpu.patch
Patch613: kexec-tools-2.0.0-x86-uv-support-part2.patch
Patch614: kexec-tools-2.0.0-makedumpfile-s390x-fix-kvbase.patch
Patch615: kexec-tools-2.0.0-i386-backup-region-missed-part.patch
Patch616: kexec-tools-2.0.0-ppc-segfault-fix.patch
Patch617: kexec-tools-2.0.0-makedumpfile-Copy-correct-nr_cpus-info-to-dumpfile-during-r.patch
Patch618: kexec-tools-2.0.0-makedumpfile-Add-config-option-to-specify-filter-con.patch
Patch619: kexec-tools-2.0.0-makedumpfile-Apply-relocation-while-loading-module-d.patch
Patch620: kexec-tools-2.0.0-makedumpfile-Load-the-module-symbol-data-from-vmcore.patch
Patch621: kexec-tools-2.0.0-makedumpfile-Introduce-routines-to-get-type-name-fro.patch
Patch622: kexec-tools-2.0.0-makedumpfile-Read-and-process-filter-commands-from-c.patch
Patch623: kexec-tools-2.0.0-makedumpfile-Read-and-process-for-command-from-confi.patch
Patch624: kexec-tools-2.0.0-makedumpfile-Add-erased-information-in-compressed-kd.patch
Patch625: kexec-tools-2.0.0-makedumpfile-Add-erase-information-in-ELF-fo.patch
Patch626: kexec-tools-2.0.0-makedumpfile-backport-security-filter-feature.patch
Patch627: kexec-tools-2.0.0-makedumpfile-cleanup-man-page-section.patch
Patch628: kexec-tools-2.0.0-makedumpfile-s390x-vmalloc_start-fix.patch
Patch629: kexec-tools-2.0.0-makedumpfile-Add-sadump-module-header-file.patch
Patch630: kexec-tools-2.0.0-makedumpfile-Extend-DumpInfo-structure.patch
Patch631: kexec-tools-2.0.0-makedumpfile-Implement-command-line-processing.patch
Patch632: kexec-tools-2.0.0-makedumpfile-Verify-and-read-VMCORE-s-in-sadump-re.patch
Patch633: kexec-tools-2.0.0-makedumpfile-Export-helpers-for-bitmap-table-handl.patch
Patch634: kexec-tools-2.0.0-makedumpfile-Initialize-internal-data-according-to.patch
Patch635: kexec-tools-2.0.0-makedumpfile-Initialize-debug-information-for-ELF-.patch
Patch636: kexec-tools-2.0.0-makedumpfile-Implement-readmem-interface-on-sadump.patch
Patch637: kexec-tools-2.0.0-makedumpfile-Estimate-phys_base-based-on-linux_ban.patch
Patch638: kexec-tools-2.0.0-makedumpfile-Generate-and-save-VMCOREINFO-and-ELF-.patch
Patch639: kexec-tools-2.0.0-makedumpfile-Process-CPUs-based-on-online-ones.patch
Patch640: kexec-tools-2.0.0-makedumpfile-Read-kexec-backup-region.patch
Patch641: kexec-tools-2.0.0-makedumpfile-Add-description-of-sadump-related-for.patch
Patch642: kexec-tools-2.0.0-makedumpfile-Add-description-of-sadump-in-man.patch
Patch643: kexec-tools-2.0.0-makedumpfile-Cleanup-Convert-multiple-spaces-to-tabs.patch
Patch644: kexec-tools-2.0.0-makedumpfile-Cleanup-Fix-some-comments-for-endif.patch
Patch645: kexec-tools-2.0.0-makedumpfile-Fix-compilation-error-in-sadump_info.h.patch
Patch646: kexec-tools-2.0.0-makedumpfile-check-if-given-cpu-is-online-in-per-cpu.patch
Patch647: kexec-tools-2.0.0-backport-vmcore-dmesg.patch
Patch648: kexec-tools-2.0.0-vmcore-dmesg-Determine-correct-machine-pointer-size.patch
Patch649: kexec-tools-2.0.0-detect-Xen-dom0-properly-to-avoid-conflict-with-pv_o.patch
Patch650: kexec-tools-2.0.0-fix-Xen-detection-for-xenfs-in-pv_ops-kernel.patch
Patch651: kexec-tools-2.0.0-ppc64-dt_reserve.patch
Patch652: kexec-tools-2.0.0-makedumpfile-upgrade-to-1.5.3.patch
Patch653: kexec-tools-2.0.0-makedumpfile-Add-a-help-message-for-b-option.patch
Patch654: kexec-tools-2.0.0-makedumpfile-Cleanup-Move-the-usage-message-of-b-option-to-.patch
Patch655: kexec-tools-2.0.0-makedumpfile-Update-pfn_cyclic-when-the-cyclic-buffer-size-.patch
Patch656: kexec-tools-2.0.0-makedumpfile-Use-divideup-to-calculate-maximum-required-bit.patch
Patch657: kexec-tools-2.0.0-makedumpfile-cache-Allocate-buffers-at-initialization-t.patch
Patch658: kexec-tools-2.0.0-makedumpfile-cache-Reuse-entry-in-pending-list.patch
Patch659: kexec-tools-2.0.0-makedumpfile-Fix-max_mapnr-issue-on-system-has-over-44-b.patch
Patch660: kexec-tools-2.0.0-makedumpfile-upgrade-to-1.5.6.patch
Patch661: kexec-tools-2.0.0-makedumpfile-Introduce-the-mdf_pfn_t-type.patch
Patch662: kexec-tools-2.0.0-makedumpfile-Fix-free-bitmap_buffer_cyclic-error.patch
Patch663: kexec-tools-2.0.0-makedumpfile-Remove-the-1st-bitmap-buffer-from-the-ELF-.patch
Patch664: kexec-tools-2.0.0-makedumpfile-Move-counting-pfn_memhole-for-cyclic-mode.patch
Patch665: kexec-tools-2.0.0-makedumpfile-Stop-maximizing-the-bitmap-buffer-to-reduc.patch
Patch666: kexec-tools-2.0.0-makedumpfile-Fix-Makefile-for-eppic_makedumpfile.so-build.patch
Patch667: kexec-tools-2.0.0-makedumpfile-Generic-handling-of-multi-page-exclusio.patch
Patch668: kexec-tools-2.0.0-makedumpfile-Get-rid-of-overrun-adjustments.patch
Patch669: kexec-tools-2.0.0-makedumpfile-Initialize-for-vmalloc-address-translat.patch
Patch670: kexec-tools-2.0.0-makedumpfile-vtop-address-translation-support-for-vm.patch
Patch671: kexec-tools-2.0.0-makedumpfile-Exclude-unnecessary-hugepages.patch
Patch672: kexec-tools-2.0.0-makedumpfile-sadump-Support-more-than-16TB-physical-memory.patch

%description
kexec-tools provides /sbin/kexec binary that facilitates a new
kernel to boot using the kernel's kexec feature either on a
normal or a panic reboot. This package contains the /sbin/kexec
binary and ancillary utilities that together form the userspace
component of the kernel's kexec feature.

%ifarch %{ix86} x86_64 ppc64 s390x
%package eppic
Requires: %{name} = %{version}-%{release}
Summary: Additional eppic_makedumpfile.so shared object
Group: Applications/System

%description eppic
The eppic_makedumpfile.so shared object is loaded by the
"makedumpfile --eppic" option, and is used to erase sensitive
or confidential kernel data from a dumpfile.
%endif

%prep
%setup -q 

mkdir -p -m755 kcp
tar -z -x -v -f %{SOURCE9}
%patch1 -p1
%patch2 -p1

%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1

%patch301 -p1
%patch302 -p1
%patch303 -p1
%patch304 -p1

%patch401 -p1
%patch402 -p1
%patch403 -p1

%patch501 -p1

%patch601 -p1
%patch602 -p1 %{?_rawbuild}
%patch603 -p1
%patch604 -p1
%patch605 -p1
%patch606 -p1
%patch607 -p1
%patch608 -p1
%patch609 -p1
%patch610 -p1
%patch611 -p1
%patch612 -p1
%patch613 -p1
%patch614 -p1
%patch615 -p1
%patch616 -p1
%patch617 -p1
%patch618 -p1
%patch619 -p1
%patch620 -p1
%patch621 -p1
%patch622 -p1
%patch623 -p1
%patch624 -p1
%patch625 -p1
%patch626 -p1
%patch627 -p1
%patch628 -p1
%patch629 -p1
%patch630 -p1
%patch631 -p1
%patch632 -p1
%patch633 -p1
%patch634 -p1
%patch635 -p1
%patch636 -p1
%patch637 -p1
%patch638 -p1
%patch639 -p1
%patch640 -p1
%patch641 -p1
%patch642 -p1
%patch643 -p1
%patch644 -p1
%patch645 -p1
%patch646 -p1
%patch647 -p1
%patch648 -p1
%patch649 -p1
%patch650 -p1
%patch651 -p1
%patch652 -p0
%patch653 -p1
%patch654 -p1
%patch655 -p1
%patch656 -p1
%patch657 -p1
%patch658 -p1
%patch659 -p1
%patch660 -p0
%patch661 -p1
%patch662 -p1
%patch663 -p1
%patch664 -p1
%patch665 -p1
%patch666 -p1
%patch667 -p1
%patch668 -p1
%patch669 -p1
%patch670 -p1
%patch671 -p1
%patch672 -p1

tar -z -x -v -f %{SOURCE13}
tar -z -x -v -f %{SOURCE17}

%ifarch ppc
%define archdef ARCH=ppc
%endif

%build
%ifarch ia64
# ia64 gcc seems to have a problem adding -fexception -fstack-protect and
# -param ssp-protect-size, like the %configure macro does
# while that shouldn't be a problem, and it still builds fine, it results in
# the kdump kernel hanging on kexec boot.  I don't yet know why, but since those
# options aren't critical, I'm just overrideing them here for ia64
export CFLAGS="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2"
%endif

%configure \
%ifarch ppc64
    --host=powerpc64-redhat-linux-gnu \
    --build=powerpc64-redhat-linux-gnu \
%endif
    --sbindir=/sbin
rm -f kexec-tools.spec.in
# setup the docs
cp %{SOURCE10} . 

%ifarch %{ix86} x86_64 ia64 ppc64 s390x
make -C eppic/libeppic
make -C makedumpfile-1.3.5 LINKTYPE=dynamic USELZO=on USESNAPPY=on
make -C makedumpfile-1.3.5 LDFLAGS="-I../eppic/libeppic -L../eppic/libeppic" eppic_makedumpfile.so
%endif
make
make -C kexec-tools-po

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
mkdir -p -m755 $RPM_BUILD_ROOT%{_localstatedir}/crash
mkdir -p -m755 $RPM_BUILD_ROOT%{_mandir}/man8/
mkdir -p -m755 $RPM_BUILD_ROOT%{_mandir}/man5/
mkdir -p -m755 $RPM_BUILD_ROOT%{_docdir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_datadir}/kdump
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
mkdir -p -m755 $RPM_BUILD_ROOT/usr/sbin
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d/kdump

SYSCONFIG=$RPM_SOURCE_DIR/kdump.sysconfig.%{_target_cpu}
[ -f $SYSCONFIG ] || SYSCONFIG=$RPM_SOURCE_DIR/kdump.sysconfig.%{_arch}
[ -f $SYSCONFIG ] || SYSCONFIG=$RPM_SOURCE_DIR/kdump.sysconfig
install -m 644 $SYSCONFIG $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/kdump

install -m 755 %{SOURCE7} $RPM_BUILD_ROOT/sbin/mkdumprd
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/kdump.conf
install -m 644 kexec/kexec.8 $RPM_BUILD_ROOT%{_mandir}/man8/kexec.8
install -m 755 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/kdump/firstboot_kdump.py
install -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_mandir}/man8/mkdumprd.8
%ifnarch s390x
# For s390x the ELF header is created in the kdump kernel and therefore kexec
# udev rules are not required
install -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/98-kexec.rules
%endif
install -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{_mandir}/man5/kdump.conf.5

%ifarch %{ix86} x86_64 ia64 ppc64 s390x
install -m 755 makedumpfile-1.3.5/makedumpfile $RPM_BUILD_ROOT/usr/sbin/makedumpfile
install -m 644 makedumpfile-1.3.5/makedumpfile.8.gz $RPM_BUILD_ROOT/%{_mandir}/man8/makedumpfile.8.gz
install -m 755 makedumpfile-1.3.5/eppic_makedumpfile.so $RPM_BUILD_ROOT/%{_libdir}/eppic_makedumpfile.so
mkdir -p $RPM_BUILD_ROOT/usr/share/makedumpfile/eppic_scripts/
install -m 644 makedumpfile-1.3.5/eppic_scripts/* $RPM_BUILD_ROOT/usr/share/makedumpfile/eppic_scripts/
%endif
make -C kexec-tools-po install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

# untar the dracut package
mkdir -p -m755 $RPM_BUILD_ROOT/etc/kdump-adv-conf
tar -C $RPM_BUILD_ROOT/etc/kdump-adv-conf -jxvf %{SOURCE100}

#and move the custom dracut modules to the dracut directory
mkdir -p $RPM_BUILD_ROOT/usr/share/dracut/modules.d/
mv $RPM_BUILD_ROOT/etc/kdump-adv-conf/kdump_dracut_modules/* $RPM_BUILD_ROOT/usr/share/dracut/modules.d/

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch /etc/kdump.conf
/sbin/chkconfig --add kdump
# This portion of the script is temporary.  Its only here
# to fix up broken boxes that require special settings 
# in /etc/sysconfig/kdump.  It will be removed when 
# These systems are fixed.

if [ -d /proc/bus/mckinley ]
then
	# This is for HP zx1 machines
	# They require machvec=dig on the kernel command line
	sed -e's/\(^KDUMP_COMMANDLINE_APPEND.*\)\("$\)/\1 machvec=dig"/' \
	/etc/sysconfig/kdump > /etc/sysconfig/kdump.new
	mv /etc/sysconfig/kdump.new /etc/sysconfig/kdump
elif [ -d /proc/sgi_sn ]
then
	# This is for SGI SN boxes
	# They require the --noio option to kexec 
	# since they don't support legacy io
	sed -e's/\(^KEXEC_ARGS.*\)\("$\)/\1 --noio"/' \
	/etc/sysconfig/kdump > /etc/sysconfig/kdump.new
	mv /etc/sysconfig/kdump.new /etc/sysconfig/kdump
fi

%postun

if [ "$1" -ge 1 ]; then
	/sbin/service kdump condrestart > /dev/null 2>&1 || :
fi

%preun
if [ "$1" = 0 ]; then
	/sbin/service kdump stop > /dev/null 2>&1 || :
	/sbin/chkconfig --del kdump
fi
exit 0

%triggerin -- firstboot
# we enable kdump everywhere except for paravirtualized xen domains; check here
if [ -f /proc/xen/capabilities ]; then
	if [ -z `grep control_d /proc/xen/capabilities` ]; then
		exit 0
	fi
fi
if [ ! -e %{_datadir}/firstboot/modules/firstboot_kdump.py ]
then
	ln -s %{_datadir}/kdump/firstboot_kdump.py %{_datadir}/firstboot/modules/firstboot_kdump.py
fi

%triggerin -- kernel-kdump
touch %{_sysconfdir}/kdump.conf

%triggerin -- fence-agents
/sbin/service kdump condrestart
exit 0

%triggerun -- firstboot
rm -f %{_datadir}/firstboot/modules/firstboot_kdump.py

%triggerpostun -- kernel kernel-xen kernel-debug kernel-PAE kernel-kdump
# List out the initrds here, strip out version nubmers
# and search for corresponding kernel installs, if a kernel
# is not found, remove the corresponding kdump initrd

#start by getting a list of all the kdump initrds
MY_ARCH=`uname -m`
if [ "$MY_ARCH" == "ia64" ]
then
	IMGDIR=/boot/efi/efi/redhat
else
	IMGDIR=/boot
fi

for i in `ls $IMGDIR/initrd*kdump.img 2>/dev/null`
do
	KDVER=`echo $i | sed -e's/^.*initrd-//' -e's/kdump.*$//'`
	if [ ! -e $IMGDIR/vmlinuz-$KDVER ]
	then
		# We have found an initrd with no corresponding kernel
		# so we should be able to remove it
		rm -f $i
	fi
done

%files -f %{name}.lang
%defattr(-,root,root,-)
/sbin/*
%ifarch %{ix86} x86_64 ia64 ppc64 s390x
/usr/sbin/*
%endif
%{_datadir}/kdump
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/kdump
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/kdump.conf
%{_sysconfdir}/kdump-adv-conf/kdump_initscripts/
%{_sysconfdir}/kdump-adv-conf/kdump_sample_manifests/
%config %{_sysconfdir}/rc.d/init.d/kdump
%ifnarch s390x
%config %{_sysconfdir}/udev/rules.d/*
%endif
%{_datadir}/dracut/modules.d/*
%dir %{_localstatedir}/crash
%{_mandir}/man5/*
%{_mandir}/man8/*
%doc News
%doc COPYING
%doc TODO
%doc kexec-kdump-howto.txt

%ifarch %{ix86} x86_64 ppc64 s390x
%files eppic
%{_libdir}/eppic_makedumpfile.so
/usr/share/makedumpfile/eppic_scripts/
%endif

%changelog
* Sun Jan 31 2016 Evgueni Souleimanov <esoule@100500.ca> - 2.0.0-286.1.101
- fix mkdumprd errors (due to /etc/mtab symbolic link to /proc/self/mounts)
  "/sbin/mkdumprd: line *: test: /sbin/fsck.rootfs: binary operator expected"
  and "fsck.rootfs \n ext3 not found".

* Tue Jun 02 2015 Baoquan He <bhe@redhat.com> - 2.0.0-286
- update kexec-kdump-howto.txt, resolves bug 949376
- mkdumprd: Load the mlx4_core module if it is needed in the 2nd kernel, resolves bug 1099589
- nfs dump will fail when netdev has different device name in ifcfg-$dev, resolves bug 1005141 
- udev-rules: Restart kdump service on cpu ADD/REMOVE events, resolves bug 1113276

* Wed Apr 15 2015 Baoquan He <bhe@redhat.com> - 2.0.0-285
- kdump.sysconfig.x86_64: Add acpi_no_memhotplug to kdump kernel, resolves bug 1208490

* Thu Mar 26 2015 Baoquan He <bhe@redhat.com> - 2.0.0-284
- sadump: Support more than 16TB physical memory space, resolves bug 1195601

* Wed Mar 11 2015 Baoquan He <bhe@redhat.com> - 2.0.0-283
- makedumpfile: Exclude unnecessary hugepages. resolves bug 1068674
- makedumpfile: Vtop address translation support for vmalloc region in PPC64 arch. resolves bug 1068674
- makedumpfile: Initialize for vmalloc address translation support in PPC64 arch. resolves bug 1068674
- makedumpfile: Get rid of overrun adjustments. resolves bug 1068674
- makedumpfile: Generic handling of multi-page exclusions. resolves bug 1068674

* Mon Mar 09 2015 Baoquan He <bhe@redhat.com> - 2.0.0-282
- mkdumprd: Delete the dead code for blacklist, resolves bug 971017

* Mon Jan 12 2015 Baoquan He <bhe@redaht.com> - 2.0.0-281
- starting kdump service after network, local fs and remote fs, resolves bug 1132300
- Add sample eppic scripts to kexec-tools-eppic package, resolves bug 1104837
- Convert leftover "getent hosts" to "getent ahostsv4", resolves bug 1142666
- mkdurmpd: Fix the syntax error on the condition of fips inexistence, resolves bug 1131945

* Wed Aug 27 2014 Baoquan He <bhe@redhat.com> - 2.0.0-280
- mkdumprd: wait for multipath device node, resolves bug 1128248
- mkdumprd: clean up found logic in wait_for_multipath_devices(), resolves bug 1128248
- use "getent ahostsv4 host-name" to get ipv4 address of a host name, resolves bug 1127138


* Tue Aug 12 2014 Baoquan He <bhe@redhat.com> - 2.0.0-279
- mkdurmpd: Issue sync after saving vmcore-dmesg.txt, resolves bug 1123061
- mkdumprd: Fix check condition of selinux status, resolves bug 1122880
- mkdumprd: fix no such file or directory warning in 2nd kernel on s390, resolves bug 1122883
- Support for eppic language as a subpackage, resolves bug 823561
- update .gitignore/sources for eppic_030413.tar.gz, resolves bug 823561
- makedumpfile: Fix Makefile for eppic_makedumpfile.so build, resolves bug 823561

* Mon Jul 21 2014 Baoquan He <bhe@redhat.com> - 2.0.0-278
- Stop maximizing the bitmap buffer to reduce the risk of OOM, resolves bug 1114153
- Move counting pfn_memhole for cyclic mode, resolves bug 1114153
- Remove the 1st bitmap buffer from the ELF path in cyclic mode, resolves bug 1114153
- Fix free bitmap_buffer_cyclic error, resolves bug 1114153
- Introduce the mdf_pfn_t type, resolves bug 1114153

* Fri Jun 20 2014 Baoquan He <bhe@redhat.com> - 2.0.0-277
- mkdumprd: add support for s390 DASD FBA type device, resolves bug 1022871
- Check status of fsck before trying to mount a file system, resolves bug 1055672

* Thu Jun 19 2014 Baoquan He <bhe@redhat.com> - 2.0.0-276
- kexec-tools: non-default routes are ignored by kdump, resolves bug 806992
- kdumpctl: Pass disable_cpu_apicid to kexec of capture kernel, resolves bug 1061480
- use -p option with fsck instead of -y, resolves bug 1055679
- kdump doesn't work properly with nic that has "-" in it's name, resolves bug 874529
- fix makedumpfile report and debug messages not shown, resolves bug 1016451

* Fri May 30 2014 Baoquan He <bhe@redhat.com> - 2.0.0-275
- makedumpfile: Upgrade from v1.5.3 to v1.5.6, resolves bug 929312

* Tue May 27 2014 Baoquan He <bhe@redhat.com> - 2.0.0-274
- Add fence_kdump support for generic clusters, resolves bug 1083938
- Add function setup_cluster_nodes_and_options, resolves bug 1083938
- Add function get_pcs_cluster_nodes, resolves bug 1083938
- Add function is_pcs_fence_kdump, resolves bug 1083938

* Tue Oct 22 2013 Baoquan He <bhe@redhat.com> - 2.0.0-273
- Fix max_mapnr issue on system has over 44-bit addressing, resolves bug 1008543
- makedumpfile: fails phys_base calculation on sadump format, resolves bug 1010103

* Wed Oct 16 2013 Baoquan He <bhe@redhat.com> - 2.0.0-272
- Allow multipathd to configure multipath map before adding partition devmappings, resolves bug 906601
- mkdumprd: use timeout_count as a global variable, resolves bug 906601
- mkdumprd: add support for SCM devices available for Linux on System z, resolves bug 903529
- kdump.init: Run multiple kdump init instances one by one in serial order, resolves bug 963948

* Mon Oct 14 2013 Baoquan He <bhe@redhat.com> - 2.0.0-271
- makedumpfile: wrong cyclic buffer size recalculation causes bitmap data corruption, resolves bug 1009207

* Wed Oct 09 2013 Baoquan He <bhe@redhat.com> - 2.0.0-270
- mkdumprd: strip_comments is not implemented correcty, resolves bug 1015764

* Fri Sep 13 2013 Baoquan He <bhe@redhat.com> - 2.0.0-269
- add snappy build, resolves bug 902147
- This patch fixes the parsing of inline comments in config file, resolves bug 967427

* Fri Sep 13 2013 Dave Young <dyoung@redhat.com> - 2.0.0-268
- Revert mkdumprd: Remove redundant code from handled, resolves bug 1007230

* Wed Aug 14 2013 Baoquan He <bhe@redhat.com> - 2.0.0-267
- mkdumprd: improve error message when e2fsprogs is missing, resolves bug 975642
- mkdumprd: improve error message when btrfs-progs is missing, resolves bug 810494
- Document mkdumprd option --allow-missing, resolves bug 951035

* Thu Aug 1 2013 Baoquan He <bhe@redhat.com> - 2.0.0-266
- kdump.conf.5: Modify 2 spelling errors
- kexec-tools: Only remap network once when cluster configured
- tools: Clean up /etc/iface_map after remapping the devices
- kernel cmdline: Remove hugepage allocations
- mkdumprd: change default disk_timeout to 180 seconds
- kdump.conf: Tell user to specify module without ".ko" suffix
- kdump.conf: add some missing supported configurations from kdump.conf.5
- kdump.conf: change line columns to 80
- Raw dump: use /sbin/blockdev to flush out block device buffers
- Update translation file for firstboot
- Update translation file for firstboot

* Thu Jul 4 2013 Baoquan He <bhe@redhat.com> - 2.0.0-265
- add selinux relabel when service startup, resolve bug 797231
- add bzip2-devel and lzo-devel to BuildRequires, resolve bug 825476

* Thu Jul 4 2013 Baoquan He <bhe@redhat.com> - 2.0.0-264
- kexec-tools.spec: turn on the dynamic and lzo build for makedumpfile, resolve bug 825476
- kexec-tools.spec: Validate patches related to makedumpfile, resolve bug 825476

* Thu Jul 4  2013 Baoquan He <bhe@redhat.com> - 2.0.0-263
- Add a help message into man page of makedumpfile for -b option, resolve bug 825476
- makedumpfile: add a big patch to upgrade from v1.3.5 to v1.5.3, resolve bug 825476
- add missing logs for makedumpfile patches, resolve bug 825476
- RHEL6.4 PATCH Use conditional restart when adding or removing CPU/Memory, resolve bug 883543
- mkdumprd: add tab key as delimiter of core_collector in kdump.conf, resolve bug 852373

* Tue May 14 2013 Baoquan He <bhe@redhat.com> - 2.0.0-262
- kexec-tools: Allow kdump over a network work with an arbitrary bridge, bond or vlan name , resolve bug 959449
- Add files related to fips support , resolve bug 909402
- Change the old copy of symlink file , resolve bug 909402
- kdump.conf: the location of makedumpfile is said wrongly , resolve bug 847247
- Revert no-udev lvm.conf changes , resolve bug 888609

* Tue May 7 2013 Baoquan He <bhe@redhat.com> - 2.0.0-261
- kexec: Respect memory limit while building crash memory ranges on ppc64, resolve bug 871522 
- modprobe output awkscripts fix, resolve bug 876667 
- kdump.init: exit and print error if kernel is old but using nr_cpus=1, resolve bug 844572
- kdump.conf.5: the location of makedumpfile is said wrongly, resolve bug 847247
- mkdumprd: remove redundant code of checkinging IS_UUID/IS_LABEL for lvm PV Name, resolve bug 879471
- mkdumprd: handlelvordev cleanup, resolve bug 879471

* Thu Apr 11 2013 Baoquan He <bhe@redhat.com> - 2.0.0-260
- kexec-tools: powerpc: dt_reserve doesn't allocate enough memory for large properties
- mkdumprd: check for empty dasd options
- mkdumprd: Remove redundant code from handledm()

* Mon Mar 25 2013 Baoquan He <bhe@redhat.com> - 2.0.0-259
- kexec-tools: Map network devices based on MAC address
- kexec-tools: Allow mkdumprd modules blacklist to be overwritten by extra_modules
- Add description about default action 'mount_root_run_init' and 'poweroff'
- check_encrypted fix
- add virtio disk identify logic
- Add scsi_id disk identify logic
- move scsi_id install to a function
- move identify critical disk logic to a function

* Fri Jan 18 2013 Dave Young <dyoung@redhat.com> - 2.0.0-258
- mkdumprd: Fix iface substitution in cfg files, resolve bug 892703

* Wed Dec 19 2012 Dave Young <dyoung@redhat.com> - 2.0.0-257
- Document supported, unsupported, unknown/tech-preview dump targets, resolve bug 878200

* Tue Dec 11 2012 Dave Young <dyoung@redhat.com> - 2.0.0-256
- mkdumprd: Set DM_DISABLE_UDEV=1 to tell libdevmapper that there is no udev, resolve bug 880040

* Thu Dec 6 2012 Dave Young <dyoung@redhat.com> - 2.0.0-255
- make the SCSI dump target work with Linux on System z, resolve bug 870957
- extract Linux on System z device init into separate functions, resolve bug 870957
- remove hwclock calls for Linux on System z, resolve bug 821376

* Wed Nov 28 2012 Dave Young <dyoung@redhat.com> - 2.0.0-254
- blacklist IB module mlx4_core.ko, resolve bug 876891
- create bonding device dynamiclly, resolve bug 859824

* Tue Nov 20 2012 Dave Young <dyoung@redhat.com> - 2.0.0-253
- pull in two patches for xen domU detection, resolve bug 872086

* Fri Nov 16 2012 Dave Young <dyoung@redhat.com> - 2.0.0-252
- remove hardcode for including ata_generic driver, resolve bug 820474
- mkdumprd: Fix /dev/mapper/* links not being created by default, resolve bug 874832
- vmcore-dmesg: Determine correct machine pointer size, resolve bug 871292

* Mon Nov 5 2012 Dave Young <dyoung@redhat.com> - 2.0.0-251
- Add ip prefix to crash directory name for mount_root_run_init, resolve bug 871663

* Mon Oct 15 2012 Dave Young <dyoung@redhat.com> - 2.0.0-250
- mkdumprd: Support line mode terminals for s390x, resolve bug 818645
- Fix kdump documentation about vmcore-dmesg handling, resolve bug 850623

* Fri Oct 12 2012 Dave Young <dyoung@redhat.com> - 2.0.0-249
- improve warning message for remain size checking, resolve bug 857282
- propagate_ssh_key remove selinux flips for ssh key generation, resolve bug 816467
- random feeding fix, resolve bug 825640
- do not print error when there's no vendor-model-type, resolve bug 801344, bug 628610

* Thu Sep 06 2012 Dave Young <dyoung@redhat.com> - 2.0.0-248
- Exclude microcode kernel module, resolve bug 788253
- Exclude virtio_balloon kernel module, resolve bug 770000

* Thu Aug 30 2012 Dave Young <dyoung@redhat.com> - 2.0.0-247
- Save vmcore-dmesg.txt before saving vmcore, resolve bug 850623

* Fri Aug 24 2012 Dave Young <dyoung@redhat.com> - 2.0.0-246
- Do not run default/final action if network interface fails to come up, resolve bug 822146
- Move default action handling code in a separate function, resolve bug 822146
- Append to /etc/iface_to_active file instead of overwriting, resolve bug 822146
- Allow activation of more than one network interface in second kernel, resolve bug 822146
- always find and install the fs module for local fs dump, resolve bug 842476
- document the supported fs types, resolve bug 813354

* Fri May 25 2012 Dave Young <dyoung@redhat.com> - 2.0.0-245
- deal with nic renaming of bridge member, resolve bug 821930

* Wed May 16 2012 Dave Young <dyoung@redhat.com> - 2.0.0-244
- use uuid instead of device name for default dump target, resolve bug 814629

* Fri May 4 2012 Dave Young <dyoung@redhat.com> - 2.0.0-243
- add s390x specific setup for network devices, resolve bug 812816

* Wed May 2 2012 Dave Young <dyoung@redhat.com> - 2.0.0-242
- add s390x support in firstboot, resolve bug 805040
- deal with s390x threshold in firstboot, resolve bug 805040 

* Mon Apr 23 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-241
- Support sadump dump formats in makedumpfile, resolve bug 736886

* Thu Apr 12 2012 Dave Young <dyoung@redhat.com> - 2.0.0-240
- remove xen_emul_unplug cmdline appending, resolve bug 798886

* Wed Apr 11 2012 Dave Young <dyoung@redhat.com> - 2.0.0-239
- s390: unblock and bring online storage devices, resolve bug 805464

* Tue Apr 10 2012 Dave Young <dyoung@redhat.com> - 2.0.0-238
- only add xen_emul_unplug cmdline for i386 and x86_64, resolve bug 798886

* Fri Apr 06 2012 Dave Young <dyoung@redhat.com> - 2.0.0-237
- Several fixes for xem hvm kdump, resolve bug 798886

* Wed Apr 04 2012 Dave Young <dyoung@redhat.com> - 2.0.0-236
- Warn when dumping to encrypted devices, resolve bug 743551
- Correct the meaning of BOOTPROTO=none, resolve bug 805803

* Fri Mar 30 2012 Dave Young <dyoung@redhat.com> - 2.0.0-235
- enable xen hvm guest without pv drivers, resolve bug 798886

* Fri Mar 30 2012 Dave Young <dyoung@redhat.com> - 2.0.0-234
- Clarify scp as core_collector, resolve bug 805793

* Fri Mar 30 2012 Dave Young <dyoung@redhat.com> - 2.0.0-233
- Clarify the kdump.conf documentation, resolve bug 805793
- uncomment the default core_collector and path, resolve bug 805793
- fix module finding logic, resolve bug 794580

* Mon Mar 26 2012 Dave Young <dyoung@redhat.com> - 2.0.0-232
- add nfs4 support, add nfs, ssh and deprecate net option, resolve bug 795804

* Mon Mar 26 2012 Dave Young <dyoung@redhat.com> - 2.0.0-231
- remote dumping fix for restricted shell on remote machine, resolve bug 801497 

* Wed Mar 21 2012 Dave Young <dyoung@redhat.com> - 2.0.0-230
- Update firstboot threshold to 2G and roundup memsize value, resolve bug 802201
- convert PREFIX to NETMASK for the second kernel, resolve bug 699318

* Wed Mar 7 2012 Dave Young <dyoung@redhat.com> - 2.0.0-229
- clarify "insufficient memory" in firstboot kdump module, resolve bug 799529 
- mkdumprd: call add_rootfs early, resolve bug 799231
- Do not depend on selinuxcoreutils, resolve bug 697657

* Thu Mar 1 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-228
- Obtain the vmalloc_start value from high_memory for s390x arch,
  resolve bug 782674.

* Thu Mar 1 2012 Dave Young <dyoung@redhat.com> - 2.0.0-227
- Fix the default dump failure option, resolve bug 729675.
- Add default console font, resolve bug 784114.
- Set pipefail at the beginning of init, resolve bug 771671.
- Some bug fixes for raw dump, resolve bug 794981.

* Tue Feb 21 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-226
- Fix some issues in NFS dump, resolve bug 785264.

* Tue Feb 21 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-225
- Support dump over vlan tagged bonding, fix bug 752458.

* Fri Feb 17 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-224
- Disable MCE for the second kernel on x86_64, fix bug 761488.

* Thu Feb 9 2012 Dave Young <dyoung@redhat.com> - 2.0.0-223
- Make clear comment about the default action, fix bug 743231

* Wed Feb 1 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-222
- Add missing "shell" in kexec-kdump-howto.txt, fix bug 770757.

* Sun Jan 29 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-221
- Fix a typo in patch for bug 738866.

* Sun Jan 29 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-220
- Makedumpfile enhancement to filter out specific kernel data.
  Resolve bug 694498.

* Sat Jan 28 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-219
- Avoid recursive directory deletion when unmount failed.
  Resolve bug 781919.

* Fri Jan 20 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-218
- Use hush instead of msh, resolve bug 782288.

* Mon Jan 16 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-217
- Copy correct nr_cpus info to dumpfile during re-filtering,
  resolve bug 748654.

* Fri Jan 6 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-216
- Don't add default gateway when there is none, resolve bug 759003.

* Fri Jan 6 2012 Amerigo Wang <amwang@redhat.com> - 2.0.0-215
- Do sync after creating kdump initrd, resolve bug 753756.

* Fri Dec 30 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-214
- Fix path for ext3 targets in kdump.conf manpage, from Dave Maley.
  Resolve bug 755760.

* Mon Dec 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-213
- Do not load iwlwifi and sound modules into kdump initrd.
  Resolve bug 635583 and bug 726086.

* Mon Dec 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-212
- Add two stage dumper framework to s390x, from Michael Holzheu.
  Resolve bug 738866.

* Fri Dec 16 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-211
- Add multipath support, from Vivek Goyal. Resolve bug 727413.

* Fri Dec 16 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-210
- Add iscsi support, from Vivek Goyal. Resolve bug 738290.

* Tue Nov 8 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-209
- Improve debugfs mounting code, from Dave Young.
  Resolve bug 748748.

* Wed Oct 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-208
- Search DUP firmware directory too, from Caspar Zhang.
  Resolve bug 747233.

* Wed Oct 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-207
- Don't run kdump service on s390x, from Caspar Zhang.
  Resolve bug 746207.

* Mon Oct 24 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-206
- Fix some security flaws, resolve bug 743165.

* Thu Oct 6 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-205
- Fix a scriptlet failure in fence-agents, resolve bug 739050.

* Mon Sep 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-204
- Add new config "force_rebuild", resolve bug 598067.

* Wed Sep 21 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-203
- Warn users to use maxcpus=1 instead of nr_cpus=1 for older
  kernels, resolve bug 727892.

* Mon Sep 19 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-202
- Pass "noefi acpi_rsdp=X" to the second kernel, resolve bug 681796.

* Sat Sep 17 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-201
- Include patch 602 for rawbuild, resolve bug 708503.

* Wed Sep 14 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-200
- Remove the warning for reserved memory on x86, resolve BZ 731394.

* Wed Aug 31 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-199
- Add debug_mem_level debugging option, from Jan Stancek.
  Resolve Bug 734528.

* Wed Aug 31 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-198
- Fix the error message on /etc/cluster_iface,
  resolve bug 731236. From Ryan O'Hara.

* Tue Aug 16 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-197
- Add coordination between kdump and cluster fencing for long
  kernel panic dumps, resolve bug 585332. From Ryan O'Hara.

* Mon Aug 1 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-196
- Use nr_cpus=1 instead of maxcpus=1 on x86, resolve Bug 725484.

* Tue Jul 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-195
- Fix segfault on ppc machine with 1TB memory, resolve Bug 709441.

* Tue Jul 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-194
- Specify kernel version for every modprobe, resolve Bug 719105.

* Tue Jul 26 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-193
- Don't handle raid device specially, resolve Bug 707805.

* Fri Jul 8 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-192
- Read mdadm.conf correctly, resolve Bug 707805.

* Thu Jun 30 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-191
- Use makedumpfile as default core_collector for ssh dump.
  Resolve Bug 693025.

* Mon Jun 27 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-190
- Revert the previous patch, resolve Bug 701339.

* Mon Jun 20 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-189
- Disable THP in kdump kernel, resolve Bug 701339.

* Wed Apr 27 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-188
- Add the missing i386 part in the backup region patch.

* Wed Apr 27 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-187
- Remove the warning of missing netmask, resolve Bug 627834.

* Thu Apr 14 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-186
- Add "MKDUMPRD_ARGS" config, resolve Bug 692685.

* Wed Apr 13 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-185
- Add "--override-resettable" parameter, resolve Bug 692685.

* Fri Apr 8 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-184
- Handle UUID on lvm correctly, resolve Bug 693015.

* Wed Apr 6 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-183
- Fix the patch in -180, resolve Bug 692264.

* Tue Apr 5 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-182
- Pass full rootdev path to udevadm, resolve Bug 674893.

* Tue Apr 5 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-181
- Fix KVBASE to correct value for s390x arcitecture.
  Resolve Bug 692449.

* Tue Apr 5 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-180
- Don't check tmpfs for temporary directories, resolve Bug 692264.

* Thu Mar 31 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-179
- Fix the patch in -172, resolve Bug 607400.

* Wed Mar 30 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-178
- Fix the patch in -173, resolve Bug 627834.

* Wed Mar 30 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-177
- Put an error when rootfs is used and it is not resettable.
  Resolve bug 674893.

* Wed Mar 30 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-176
- Avoid loading rootfs when possible, resolve bug 674893.

* Fri Mar 25 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-175
- Fix the hpsa case, resolve bug 674893.

* Tue Mar 22 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-174
- Check non-resettable devices, resolve bug 674893.

* Mon Mar 21 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-173
- Don't check netmask for bridge or bonding interfaces. 
  Resolve Bug 627834.

* Mon Mar 21 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-172
- Add UV support, extend for large cpu count and memory.
  Resolve Bug 607400.

* Thu Mar 17 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-171
- Take closing the reboot dialog as no, resolve bug 688150.

* Thu Mar 17 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-170
- Configure kdump in firstboot, from Neil Horman.
  Resolve bug 598064.

* Thu Mar 10 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-169
- Fix a typo in monitor_dd_progress, resolve bug 683713.

* Thu Mar 10 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-168
- Use makedumpfile as the default core collector for raw dump,
  resolve bug 683735.

* Tue Mar 1 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-167
- Fix makedumpfile -V segfault, resolve bug 680741.

* Wed Feb 23 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-166
- Update ru.po, resolve bug 679310.

* Fri Feb 11 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-165
- Handle new crashkernel= syntax in firstboot.
  Resolve bug 676758.

* Fri Feb 4 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-164
- Re-upload kexec-tools-po.tar.gz.

* Thu Jan 27 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-163
- Don't use "rev" to identify a disk. Resolve bug 671013.

* Mon Jan 24 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-162
- Use TMPDIR for all commands invoked. Resolve bug 669655.

* Fri Jan 21 2011 Amerigo Wang <amwang@redhat.com> - 2.0.0-161
- Update ml.po. Resolve bz 630305.

* Tue Nov 30 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-160
- Fixed buffer size for ppc devtree, from Neil Horman.
  Resolve bz 642735.

* Mon Nov 29 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-159
- Add blacklist directive to man page (bz 619682)

* Thu Nov 25 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-158
- Rename the core to .flat only when makedumpfile is specified.
  Resolve bz 652191.

* Thu Nov 25 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-157
- Respect "path" in kdump.init. Resolve bz 626746.

* Thu Nov 25 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-156
- Add support for s390x, from Mahesh. Resolve bz 632709.

* Thu Nov 18 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-155
- Check raw partition in kdump.init, from Martin Wilck.
  Resolve bz 605411.

* Thu Nov 18 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-154
- Check if reserving memory succeeds before showing error dialog.
  Resolve bz 654245.

* Wed Nov 17 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-153
- Deselect kdump enable checkbox in firstboot when no enough memory.
  Resolve bz 652724.

* Thu Nov 11 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-152
- Fix ppc file globbing (bz 627118)

* Thu Nov 11 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-151
- moved makedumpfile to /usr/sbin (bz 627118)

* Wed Nov 03 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-150
- Extend kcore elf headers size, bz 645441.

* Wed Nov 03 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-149
- Add "extra_bins /bin/cp" into comments lines of kdump.conf.
  bz 628827.

* Tue Nov 02 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-148
- Fix untranslated strings in firstboot_kdump.py, from Parag.
  bz 626318.

* Tue Nov 02 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-147
- Fix udhcpc script NAK handling, bz 642855.

* Tue Nov 02 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-146
- Fix mkdumprd hang, bz 626606.

* Mon Aug 30 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-145
- Fixing typo, bz 627747

* Mon Aug 30 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-144
- Fix install to not fail on xen domU, see bz 627747

* Wed Aug 25 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-143
- Prevent installation on xen guests. See bug 608320.

* Thu Aug 19 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-142
- Use stat -f to get fs type instead of df -T. See bug 609814.

* Thu Aug 19 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-141
- Check write permission of all possible tmp dirs. See bug 609814.

* Thu Aug 19 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-140
- Fix storage driver discovery when device label is used,
  resolve bug 621162.

* Fri Aug 13 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-139
- Don't rename ld.so.cache, use -N instead. resolve bug 609814.

* Thu Aug 12 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-138
- Fix udhcpc hang when bridge is used, resolve bug 602325.

* Wed Aug 11 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-137
- Extend for large cpu count and memory, resolves bug 607400.

* Wed Aug 11 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-136
- Increase segments max, resolves bug 615281.

* Tue Aug 10 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-135
- Update po files, resolves bug 619744.

* Mon Aug 09 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-134
- Fix a localized string in firstboot. Bug 619744.

* Wed Aug 04 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-133
- Add EFI info to boot_params (bz 593109)

* Fri Jul 30 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-132
- Fix firstboot locale bug. Resolves bug 619061.

* Thu Jul 29 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-131
- fix firstboot to ensure kdump svc is disabled properly (bz 594830)

* Tue Jul 27 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-130
- Show error diablog when firstboot is not configurable. Resolves bug 612745.

* Tue Jul 27 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-129
- Fix a typo in code. Resolves bug 616694.

* Mon Jul 26 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-128
- Fix missing spec requires (bz 617445)

* Mon Jul 26 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-127
- Don't convert LABEL or UUID. Resolves bug 617124.

* Mon Jul 26 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-126
- Fix an awk syntax error when slashes are contained. (bug 600575)

* Mon Jul 26 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-125
- Support xfs. Resolves bug 607527.

* Fri Jul 23 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-124
- Fix the incorrect count of block devices.
  See comment #5 of bug 600575.

* Fri Jul 23 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-123
- Fix missed btrfsck. Resolves bug 616694.

* Wed Jul 21 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-122
- Fixed KENREL_TEXT_SIZE value (bz 605732)

* Tue Jul 20 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-121
- enhance block device detection to handle renaming better (bz 597268)

* Tue Jul 20 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-120
- Support dumping over bridge. Resolves bug 602325.

* Mon Jul 19 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-119
- Move kernel parameter checking earlier, before generating initrd.
  Resolves bug 605624.

* Thu Jul 15 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-118
- Fix unmount of rootfs when selinux policy loaded (bz 612822)

* Thu Jul 15 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-117
- Ignore other core_collector's when dumping over ssh, from Neil Horman.
  Resolve bug 614303.

* Wed Jul 14 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-116
- Include makedumpfile binary by default, resolves bug 614379.

* Wed Jul 14 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-115
- Clarify core_collector in documents, resolves bug 611614.

* Wed Jul 14 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-114
- Use tcp when dumping over NFS, to avoid heavily dropped packets.
  see comment #6 in bug 613499.

* Wed Jul 14 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-113
- Use makedumpfile -c -d 31 as default, resolves bug 612183.

* Tue Jul 13 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-112
- Fix an NFS mount error, resolves bug 613499.
- Fix an ssh error on ppc64, resolves bug 602570.

* Mon Jul 12 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-111
- Disable kdump service inside xen-guest, resolves bug 608320.

* Mon Jul 12 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-110
- Fix the wrong local host name, resolves bug 612872.

* Fri Jul 09 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-109
- Make i686 kexec properly specify e820 map (bz 611654)

* Fri Jul 09 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-108
- Make makedumpfile respect global TMPDIR. Resolves bug 607404.

* Fri Jul 09 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-107
- Include the patch from Cai, adding missed options to --help
  of makedumpfile. Resolves bug 606704.

* Fri Jul 09 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-106
- Fix the clock issues in RHEL6. Resolves bug 605844.

* Thu Jul 08 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-105
- Fix docs to reflect bz 595956 (bz 611639)

* Wed Jul 07 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-104
- Pick a tmp directory before using it. Resolves bug 609814.

* Wed Jul 07 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-103
- msh will hang if there are no statements within while loop,
  add a no-op. Resolves bug 611667.

* Wed Jul 07 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-102
- If a symlink with the same name exists, remove it first before
  copying, so that extra_bins will be copied correctly.
  Resolves bug 611699.

* Wed Jul 07 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-101
- Copy btrfsck only when necessary. Resolves bug 611451.

* Wed Jul 07 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-100
- Display memory usage stats during kdump boot.
  Resolves bug 604808.

* Mon Jul 05 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-99
- Support btrfs, and move fs type check earlier so that
  mkdumprd will fail soon with unsupported fs type.
  Resolves bug 607515 and bug 607131.

* Mon Jul 05 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-98
- Allow using PREFIX rather than NETMASK too. Resolves bug 608582.

* Mon Jul 05 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-97
- Remove the debug statement, resolves bug 600286.

* Thu Jul 01 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-96
- Fix the patch for bug 607195. 

* Thu Jul 01 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-95
- Move modules from /lib into /lib/modules/`uname -r`, and
  regenerate modules.dep for them. Resolves bug 602033.

* Wed Jun 30 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-94
- Fix addition of reserved/acpi regions (bz 600777)

* Wed Jun 30 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-93
- Fix a regression introduced by the previous patch, see
  comment #13 in bug 600607.

* Wed Jun 30 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-92
- When there are multiple net dump targets, let the last one
  overwrite the previous ones, stop showing errors in this case.
  See comment #4 in bug 600607.

* Mon Jun 28 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-91
- Add warning to kdump if we exceeded resere use (bz 607195)

* Mon Jun 28 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-90
- Only include firmwares that will be used, to reduce kdump
  initrd size. Resolves bug 604151.

* Fri Jun 25 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-89
- Removed remaining nash refs (bz 604787)

* Wed Jun 23 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-88
- load selinux policy in initramfs (bz 597229)

* Wed Jun 23 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-87
- We don't need to escape '#' with "\#", otherwise '#' will be
  executed as a command before aliased. See comment #4 of bug 600896.

* Wed Jun 23 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-86
- When there are double quotes in LABEL= in kdump.conf, findfs
  will not be able to find the correct label, we should allow
  quotes in LABEL= in kdump.conf because a label name may contain
  spaces. See comment #4 of bug 600611.

* Tue Jun 22 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-85
- disable memory cgroups in kdump (bz 605717)

* Mon Jun 21 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-84
- Fix the wrong patch for bug 600597.

* Mon Jun 21 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-83
- Add the missed patch for bug 600572.

* Sat Jun 19 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-82
- prevent fsck from oeprating interactively (bz 595057)

* Fri Jun 18 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-81
- Add 4G limit to firstboot_kdump.py, resolves bug 523092.

* Fri Jun 18 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-80
- Fix the other issue in bug 603522.

* Wed Jun 16 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-79
- Fix bug 603006 and bug 603522.

* Tue Jun 15 2010 Amerigo Wang <amwang@redhat.com> - 2.0.0-78
- Forward patches from RHEL5, Resolves: bz 592312  600566
  600571  600572 600574 600575 600577 600578 600579 600581 600583
  600584  600585 600586 600588 600590 600591 600593 600594 600595
  600596 600597  600598 600599 600600 600601 600602 600604 600605
  600606 600607 600610 600611 600613 600896 602785  602905.

* Wed Jun 09 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-77
- dchapmans patch to use current rootfs as default in kdump.conf (bz595956)

* Tue Jun 08 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-76
- Fix blacklisting (bz 596439)

* Thu Jun 03 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-75
- Fix ppc64 to work & not corrupt vmcore (bz 578067 575685)

* Wed Jun 02 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-74
- Enhance initrd rebuild detection (bz 592312)

* Thu May 27 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-73
- fixed raid5 module detection (bz 595809)

* Wed May 26 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-72
- Fixed kdump option handling (bz 594508)
- Fixed kdump fsck pause (bz 595057)

* Mon May 24 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-71
- Fixed mkdumprd to remove dup insmod (bz 591172)

* Thu May 20 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-70
- Fix firstboot to find grub on EFI systems (bz 592140)
- Fix scp monitoring script (bz 593403)

* Thu May 06 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-69
- Updated translations (bz 589214)

* Mon Apr 26 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-68
- Remove bogus debug comment from mkdumprd. (bz 585811)

* Tue Apr  6 2010 Vitaly Mayatskikh <vmayatsk@redhat.com> - 2.0.0-67
- Handle SPARSEMEM properly (bz 574370)

* Mon Apr 05 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-66
- Add blacklist feature to kdump.conf (bz 568018)

* Mon Apr 05 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-65
- Fix ssh id propogation w/ selinux (bz 579477)

* Mon Apr 05 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-64
- Fix major/minor numbers on /dev/rtc (bz 578411)

* Thu Apr 01 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-63
- Vitaly's fix to detect need for 64 bit elf (bz 578178)

* Tue Mar 30 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-62
- Update mkdumprd to deal with changes in busybox fsck (bz 577981)

* Wed Mar 24 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-61
- Add ability to handle firmware hotplug events (bz 563145)

* Mon Mar 22 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-60
- Add help info for -b option (bz 574305)

* Thu Mar 18 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-59
- Fix critical_disks list to exclude cciss/md (bz 573624)

* Thu Mar 11 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-58
- Fix spec file typo (bz 567871)

* Thu Mar 11 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-57
- Enable execshield in ppc build (bz 567871)

* Wed Mar 03 2010 Neil Horman <nhorman@redhat.com> -2.0.0-56
- Added utsname support to makedumpfile for 2.6.32 (bz 556356)
- Cleaned up some syntax in the changelog

* Mon Mar 01 2010 Neil Horman <nhorman@redhat.com> -2.0.0-55
- Fixed lvm setup loop to not hang (bz 561793)

* Tue Feb 09 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-54
- Fixed firstboot enable sense (bz 563062)

* Mon Feb 08 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-53
- Removed rhpl code from firstboot (bz 561717)

* Fri Jan 29 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-52
- Updated kexec with mr translations (bz 559099)

* Fri Jan 29 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-51
- Fixed x86_64 page_offset specifictaion (bz 546549)

* Mon Jan 25 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-50
- Fixed readlink issue (bz 558193)

* Wed Jan 20 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-49
- Removed remaining nash calls from mkdumprd (bz 556877)

* Fri Jan 08 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-48
- Added poweroff option to mkdumprd (bz 543360)

* Fri Jan 08 2010 Neil Horman <nhorman@redhat.com> - 2.0.0-47
- Fixed bad call to resolve_dm_name (bz 529393)

* Tue Dec 08 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-46
- Update makedumpfile to 1.3.5 (bz 532064)

* Fri Dec 04 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-45
- Fix initscript to return proper LSB return codes (bz 544161)

* Fri Nov 20 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-44
- Exclude s390[x] from build (bz 538852)

* Tue Nov 17 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-43
- Fixing crashkernel syntax parsing (bz 533800)

* Wed Nov 11 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-42
- Cai's fix for broken regex (bz 536719)

* Fri Nov 06 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-41
- Improved mkdumprd run time (bz 528737)

* Wed Nov 04 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-40
- Adding -i/-x options to makedumpfile (bz 529411)

* Wed Nov 04 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-39
- Fix ppc64 sysconfig file (bz 531565)

* Wed Nov 04 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-38
- Update makedumpfile to v 1.3.4 (bz 529409)

* Mon Nov 02 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-37
- Adding relocatable patches from bz 484465)

* Thu Oct 29 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-36
- Pulling fedora fixes for dracut/kdump into RHEL6 (bz 531473)

* Mon Oct 12 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-35
- Fixed kexec-kdump-howto.doc for RHEL6 (bz 525043)

* Mon Oct 12 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-34
- Fix firstboot to deal with new crashkernel sytaxes (bz 525026)

* Wed Oct 07 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-33
- Fix x8664 memory map changes for makedumpfile (bz 526749)
 
* Wed Sep 30 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-32
- Fix infinite loop from modprobe changes (bz 524875)

* Thu Sep 24 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-31
- Removed universal add of ata_piix from mkdumprd (bz 524817)

* Wed Sep 23 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-30
- Fix reboot in firstboot (bz 524811)

* Tue Sep 22 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-29
- Fix mkdumprd typo (bz 524820)

* Fri Sep 18 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-28
- Fix typo (bz 517584)

* Fri Sep 18 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-27
- Update mkdumprd to pull in all modules needed (bz 517584)

* Mon Aug 31 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-26
- Update docs to reflect use of ext4 ( bz 520183)

* Mon Aug 24 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-25
- Update kexec-kdump-howto.txt (bz 518604 & 518296)

* Thu Aug 13 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-24
- update kdump adv conf init script & dracut module

* Wed Jul 29 2009 Neil Horman <nhorman@redhat.com> - 2.0,0-23
- Remove mkdumprd2 and start replacement with dracut

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Neil Horman <nhorman@redhat.com> 2.0.0-21
- Fixed build break

* Mon Jul 06 2009 Neil Horman <nhorman@redhat.com> 2.0.0-20
- Make makedumpfile a dynamic binary

* Mon Jul 06 2009 Neil Horman <nhorman@redhat.com> 2.0.0-19
- Fix build issue 

* Mon Jul 06 2009 Neil Horman <nhorman@redhat.com> 2.0.0-18
- Updated initscript to use mkdumprd2 if manifest is present
- Updated spec to require dash
- Updated sample manifest to point to correct initscript
- Updated populate_std_files helper to fix sh symlink

* Mon Jul 06 2009 Neil Horman <nhorman@redhat.com> 2.0.0-17
- Fixed mkdumprd2 tarball creation

* Tue Jun 23 2009 Neil Horman <nhorman@redhat.com> 2.0.0-16
- Fix up kdump so it works with latest firstboot

* Mon Jun 15 2009 Neil Horman <nhorman@redhat.com> 2.0.0-15
- Fixed some stat drive detect bugs by E. Biederman (bz505701)

* Wed May 20 2009 Neil Horman <nhorman@redhat.com> 2.0.0-14
- Put early copy of mkdumprd2 out in the wild (bz 466392)

* Fri May 08 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-13
- Update makedumpfile to v 1.3.3 (bz 499849)

* Tue Apr 07 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-12
- Simplifed rootfs mounting code in mkdumprd (bz 494416)

* Sun Apr 05 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.0.0-11
- Install the correct configuration for i586

* Fri Apr 03 2009 Neil Horman <nhorman@redhat.com> - 2.0.0-10
- Fix problem with quoted CORE_COLLECTOR string (bz 493707)

* Thu Apr 02 2009 Orion Poplawski <orion@cora.nwra.com> - 2.0.0-9
- Add BR glibc-static

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.0-7
- Rebuild for Python 2.6

* Mon Dec 01 2008 Neil Horman <nhorman@redhat.com> - 2.0.0.6
- adding makedumpfile man page updates (bz 473212)

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0.0-5
- Rebuild for Python 2.6

* Wed Nov 05 2008 Neil Horman <nhorman@redhat.com> - 2.0.0-3
- Correct source file to use proper lang package (bz 335191)

* Wed Oct 29 2008 Neil Horman <nhorman@redhat.com> - 2.0.0-2
- Fix mkdumprd typo (bz 469001)

* Mon Sep 15 2008 Neil Horman <nhorman@redhat.com> - 2.0.0-2
- Fix sysconfig files to not specify --args-linux on x86 (bz 461615)

* Wed Aug 27 2008 Neil Horman <nhorman@redhat.com> - 2.0.0-1
- Update kexec-tools to latest upstream version

* Wed Aug 27 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-16
- Fix mkdumprd to properly use UUID/LABEL search (bz 455998)

* Tue Aug  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.102pre-15
- fix license tag

* Mon Jul 28 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-14
- Add video reset section to docs (bz 456572)

* Fri Jul 11 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-13
- Fix mkdumprd to support dynamic busybox (bz 443878)

* Wed Jun 11 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-12
- Added lvm to bin list (bz 443878)

* Thu Jun 05 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-11
- Update to latest makedumpfile from upstream
- Mass import of RHEL fixes missing in rawhide

* Thu Apr 24 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-10
- Fix mkdumprd to properly pull in libs for lvm/mdadm (bz 443878)

* Wed Apr 16 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-9
- Fix cmdline length issue

* Tue Mar 25 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-8
- Fixing ARCH definition for bz 438661

* Mon Mar 24 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-7
- Adding patches for bz 438661

* Fri Feb 22 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-6
- Bringing rawhide up to date with bugfixes from RHEL5
- Adding patch to prevent kexec buffer overflow on ppc (bz 428684)

* Tue Feb 19 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-5
- Modifying mkdumprd to include dynamic executibles (bz 433350)

* Tue Feb 12 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-4
- bumping rev number for rebuild

* Wed Jan 02 2008 Neil Horman <nhorman@redhat.com> - 1.102pre-3
- Fix ARCH placement in kdump init script (bz 427201)
- Fix BuildRequires
- Fix Makedumpfile to build with new libelf

* Mon Oct 01 2007 Neil Horman <nhorman@redhat.com> - 1.102pre-2
- Fix triggerpostun script (bz 308151)

* Thu Aug 30 2007 Neil Horman <nhorman@redhat.com> - 1.102pre-1
- Bumping kexec version to latest horms tree (bz 257201)
- Adding trigger to remove initrds when a kernel is removed

* Wed Aug 22 2007 Neil Horman <nhorman@redhat.com> - 1.101-81
- Add xen-syms patch to makedumpfile (bz 250341)

* Wed Aug 22 2007 Neil Horman <nhorman@redhat.com> - 1.101-80
- Fix ability to determine space on nfs shares (bz 252170)

* Tue Aug 21 2007 Neil Horman <nhorman@redhat.com> - 1.101-79
- Update kdump.init to always create sparse files (bz 253714)

* Fri Aug 10 2007 Neil Horman <nhorman@redhat.com> - 1.101-78
- Update init script to handle xen kernel cmdlnes (bz 250803)

* Wed Aug 01 2007 Neil Horman <nhorman@redhat.com> - 1.101-77
- Update mkdumprd to suppres notifications /rev makedumpfile (bz 250341)

* Thu Jul 19 2007 Neil Horman <nhorman@redhat.com> - 1.101-76
- Fix mkdumprd to suppress informative messages (bz 248797)

* Wed Jul 18 2007 Neil Horman <nhorman@redhat.com> - 1.101-75
- Updated fr.po translations (bz 248287)

* Tue Jul 17 2007 Neil Horman <nhorman@redhat.com> - 1.101-74
- Fix up add_buff to retry locate_hole on segment overlap (bz 247989)

* Mon Jul 09 2007 Neil Horman <nhorman@redhat.com> - 1.101-73
- Fix up language files for kexec (bz 246508)

* Thu Jul 05 2007 Neil Horman <nhorman@redhat.com> - 1.101-72
- Fixing up initscript for LSB (bz 246967)

* Tue Jun 19 2007 Neil Horman <nhorman@redhat.com> - 1.101-71
- Fixed conflict in mkdumprd in use of /mnt (bz 222911)

* Mon Jun 18 2007 Neil Horman <nhorman@redhat.com> - 1.101-70
- Fixed kdump.init to properly read cmdline (bz 244649)

* Wed Apr 11 2007 Neil Horman <nhorman@redhat.com> - 1.101-69
- Fixed up kdump.init to enforce mode 600 on authorized_keys2 (bz 235986)

* Tue Apr 10 2007 Neil Horman <nhorman@redhat.com> - 1.101-68
- Fix alignment of bootargs and device-tree structures on ppc64

* Tue Apr 10 2007 Neil Horman <nhorman@redhat.com> - 1.101-67
- Allow ppc to boot ppc64 kernels (bz 235608)

* Tue Apr 10 2007 Neil Horman <nhorman@redhat.com> - 1.101-66
- Reduce rmo_top to 0x7c000000 for PS3 (bz 235030)

* Mon Mar 26 2007 Neil Horman <nhorman@redhat.com> - 1.101-65
- Fix spec to own kexec_tools directory (bz 219035)

* Wed Mar 21 2007 Neil Horman <nhorman@redhat.com> - 1.101-64
- Add fix for ppc memory region computation (bz 233312)

* Thu Mar 15 2007 Neil Horman <nhorman@redhat.com> - 1.101-63
- Adding extra check to avoid oom kills on nfs mount failure (bz 215056)

* Tue Mar 06 2007 Neil Horman <nhorman@redhat.com> - 1.101-62
- Updating makedumpfile to version 1.1.1 (bz 2223743)

* Thu Feb 22 2007 Neil Horman <nhorman@redhat.com> - 1.101-61
- Adding multilanguage infrastructure to firstboot_kdump (bz 223175)

* Mon Feb 12 2007 Neil Horman <nhorman@redhat.com> - 1.101-60
- Fixing up file permissions on kdump.conf (bz 228137)

* Fri Feb 09 2007 Neil Horman <nhorman@redhat.com> - 1.101-59
- Adding mkdumprd man page to build

* Thu Jan 25 2007 Neil Horman <nhorman@redhat.com> - 1.101-58
- Updating kdump.init and mkdumprd with most recent RHEL5 fixes
- Fixing BuildReq to require elfutils-devel-static

* Thu Jan 04 2007 Neil Horman <nhorman@redhat.com> - 1.101-56
- Fix option parsing problem for bzImage files (bz 221272)

* Fri Dec 15 2006 Neil Horman <nhorman@redhat.com> - 1.101-55
- Wholesale update of RHEL5 revisions 55-147

* Tue Aug 29 2006 Neil Horman <nhorman@redhat.com> - 1.101-54
- integrate default elf format patch

* Tue Aug 29 2006 Neil Horman <nhorman@redhat.com> - 1.101-53
- Taking Viveks x86_64 crashdump patch (rcv. via email)

* Tue Aug 29 2006 Neil Horman <nhorman@redhat.com> - 1.101-52
- Taking ia64 tools patch for bz 181358

* Mon Aug 28 2006 Neil Horman <nhorman@redhat.com> - 1.101-51
- more doc updates
- added patch to fix build break from kernel headers change

* Thu Aug 24 2006 Neil Horman <nhorman@redhat.com> - 1.101-50
- repo patch to enable support for relocatable kernels.

* Thu Aug 24 2006 Neil Horman <nhorman@redhat.com> - 1.101-49
- rewriting kcp to properly do ssh and scp
- updating mkdumprd to use new kcp syntax

* Wed Aug 23 2006 Neil Horman <nhorman@redhat.com> - 1.101-48
- Bumping revision number 

* Tue Aug 22 2006 Jarod Wilson <jwilson@redhat.com> - 1.101-47
- ppc64 no-more-platform fix

* Mon Aug 21 2006 Jarod Wilson <jwilson@redhat.com> - 1.101-46
- ppc64 fixups:
  - actually build ppc64 binaries (bug 203407)
  - correct usage output
  - avoid segfault in command-line parsing
- install kexec man page
- use regulation Fedora BuildRoot

* Fri Aug 18 2006 Neil Horman <nhorman@redhat.com> - 1.101-45
- fixed typo in mkdumprd for bz 202983
- fixed typo in mkdumprd for bz 203053
- clarified docs in kdump.conf with examples per bz 203015

* Tue Aug 15 2006 Neil Horman <nhorman@redhat.com> - 1.101-44
- updated init script to implement status function/scrub err messages
 
* Wed Aug 09 2006 Jarod Wilson <jwilson@redhat.com> - 1.101-43
- Misc spec cleanups and macro-ifications

* Wed Aug 09 2006 Jarod Wilson <jwilson@redhat.com> - 1.101-42
- Add dir /var/crash, so default kdump setup works

* Thu Aug 03 2006 Neil Horman <nhorman@redhat.com> - 1.101-41
- fix another silly makefile error for makedumpfile 

* Thu Aug 03 2006 Neil Horman <nhorman@redhat.com> - 1.101-40
- exclude makedumpfile from build on non-x86[_64] arches 

* Thu Aug 03 2006 Neil Horman <nhorman@redhat.com> - 1.101-39
- exclude makedumpfile from build on non-x86[_64] arches 

* Thu Aug 03 2006 Neil Horman <nhorman@redhat.com> - 1.101-38
- updating makedumpfile makefile to use pkg-config on glib-2.0

* Thu Aug 03 2006 Neil Horman <nhorman@redhat.com> - 1.101-37
- updating makedumpfile makefile to use pkg-config

* Thu Aug 03 2006 Neil Horman <nhorman@redhat.com> - 1.101-36
- Removing unneeded deps after Makefile fixup for makedumpfile

* Thu Aug 03 2006 Neil Horman <nhorman@redhat.com> - 1.101-35
- fixing up FC6/RHEL5 BuildRequires line to build in brew

* Wed Aug 02 2006 Neil Horman <nhorman@redhat.com> - 1.101-34
- enabling makedumpfile in build

* Wed Aug 02 2006 Neil Horman <nhorman@redhat.com> - 1.101-33
- added makedumpfile source to package

* Mon Jul 31 2006 Neil Horman <nhorman@redhat.com> - 1.101-32
- added et-dyn patch to allow loading of relocatable kernels

* Thu Jul 27 2006 Neil Horman <nhorman@redhat.com> - 1.101-30
- fixing up missing patch to kdump.init

* Wed Jul 19 2006 Neil Horman <nhorman@redhat.com> - 1.101-30
- add kexec frontend (bz 197695)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.101-29
- rebuild

* Fri Jul 07 2006 Neil Horman <nhorman@redhat.com> 1.101-27
- Buildrequire zlib-devel

* Thu Jun 22 2006 Neil Horman <nhorman@redhat.com> -1.101-19
- Bumping rev number

* Thu Jun 22 2006 Neil Horman <nhorman@redhat.com> -1.101-17
- Add patch to allow ppc64 to ignore args-linux option

* Wed Mar 08 2006 Bill Nottingham <notting@redhat.com> - 1.101-16
- fix scriptlet - call chkconfig --add, change the default in the
  script itself (#183633)

* Wed Mar 08 2006 Thomas Graf <tgraf@redhat.com> - 1.101-15
- Don't add kdump service by default, let the user manually add it to
  avoid everyone seeing a warning.

* Tue Mar 07 2006 Thomas Graf <tgraf@redhat.com> - 1.101-14
- Fix kdump.init to call kexec from its new location

* Mon Mar  6 2006 Jeremy Katz <katzj@redhat.com> - 1.101-13
- proper requires for scriptlets

* Mon Mar 06 2006 Thomas Graf <tgraf@redhat.com> - 1.101-12
- Move kexec and kdump binaries to /sbin

* Thu Mar 02 2006 Thomas Graf <tgraf@redhat.com> - 1.101-11
- Fix argument order when stopping kexec

* Mon Feb 27 2006 Thomas Graf <tgraf@redhat.com> - 1.101-10
- kdump7.patch
   o Remove elf32 core headers support for x86_64
   o Fix x86 prepare elf core header routine
   o Fix ppc64 kexec -p failure for gcc 4.10
   o Fix few warnings for gcc 4.10
   o Add the missing --initrd option for ppc64
   o Fix ppc64 persistent root device bug
- Remove --elf32-core-headers from default configuration, users
  may re-add it via KEXEC_ARGS.
- Remove obsolete KEXEC_HEADERS
* Wed Feb 22 2006 Thomas Graf <tgraf@redhat.com> - 1.101-9
- Remove wrong quotes around --command-line in kdump.init

* Fri Feb 17 2006 Jeff Moyer <jmoyer@redhat.com> - 1.101-8
- Fix the service stop case.  It was previously unloading the wrong kernel.
- Implement the "restart" function.
- Add the "irqpoll" option as a default kdump kernel commandline parameter.
- Create a default kernel command line in the sysconfig file upon rpm install.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.101-7.1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Feb 02 2006 Thomas Graf <tgraf@redhat.com> - 1.101-7.1
- Add patch to enable the kdump binary for x86_64
* Wed Feb 01 2006 Thomas Graf <tgraf@redhat.com>
- New kdump patch to support s390 arch + various fixes
- Include kdump in x86_64 builds
* Mon Jan 30 2006 Thomas Graf <tgraf@redhat.com>
- New kdump patch to support x86_64 userspace

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Wed Nov 16 2005 Thomas Graf <tgraf@redhat.com> - 1.101-5
- Report missing kdump kernel image as warning
 
* Thu Nov  3 2005 Jeff Moyer <jmoyer@redhat.com> - 1.101-4
- Build for x86_64 as well.  Kdump support doesn't work there, but users
  should be able to use kexec.

* Fri Sep 23 2005 Jeff Moyer <jmoyer@redhat.com> - 1.101-3
- Add a kdump sysconfig file and init script
- Spec file additions for pre/post install/uninstall

* Thu Aug 25 2005 Jeff Moyer <jmoyer@redhat.com>
- Initial prototype for RH/FC5
