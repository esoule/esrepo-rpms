## Installation prefix of the toolchain
%global _newprefix              /usr/low10

## Installation prefix of the symbolic links
%define _prefix                 /opt/ccache/usr/low10
%define _bindir                 %{_prefix}/bin

%define gcc_target              m68k-elf

Name:           m68k-elf-tools-ccache-gcc-20031003
Version:        1.0
Release:        101%{?dist}
Summary:        ccache symbolic link for gcc for %{gcc_target}

Group:          Development/Tools
License:        Public Domain
URL:            https://github.com/esoule

BuildArch:      noarch

Requires:       ccache
Requires:       /usr/bin/ccache

%description
Provides symbolic links to %{gcc_target}-gcc,
%{gcc_target}-c++, %{gcc_target}-g++ in
%{_bindir}.

%prep
true


%build
true

%install
export TZ=UTC

rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
ln -v -s ../../../../../usr/bin/ccache %{buildroot}%{_bindir}/%{gcc_target}-c++
ln -v -s ../../../../../usr/bin/ccache %{buildroot}%{_bindir}/%{gcc_target}-g++
ln -v -s ../../../../../usr/bin/ccache %{buildroot}%{_bindir}/%{gcc_target}-gcc

## roll back dates of files
find -H %{buildroot}    \
        -print0    \
        | xargs -0 --no-run-if-empty touch --no-create    \
        --no-dereference --date="2004-10-03 00:00:00 +0000"


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_prefix}
%dir %{_bindir}
%{_bindir}/%{gcc_target}-c++
%{_bindir}/%{gcc_target}-g++
%{_bindir}/%{gcc_target}-gcc

%changelog
* Thu Nov 24 2016 Evgueni Souleimanov <esoule@100500.ca> - 1.101
- Initial package
