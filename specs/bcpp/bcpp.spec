Name:           bcpp
Version:        20150811
Release:        1.101%{?dist}
Summary:        Indent C/C++ source programs

Group:          Applications/Text
License:        MIT
URL:            http://invisible-island.net/bcpp/
Source0:        ftp://invisible-island.net/bcpp/bcpp-%{version}.tgz
Source1:        ftp://invisible-island.net/bcpp/bcpp-%{version}.tgz.asc

BuildRequires:  redhat-rpm-config

%description
bcpp indents C/C++ source programs, replacing tabs with spaces or the
reverse. Unlike indent, it does (by design) not attempt to wrap long
statements.

This version improves the parsing algorithm by marking the state of all
characters, recognizes a wider range of indention structures, and implements
a simple algorithm for indenting embedded SQL.

%prep
%setup -q


%build
CFLAGS='%{optflags} -DBCPP_CONFIG_DIR="\"%{_sysconfdir}/bcpp/\""' ;
export CFLAGS ;
CXXFLAGS='%{optflags} -DBCPP_CONFIG_DIR="\"%{_sysconfdir}/bcpp/\""' ;
export CXXFLAGS ;

%configure

make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_sysconfdir}/bcpp
install code/bcpp.cfg %{buildroot}%{_sysconfdir}/bcpp/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc CHANGES COPYING MANIFEST README VERSION
%{_bindir}/bcpp
%{_bindir}/cb++
%{_sysconfdir}/bcpp/bcpp.cfg
%{_mandir}/man1/bcpp.*


%changelog
* Sun May 08 2016 Evgueni Souleimanov <esoule@100500.ca> - 20150811-1.101
- Initial package
