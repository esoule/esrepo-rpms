%define _top_url_str       %{?_top_url}%{!?_top_url:http://centos.mirror.local/ftp/pub/linux/esrepo}
%define _site_dist_str     %{?_site_dist}%{!?_site_dist:local}

Name:           esrepo-release-%{_site_dist_str}
Version:        4.0
Release:        1%{?dist}
Summary:        esrepo repository configuration (site `%{_site_dist_str}')

Group:          System Environment/Base
License:        GPLv2
URL:            %{_top_url_str}/
Source0:        esrepo-repo-write.sh
Source1:        COPYING

BuildArch:      noarch

Requires:       redhat-release

Provides:       esrepo-release

Obsoletes:      esrepo-release-centos <= 3.0

%description
This package contains the esrepo repository (site `%{_site_dist_str}')
configuration for yum and up2date.


%prep
%setup -q -c -T
install -pm 755 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build
TOP_URL="%{_top_url_str}" DIST_STR="%{_site_dist_str}" ./esrepo-repo-write.sh >esrepo.repo

%install
rm -rf %{buildroot}

# yum
install -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 esrepo.repo  \
    %{buildroot}%{_sysconfdir}/yum.repos.d


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
%config(noreplace) /etc/yum.repos.d/esrepo.repo


%changelog
* Sat Jul 07 2016 Evgueni Souleimanov <esoule@100500.ca> - 4.0-1
- Use centos.mirror.local mirror
- Clean up spec file

* Tue Oct 14 2014 Evgueni Souleimanov <esoule@100500.ca> - 3.0-1
- Add support for site-specific repository file generation

* Sat Jun 28 2014 Evgueni Souleimanov <esoule@100500.ca> - 2.0-1
- Initial Package
