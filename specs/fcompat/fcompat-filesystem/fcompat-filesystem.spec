%global _prefix			/usr/fcompat
%global orig_prefix		/usr
%if %{_lib} == lib64
%global mib			mib64
%else
%global mib			mib
%endif

Name:           fcompat-filesystem
Version:        1.0
Release:        101%{?dist}
Summary:        fcompat directory layout

Group:          System Environment/Base
License:        Public Domain
URL:            https://fedorahosted.org/filesystem

BuildRequires:  filesystem, iso-codes
Requires:       filesystem


%description
This package contains the layout of directories that are added to a
basic directory tree for a Linux operating system.


%prep


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
mkdir %{buildroot}%{_prefix}/bin

%if %{_lib} == lib64
mkdir %{buildroot}%{_prefix}/lib
ln -v -s usr/fcompat/lib %{buildroot}/mib
ln -v -s fcompat/lib %{buildroot}%{orig_prefix}/mib
%endif

mkdir %{buildroot}%{_prefix}/%{_lib}
ln -v -s usr/fcompat/%{_lib} %{buildroot}/%{mib}
ln -v -s fcompat/%{_lib} %{buildroot}%{orig_prefix}/%{mib}


%clean
rm -rf %{buildroot}


%posttrans
# symbolic links do not match SELinux policy
# TODO provide SELinux policy for "mib" and "mib64"
%if %{_lib} == lib64
/usr/bin/chcon --no-dereference --reference=/usr/lib /mib %{orig_prefix}/mib
%endif

/usr/bin/chcon --no-dereference --reference=/usr/lib /%{mib} %{orig_prefix}/%{mib}


%files
%defattr(0755,root,root,-)
%dir %attr(555,root,root) %{_prefix}
%dir %attr(555,root,root) %{_prefix}/bin
%if %{_lib} == lib64
%dir %attr(555,root,root) %{_prefix}/lib
/mib
%{orig_prefix}/mib
%endif
%dir %attr(555,root,root) %{_prefix}/%{_lib}
/%{mib}
%{orig_prefix}/%{mib}

%changelog
* Wed May 11 2016 Evgueni Souleimanov <esoule@100500.ca> - 1.0-101
- Initial package
