%define _prefix                 /opt/ccache/opt/rtems-4.6
%define _bindir                 %{_prefix}/bin

%define rpmprefix               rtems-4.6-

%define gcc_target              powerpc-rtems

Name:           %{rpmprefix}%{gcc_target}-ccache-gcc
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
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
ln -v -s ../../../../../usr/bin/ccache %{buildroot}%{_bindir}/%{gcc_target}-c++
ln -v -s ../../../../../usr/bin/ccache %{buildroot}%{_bindir}/%{gcc_target}-g++
ln -v -s ../../../../../usr/bin/ccache %{buildroot}%{_bindir}/%{gcc_target}-gcc


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
* Tue Jul 05 2016 Evgueni Souleimanov <esoule@100500.ca> - 1.101
- Initial package
