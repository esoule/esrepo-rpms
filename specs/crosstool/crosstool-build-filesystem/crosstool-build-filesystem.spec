
%global top_dir /opt

Name:           crosstool-build-filesystem
Version:        1.0.1
Release:        1%{?dist}
Summary:        Directories for building crosstool without fix-embedded-paths utility
License:        GPLv2
Group:          Development/Tools
BuildArch:      noarch

Source0:        %{name}.mark.txt

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package creates directories for building crosstool, without
fix-embedded-paths utility.

This package may only be installed for building the
toolchain and must be removed before installing the toolchain

%prep


%build


%install
rm -rf %{buildroot}
install -d -v -m 0755 %{buildroot}%{top_dir}/%{name}
install -p -v -m 0644 %{SOURCE0} %{buildroot}%{top_dir}/%{name}/%{name}.mark.txt

%clean
rm -rf %{buildroot}

%post

top_dir=%{top_dir}

mkdir -v -p ${top_dir}/crosstool
chmod -c 0777 ${top_dir}/crosstool || :

%preun

top_dir=%{top_dir}

if [ $1 -eq 0 ] ; then
  chmod -c 0755 ${top_dir}/crosstool || :
  rmdir ${top_dir}/crosstool || :
fi

%files
%defattr(-,root,root)
%dir %{top_dir}/%{name}
%{top_dir}/%{name}/%{name}.mark.txt

%changelog
* Sun Sep 28 2014 Evgueni Souleimanov <esoule@100500.ca> - 1.0.1-1
- initial package
