## Installation prefix of the toolchain
%global         _newprefix              /usr/low10

## Do not generate debuginfo packages
%define         debug_package           %{nil}

## Do not strip any binaries
%define         __strip                 /bin/true

Name:           m68k-elf-tools-20031003
Version:        20031003
Release:        1.102%{?dist}
Summary:        Collection of tools for use with uClinux/m68k

Group:          Development/Tools
License:        GPLv2
URL:            http://www.uclinux.org/pub/uClinux/m68k-elf-tools/
Source0:        http://www.uclinux.org/pub/uClinux/m68k-elf-tools/m68k-elf-tools-%{version}.sh
Source1:        md5sums-%{version}.txt
Source2:        fix-embedded-paths.c

%define         buildsubdir             %{name}

## Note: __find_provides and __find_requires are used
## iff _use_internal_dependency_generator is zero.
%define         _use_internal_dependency_generator              0

# Binaries inside are 32-bit
ExclusiveArch:  %ix86

%description
This is a collection of tools for use with uClinux/m68k.

The current stable version of the tools, the 20030314 cut, is primarily
based on gcc-2.95.3, binutils-2.10 and Paul Dale's latest gcc/binutils
patches. It now includes ARM patches from Philip Blundell and Michiel
Thuys and other patches from myself. An experimental version of the m68k
tools, m68k-elf-tools-20031003.sh, is also available for building 2.6
kernels.

This release uses STLport for C++ support, uClibc-0.9.19 with pthreads
and full XIP/non-XIP applications on m68k and ARM. It still provides
flat format shared libraries for the m68k tool chain, the arm folks will
have to wait a while longer yet. The latest ARMulator and a working
m68k-bdm-elf-gdb are included.

This is an experimental version of the m68k tools,
m68k-elf-tools-20031003.sh, for building 2.6 kernels.

%prep
%setup -q -T -c -n %{buildsubdir}

( cd %{_sourcedir} && md5sum -c %{SOURCE1} ; )

SKIP=$(awk '/^__ARCHIVE_FOLLOWS__/ { print NR + 1; exit 0; }' %{SOURCE0})

tail -n +${SKIP} %{SOURCE0} >%{name}.tar.gz
tar -xf %{name}.tar.gz
rm -f %{name}.tar.gz

# remove m68k-elf-gdb, because it requires libncurses.so.4 which we do
# not have on EL6
rm -f ./usr/local/bin/m68k-elf-gdb
rm -f ./usr/local/bin/m68k-bdm-elf-gdb

mv ./usr/local ./%{_newprefix}

cp %{SOURCE2} ./fix-embedded-paths.c

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;

gcc ${CFLAGS} -o fix-embedded-paths fix-embedded-paths.c

./fix-embedded-paths /usr/local %{_newprefix} %{_builddir}/%{buildsubdir}%{_newprefix}

## convert absolute symbolic links to relative ones
for link in $( find -L ./%{_newprefix} -type l ) ; do
	target="$( readlink "${link}" )"
	bn="$( basename "${target}" )"
	rm -f "${link}"
	ln -s "${bn}" "${link}"
done

(
cd %{_builddir}/%{buildsubdir}%{_newprefix}
find -L . -type f | sort | xargs --no-run-if-empty md5sum -b
true
) >md5sums.txt

mv md5sums.txt %{_builddir}/%{buildsubdir}%{_newprefix}/%{name}-%{version}-%{release}-md5sums.txt

## roll back dates of new files
touch --date='2004-10-03 00:00:00 +0000' mark-newest-file.txt

find -H %{_builddir}/%{buildsubdir}%{_newprefix}    \
        -newer mark-newest-file.txt -print0    \
        | xargs -0 --no-run-if-empty touch --no-create    \
        --no-dereference --date="2004-10-03 00:00:00 +0000"

rm -f mark-newest-file.txt

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
mv --no-target-directory %{_builddir}/%{buildsubdir}%{_newprefix} %{buildroot}%{_newprefix}

## skip over non-native binaries when computing provides
cat <<EOF >%{_builddir}/%{buildsubdir}/find-provides-my
#!/bin/sh
grep -E -v '^%{buildroot}%{_newprefix}/lib/gcc-lib/m68k-elf/'    \
        | grep -E -v '^%{buildroot}%{_newprefix}/m68k-elf/lib/'    \
        | %__find_provides
EOF

## skip over non-native binaries when computing requires
cat <<EOF >%{_builddir}/%{buildsubdir}/find-requires-my
#!/bin/sh
grep -E -v '^%{buildroot}%{_newprefix}/lib/gcc-lib/m68k-elf/'    \
        | grep -E -v '^%{buildroot}%{_newprefix}/m68k-elf/lib/'    \
        | %__find_requires
EOF

chmod +x %{_builddir}/%{buildsubdir}/find-provides-my
chmod +x %{_builddir}/%{buildsubdir}/find-requires-my

## Note: Used iff _use_internal_dependency_generator is zero.
%define __find_provides %{_builddir}/%{buildsubdir}/find-provides-my
%define __find_requires %{_builddir}/%{buildsubdir}/find-requires-my


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_newprefix}
%{_newprefix}/*


%changelog
* Fri Nov 10 2016 Evgueni Souleimanov <esoule@100500.ca> - 20031003-1.102
- Actually use generated find-provides and find-requires scripts
- Check checksum of origin .sh file
- Put checksum of all files into the package
- Roll back dates of files modified with fix-embedded-paths

* Thu Nov 10 2016 Evgueni Souleimanov <esoule@100500.ca> - 20031003-1.101
- Initial package
