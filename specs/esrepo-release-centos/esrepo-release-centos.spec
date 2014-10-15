%define _top_url_str       %{?_top_url}%{!?_top_url:http://localhost.localdomain/ftp/pub/linux/esrepo}
%define _site_dist_str     %{?_site_dist}%{!?_site_dist:localhost}
%define _site_dist_str_2   .%{_site_dist_str}

Name:           esrepo-release-centos
Version:        3.0
Release:        1%{?dist}%{_site_dist_str_2}
Summary:        esrepo repository configuration (site `%{_site_dist_str}')

Group:          System Environment/Base
License:        GPLv2

URL:            %{_top_url_str}
Source0:        esrepo-repo-write.sh
Source1:        COPYING

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release

%description
This package contains the esrepo repository (site `%{_site_dist_str}')
configuration for yum and up2date.

%prep
%setup -q  -c -T
install -pm 755 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build
TOP_URL="%{_top_url_str}" DIST_STR="%{_site_dist_str}" ./esrepo-repo-write.sh >esrepo.repo

%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 esrepo.repo  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun


%files
%defattr(-,root,root,-)
%doc COPYING
%config(noreplace) /etc/yum.repos.d/esrepo.repo


%changelog
* Tue Oct 14 2014 Evgueni Souleimanov <esoule@100500.ca> - 3.0-1
- Add support for site-specific repository file generation

* Sat Jun 28 2014 Evgueni Souleimanov <esoule@100500.ca> - 2.0-1
- Initial Package

