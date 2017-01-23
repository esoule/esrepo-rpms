Name:           strip-nondeterminism
Version:        0.029
Release:        1.104%{?dist}
Summary:        Tool for stripping non-deterministic information from files

Group:          Development/Libraries
License:        GPLv3+
URL:            https://anonscm.debian.org/git/reproducible/strip-nondeterminism.git
Source0:        http://http.debian.net/debian/pool/main/s/strip-nondeterminism/strip-nondeterminism_%{version}.orig.tar.gz
Source1:        dummy.bflt.in
Source2:        dummy.bflt.out
Source3:        Linux-1001.uImage.in
Source4:        Linux-1001.uImage.out

Patch1:         strip-nondeterminism-0001-stop-using-subtests.patch
Patch2:         strip-nondeterminism-0002-Add-bFLT-format-support.patch
Patch4:         strip-nondeterminism-0004-Add-uImage-handler.patch
BuildArch:      noarch

BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
StripNondeterminism is a library for stripping non-deterministic
information, such as timestamps and file system order, from files. It is
used as part of the Reproducible Builds project.

This can be used as a post-processing step to improve the
reproducibility of a build product, when the build process itself cannot
be made deterministic.

strip-nondeterminism contains the File::StripNondeterminism Perl module,
and the strip-nondeterminism command line utility.

%prep
%setup -q -c -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch4 -p1
mkdir t/fixtures/bflt
cp %{SOURCE1} %{SOURCE2} t/fixtures/bflt/
mkdir t/fixtures/uimage
cp %{SOURCE3} %{SOURCE4} t/fixtures/bflt/

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

# remove debhelper add-on
rm -f %{buildroot}%{_bindir}/dh_strip_nondeterminism
rm -f %{buildroot}%{_mandir}/man1/dh_strip_nondeterminism*.1*

%check
make test


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README TODO COPYING
%{_bindir}/strip-nondeterminism

# For noarch packages: vendorlib
%{perl_vendorlib}/*

%{_mandir}/man1/*.1*


%changelog
* Sun Jan 22 2017 Evgueni Souleimanov <esoule@100500.ca> - 0.029-1.104
- Update to 0.029
- Make bFLT executable detection more reliable

* Wed Dec 28 2016 Evgueni Souleimanov <esoule@100500.ca> - 0.028-1.103
- Add support for legacy U-Boot image (uImage) files

* Sun Nov 13 2016 Evgueni Souleimanov <esoule@100500.ca> - 0.028-1.102
- Add support for bFLT Binary Flat executables

* Wed Nov 9 2016 Evgueni Souleimanov <esoule@100500.ca> - 0.028-1.101
- Initial package
- Make tests work on perl(Test::More) 0.92
