# Patented bytecode interpreter and patented subpixel rendering disabled by default.
# Pass '--with bytecode_interpreter' and '--with subpixel_rendering' on rpmbuild
# command-line to enable them.
%{!?_with_bytecode_interpreter: %{!?_without_bytecode_interpreter: %define _without_bytecode_interpreter --without-bytecode_interpreter}}
%{!?_with_subpixel_rendering: %{!?_without_subpixel_rendering: %define _without_subpixel_rendering --without-subpixel_rendering}}

%{!?with_xfree86:%define with_xfree86 1}

Summary: A free and portable font rendering engine
Name: freetype
Version: 2.3.11
Release: 17%{?dist_01}.1.101%{?dist}
License: FTL or GPLv2+
Group: System Environment/Libraries
URL: http://www.freetype.org
Source:  http://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.bz2
Source1: http://download.savannah.gnu.org/releases/freetype/freetype-doc-%{version}.tar.bz2
Source2: http://download.savannah.gnu.org/releases/freetype/ft2demos-%{version}.tar.bz2

# Add -lm when linking X demos
Patch5: ft2demos-2.1.9-mathlib.patch
Patch20:  freetype-2.1.10-enable-ft2-bci.patch
Patch21:  freetype-2.3.0-enable-spr.patch

# Enable otvalid and gxvalid modules
Patch46:  freetype-2.2.1-enable-valid.patch
# Enable additional demos
Patch47:  freetype-2.3.11-more-demos.patch

# Fix multilib conflicts
Patch88:  freetype-multilib.patch

Patch89:  freetype-2.3.11-CVE-2010-2498.patch
Patch90:  freetype-2.3.11-CVE-2010-2499.patch
Patch91:  freetype-2.3.11-CVE-2010-2500.patch
Patch92:  freetype-2.3.11-CVE-2010-2519.patch
Patch93:  freetype-2.3.11-CVE-2010-2520.patch
Patch94:  freetype-2.3.11-CVE-2010-2527.patch
Patch95:  freetype-2.3.11-axis-name-overflow.patch
Patch96:  freetype-2.3.11-CVE-2010-1797.patch
Patch97:  freetype-2.3.11-CVE-2010-2805.patch
Patch98:  freetype-2.3.11-CVE-2010-2806.patch
Patch99:  freetype-2.3.11-CVE-2010-2808.patch
Patch100:  freetype-2.3.11-CVE-2010-3311.patch
Patch101:  freetype-2.3.11-CVE-2010-3855.patch
Patch102:  freetype-2.3.11-CVE-2011-0226.patch
Patch103:  freetype-2.3.11-CVE-2011-3256.patch
Patch104:  freetype-2.3.11-CVE-2011-3439.patch
Patch105:  freetype-2.3.11-CVE-2012-1126.patch
Patch106:  freetype-2.3.11-CVE-2012-1127.patch
Patch107:  freetype-2.3.11-CVE-2012-1130.patch
Patch108:  freetype-2.3.11-CVE-2012-1131.patch
Patch109:  freetype-2.3.11-CVE-2012-1132.patch
Patch110:  freetype-2.3.11-CVE-2012-1134.patch
Patch111:  freetype-2.3.11-CVE-2012-1136.patch
Patch112:  freetype-2.3.11-CVE-2012-1137.patch
Patch113:  freetype-2.3.11-CVE-2012-1139.patch
Patch114:  freetype-2.3.11-CVE-2012-1140.patch
Patch115:  freetype-2.3.11-CVE-2012-1141.patch
Patch116:  freetype-2.3.11-CVE-2012-1142.patch
Patch117:  freetype-2.3.11-CVE-2012-1143.patch
Patch118:  freetype-2.3.11-CVE-2012-1144.patch
Patch119:  freetype-2.3.11-bdf-overflow.patch
Patch120:  freetype-2.3.11-array-initialization.patch
Patch121:  freetype-2.3.11-CVE-2012-5669.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1197738
Patch122:  freetype-2.3.11-CVE-2014-9657.patch
Patch123:  freetype-2.3.11-CVE-2014-9658.patch
Patch124:  freetype-2.3.11-ft-strncmp.patch
Patch125:  freetype-2.3.11-CVE-2014-9675.patch
Patch126:  freetype-2.3.11-CVE-2014-9660.patch
Patch127:  freetype-2.3.11-CVE-2014-9661a.patch
Patch128:  freetype-2.3.11-CVE-2014-9661b.patch
Patch129:  freetype-2.3.11-CVE-2014-9663.patch
Patch130:  freetype-2.3.11-CVE-2014-9664a.patch
Patch131:  freetype-2.3.11-CVE-2014-9664b.patch
Patch132:  freetype-2.3.11-CVE-2014-9667.patch
Patch133:  freetype-2.3.11-CVE-2014-9669.patch
Patch134:  freetype-2.3.11-CVE-2014-9670.patch
Patch135:  freetype-2.3.11-CVE-2014-9671.patch
Patch136:  freetype-2.3.11-CVE-2014-9673.patch
Patch137:  freetype-2.3.11-CVE-2014-9674a.patch
Patch138:  freetype-2.3.11-unsigned-long.patch
Patch139:  freetype-2.3.11-CVE-2014-9674b.patch
Patch140:  freetype-2.3.11-pcf-read-a.patch
Patch141:  freetype-2.3.11-pcf-read-b.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1154625
Patch142:  freetype-2.3.11-fix-buffer-size.patch

Buildroot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)

BuildRequires: libX11-devel

%if %{?_with_bytecode_interpreter:1}%{!?_with_bytecode_interpreter:0}
Provides: %{name}-bytecode
%endif
%if %{?_with_subpixel_rendering:1}%{!?_with_subpixel_rendering:0}
Provides: %{name}-subpixel
%endif

%description
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments. FreeType is a library which can open and
manages font files as well as efficiently load, hint and render
individual glyphs. FreeType is not a font server or a complete
text-rendering library.


%package demos
Summary: A collection of FreeType demos
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description demos
The FreeType engine is a free and portable font rendering
engine, developed to provide advanced font support for a variety of
platforms and environments.  The demos package includes a set of useful
small utilities showing various capabilities of the FreeType library.


%package devel
Summary: FreeType development libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel
Requires: pkgconfig

%description devel
The freetype-devel package includes the static libraries and header files
for the FreeType font rendering engine.

Install freetype-devel if you want to develop programs which will use
FreeType.


%prep
%setup -q -b 1 -a 2

pushd ft2demos-%{version}
%patch5 -p1 -b .mathlib
popd

%if %{?_with_bytecode_interpreter:1}%{!?_with_bytecode_interpreter:0}
%patch20  -p1 -b .enable-ft2-bci
%endif

%if %{?_with_subpixel_rendering:1}%{!?_with_subpixel_rendering:0}
%patch21  -p1 -b .enable-spr
%endif

%patch46  -p1 -b .enable-valid
%patch47  -p1 -b .more-demos

%patch88 -p1 -b .multilib

%patch89 -p1 -b .CVE-2010-2498
%patch90 -p1 -b .CVE-2010-2499
%patch91 -p1 -b .CVE-2010-2500
%patch92 -p1 -b .CVE-2010-2519
%patch93 -p1 -b .CVE-2010-2520
%patch94 -p1 -b .CVE-2010-2527
%patch95 -p1 -b .axis-name-overflow
%patch96 -p1 -b .CVE-2010-1797
%patch97 -p1 -b .CVE-2010-2805
%patch98 -p1 -b .CVE-2010-2806
%patch99 -p1 -b .CVE-2010-2808
%patch100 -p1 -b .CVE-2010-3311
%patch101 -p1 -b .CVE-2010-3855
%patch102 -p1 -b .CVE-2011-0226
%patch103 -p1 -b .CVE-2011-3256
%patch104 -p1 -b .CVE-2011-3439
%patch105 -p1 -b .CVE-2012-1126
%patch106 -p1 -b .CVE-2012-1127
%patch107 -p1 -b .CVE-2012-1130
%patch108 -p1 -b .CVE-2012-1131
%patch109 -p1 -b .CVE-2012-1132
%patch110 -p1 -b .CVE-2012-1134
%patch111 -p1 -b .CVE-2012-1136
%patch112 -p1 -b .CVE-2012-1137
%patch113 -p1 -b .CVE-2012-1139
%patch114 -p1 -b .CVE-2012-1140
%patch115 -p1 -b .CVE-2012-1141
%patch116 -p1 -b .CVE-2012-1142
%patch117 -p1 -b .CVE-2012-1143
%patch118 -p1 -b .CVE-2012-1144
%patch119 -p1 -b .bdf-overflow
%patch120 -p1 -b .array-initialization
%patch121 -p1 -b .CVE-2012-5669

%patch122 -p1 -b .CVE-2014-9657
%patch123 -p1 -b .CVE-2014-9658
%patch124 -p1 -b .ft-strncmp
%patch125 -p1 -b .CVE-2014-9675
%patch126 -p1 -b .CVE-2014-9660
%patch127 -p1 -b .CVE-2014-9661a
%patch128 -p1 -b .CVE-2014-9661b
%patch129 -p1 -b .CVE-2014-9663
%patch130 -p1 -b .CVE-2014-9664a
%patch131 -p1 -b .CVE-2014-9664b
%patch132 -p1 -b .CVE-2014-9667
%patch133 -p1 -b .CVE-2014-9669
%patch134 -p1 -b .CVE-2014-9670
%patch135 -p1 -b .CVE-2014-9671
%patch136 -p1 -b .CVE-2014-9673
%patch137 -p1 -b .CVE-2014-9674a
%patch138 -p1 -b .unsigned-long
%patch139 -p1 -b .CVE-2014-9674b
%patch140 -p1 -b .pvf-read-a
%patch141 -p1 -b .pvf-read-b
%patch142 -p1 -b .fix-buffer-size

%build

%configure --disable-static CFLAGS="$CFLAGS -fno-strict-aliasing"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' builds/unix/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' builds/unix/libtool
make %{?_smp_mflags}

%if %{with_xfree86}
# Build demos
pushd ft2demos-%{version}
make TOP_DIR=".."
popd
%endif

# Convert FTL.txt to UTF-8
pushd docs
iconv -f latin1 -t utf-8 < FTL.TXT > FTL.TXT.tmp && \
touch -r FTL.TXT FTL.TXT.tmp && \
mv FTL.TXT.tmp FTL.TXT
popd


%install
rm -rf $RPM_BUILD_ROOT


%makeinstall gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

{
  for ftdemo in ftbench ftchkwd ftdump ftlint ftmemchk ftvalid ; do
      builds/unix/libtool --mode=install install -m 755 ft2demos-%{version}/bin/$ftdemo $RPM_BUILD_ROOT/%{_bindir}
  done
}
%if %{with_xfree86}
{
  for ftdemo in ftdiff ftgamma ftgrid ftmulti ftstring fttimer ftview ; do
      builds/unix/libtool --mode=install install -m 755 ft2demos-%{version}/bin/$ftdemo $RPM_BUILD_ROOT/%{_bindir}
  done
}
%endif

# fix multilib issues
%ifarch x86_64 s390x ia64 ppc64 alpha sparc64
%define wordsize 64
%else
%define wordsize 32
%endif

mv $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h \
   $RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig-%{wordsize}.h
cat >$RPM_BUILD_ROOT%{_includedir}/freetype2/freetype/config/ftconfig.h <<EOF
#ifndef __FTCONFIG_H__MULTILIB
#define __FTCONFIG_H__MULTILIB

#include <bits/wordsize.h>

#if __WORDSIZE == 32
# include "ftconfig-32.h"
#elif __WORDSIZE == 64
# include "ftconfig-64.h"
#else
# error "unexpected value for __WORDSIZE macro"
#endif

#endif 
EOF

# Don't package static a or .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerpostun -- freetype < 2.0.5-3
{
  # ttmkfdir updated - as of 2.0.5-3, on upgrades we need xfs to regenerate
  # things to get the iso10646-1 encoding listed.
  for I in %{_datadir}/fonts/*/TrueType /usr/share/X11/fonts/TTF; do
      [ -d $I ] && [ -f $I/fonts.scale ] && [ -f $I/fonts.dir ] && touch $I/fonts.scale
  done
  exit 0
}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libfreetype.so.*
%doc README
%doc docs/LICENSE.TXT docs/FTL.TXT docs/GPL.TXT
%doc docs/CHANGES docs/VERSION.DLL docs/formats.txt docs/ft2faq.html

%files demos
%defattr(-,root,root)
%{_bindir}/ftbench
%{_bindir}/ftchkwd
%{_bindir}/ftdump
%{_bindir}/ftlint
%{_bindir}/ftmemchk
%{_bindir}/ftvalid
%if %{with_xfree86}
%{_bindir}/ftdiff
%{_bindir}/ftgamma
%{_bindir}/ftgrid
%{_bindir}/ftmulti
%{_bindir}/ftstring
%{_bindir}/fttimer
%{_bindir}/ftview
%endif
%doc ChangeLog README

%files devel
%defattr(-,root,root)
%dir %{_includedir}/freetype2
%{_datadir}/aclocal/freetype2.m4
%{_includedir}/freetype2/*
%{_includedir}/*.h
%{_libdir}/libfreetype.so
%{_bindir}/freetype-config
%{_libdir}/pkgconfig/freetype2.pc
%doc docs/design
%doc docs/glyphs
%doc docs/reference
%doc docs/tutorial

%changelog
* Tue Dec 15 2015 Felipe Borges <feborges@redhat.com> - 2.3.11-17
- Fix computation of size of rasterization buffer
- Resolves: #1154625

* Wed Mar  4 2015 Marek Kasik <mkasik@redhat.com> - 2.3.11-16
- Fixes CVE-2014-9657
   - Check minimum size of `record_size'.
- Fixes CVE-2014-9658
   - Use correct value for minimum table length test.
- Fixes CVE-2014-9675
   - New macro that checks one character more than `strncmp'.
- Fixes CVE-2014-9660
   - Check `_BDF_GLYPH_BITS'.
- Fixes CVE-2014-9661
   - Initialize `face->ttf_size'.
   - Always set `face->ttf_size' directly.
   - Exclusively use the `truetype' font driver for loading
     the font contained in the `sfnts' array.
- Fixes CVE-2014-9663
   - Fix order of validity tests.
- Fixes CVE-2014-9664
   - Add another boundary testing.
   - Fix boundary testing.
- Fixes CVE-2014-9667
   - Protect against addition overflow.
- Fixes CVE-2014-9669
   - Protect against overflow in additions and multiplications.
- Fixes CVE-2014-9670
   - Add sanity checks for row and column values.
- Fixes CVE-2014-9671
   - Check `size' and `offset' values.
- Fixes CVE-2014-9673
   - Fix integer overflow by a broken POST table in resource-fork.
- Fixes CVE-2014-9674
   - Fix integer overflow by a broken POST table in resource-fork.
   - Additional overflow check in the summation of POST fragment lengths.
- Work around behaviour of X11's `pcfWriteFont' and `pcfReadFont' functions
- Resolves: #1197738

* Thu Jan 24 2013 Marek Kasik <mkasik@redhat.com> 2.3.11-15
- Fix CVE-2012-5669
    (Use correct array size for checking `glyph_enc')
- Resolves: #903543

* Thu Jul 19 2012 Marek Kasik <mkasik@redhat.com> 2.3.11-14
- A little change in configure part
- Related: #723468

* Tue Apr  3 2012 Marek Kasik <mkasik@redhat.com> 2.3.11-13
- Fix CVE-2012-{1126, 1127, 1130, 1131, 1132, 1134, 1136,
  1137, 1139, 1140, 1141, 1142, 1143, 1144}
- Properly initialize array "result" in
  FT_Outline_Get_Orientation()
- Check bytes per row for overflow in _bdf_parse_glyphs()
- Resolves: #806269

* Tue Nov 15 2011 Marek Kasik <mkasik@redhat.com> 2.3.11-12
- Add freetype-2.3.11-CVE-2011-3439.patch
    (Various loading fixes.)
- Resolves: #754012

* Fri Oct 21 2011 Marek Kasik <mkasik@redhat.com> 2.3.11-11
- Add freetype-2.3.11-CVE-2011-3256.patch
    (Handle some border cases.)
- Resolves: #747084

* Wed Jul 20 2011 Marek Kasik <mkasik@redhat.com> 2.3.11-10
- Use -fno-strict-aliasing instead of __attribute__((__may_alias__))
- Resolves: #723468

* Wed Jul 20 2011 Marek Kasik <mkasik@redhat.com> 2.3.11-9
- Allow FT_Glyph to alias (to pass Rpmdiff)
- Resolves: #723468

* Wed Jul 20 2011 Marek Kasik <mkasik@redhat.com> 2.3.11-8
- Add freetype-2.3.11-CVE-2011-0226.patch
    (Add better argument check for `callothersubr'.)
    - based on patches by Werner Lemberg,
      Alexei Podtelezhnikov and Matthias Drochner
- Resolves: #723468

* Wed Nov 10 2010 Marek Kasik <mkasik@redhat.com> 2.3.11-7
- Add freetype-2.3.11-CVE-2010-3855.patch
    (Protect against invalid `runcnt' values.)
- Resolves: #651762

* Thu Sep 30 2010 Marek Kasik <mkasik@redhat.com> 2.3.11-6
- Add freetype-2.3.11-CVE-2010-2805.patch
    (Fix comparison.)
- Add freetype-2.3.11-CVE-2010-2806.patch
    (Protect against negative string_size. Fix comparison.)
- Add freetype-2.3.11-CVE-2010-2808.patch
    (Check the total length of collected POST segments.)
- Add freetype-2.3.11-CVE-2010-3311.patch
    (Don't seek behind end of stream.)
- Resolves: #638839

* Wed Aug 11 2010 Marek Kasik <mkasik@redhat.com> 2.3.11-5
- Add freetype-2.3.11-CVE-2010-1797.patch
    (Check stack after execution of operations too.
     Skip the evaluations of the values in decoder, if
     cff_decoder_parse_charstrings() returns any error.)
- Resolves: #621624

* Thu Jul 22 2010 Marek Kasik <mkasik@redhat.com> 2.3.11-4
- Add freetype-2.3.11-CVE-2010-2498.patch
    (Assure that `end_point' is not larger than `glyph->num_points')
- Add freetype-2.3.11-CVE-2010-2499.patch
    (Check the buffer size during gathering PFB fragments)
- Add freetype-2.3.11-CVE-2010-2500.patch
    (Use smaller threshold values for `width' and `height')
- Add freetype-2.3.11-CVE-2010-2519.patch
    (Check `rlen' the length of fragment declared in the POST fragment header)
- Add freetype-2.3.11-CVE-2010-2520.patch
    (Fix bounds check)
- Add freetype-2.3.11-CVE-2010-2527.patch
    (Use precision for `%s' where appropriate to avoid buffer overflows)
- Add freetype-2.3.11-axis-name-overflow.patch
    (Avoid overflow when dealing with names of axes)
- Resolves: #613298

* Thu Dec  3 2009 Behdad Esfahbod <behdad@redhat.com> 2.3.11-3
- Add freetype-2.3.11-more-demos.patch
- New demo programs ftmemchk, ftpatchk, and fttimer

* Thu Dec  3 2009 Behdad Esfahbod <behdad@redhat.com> 2.3.11-2
- Second try.  Drop upstreamed patches.

* Thu Dec  3 2009 Behdad Esfahbod <behdad@redhat.com> 2.3.11-1
- 2.3.11

* Thu Jul 30 2009 Behdad Esfahbod <behdad@redhat.com> 2.3.9-6
- Add freetype-2.3.9-aliasing.patch
- Resolves: 513582

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May  7 2009 Matthias Clasen <mclasen@redhat.com> 2.3.9-4
- Don't own /usr/lib/pkgconfig

* Wed Mar 27 2009 Behdad Esfahbod <besfahbo@redhat.com> 2.3.9-3
- Disable subpixel hinting by default.  Was turned on unintentionally.

* Wed Mar 25 2009 Behdad Esfahbod <besfahbo@redhat.com> 2.3.9-2
- Add Provides: freetype-bytecode and freetype-subpixel if built
  with those options.
- Resolves: #155210

* Thu Mar 13 2009 Behdad Esfahbod <besfahbo@redhat.com> 2.3.9-1
- Update to 2.3.9.
- Resolves #489928

* Thu Mar 09 2009 Behdad Esfahbod <besfahbo@redhat.com> 2.3.8-2.1
- Preserve timestamp of FTL.TXT when converting to UTF-8.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Behdad Esfahbod <besfahbo@redhat.com> 2.3.8-1
- Update to 2.3.8
- Remove freetype-autohinter-ligature.patch

* Tue Dec 09 2008 Behdad Esfahbod <besfahbo@redhat.com> 2.3.7-3
- Add full source URL to Source lines.
- Add docs to main and devel package.
- rpmlint is happy now.
- Resolves: #225770

* Fri Dec 05 2008 Behdad Esfahbod <besfahbo@redhat.com> 2.3.7-2
- Add freetype-autohinter-ligature.patch
- Resolves: #368561

* Tue Aug 14 2008 Behdad Esfahbod <besfahbo@redhat.com> 2.3.7-1
- Update to 2.3.7

* Tue Jun 10 2008 Behdad Esfahbod <besfahbo@redhat.com> 2.3.6-1
- Update to 2.3.6

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.3.5-5
- fix license tag
- add sparc64 to list of 64bit arches

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.3.5-4
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 2.3.5-3
- Rebuild for build ID

* Tue Jul 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.5-2
- Change spec file to permit enabling bytecode-interpreter and
  subpixel-rendering without editing spec file.
- Resolves: 249986

* Wed Jul 25 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.5-1
- Update to 2.3.5.
- Drop freetype-2.3.4-ttf-overflow.patch

* Fri Jun 29 2007 Adam Jackson <ajax@redhat.com> 2.3.4-4
- Fix builds/unix/libtool to not emit rpath into binaries. (#225770)

* Thu May 31 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.4-3
- Add freetype-2.3.4-ttf-overflow.patch

* Thu Apr 12 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.4-2
- Add alpha to 64-bit archs (#236166)

* Tue Apr 05 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.4-1
- Update to 2.3.4.

* Thu Apr 05 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.3-2
- Include new demos ftgrid and ftdiff in freetype-demos. (#235478)

* Thu Apr 05 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.3-1
- Update to 2.3.3.

* Fri Mar 09 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.2-1
- Update to 2.3.2.

* Fri Feb 02 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.1-1
- Update to 2.3.1.

* Wed Jan 17 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.0-2
- Add without_subpixel_rendering.
- Drop X11_PATH=/usr.  Not needed anymore.

* Wed Jan 17 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.3.0-1
- Update to 2.3.0.
- Drop upstream patches.
- Drop -fno-strict-aliasing, it should just work.
- Fix typo in ftconfig.h generation.

* Tue Jan 09 2007 Behdad Esfahbod <besfahbo@redhat.com> 2.2.1-16
- Backport binary-search fixes from HEAD
- Add freetype-2.2.1-ttcmap.patch
- Resolves: #208734

- Fix rendering issue with some Asian fonts.
- Add freetype-2.2.1-fix-get-orientation.patch
- Resolves: #207261

- Copy non-X demos even if not compiling with_xfree86.

- Add freetype-2.2.1-zero-item-size.patch, to fix crasher.
- Resolves #214048

- Add X11_PATH=/usr to "make"s, to find modern X.
- Resolves #212199

* Mon Sep 11 2006 Behdad Esfahbod <besfahbo@redhat.com> 2.2.1-10
- Fix crasher https://bugs.freedesktop.org/show_bug.cgi?id=6841
- Add freetype-2.2.1-memcpy-fix.patch

* Thu Sep 07 2006 Behdad Esfahbod <besfahbo@redhat.com> 2.2.1-9
- Add BuildRequires: libX11-devel (#205355)

* Tue Aug 29 2006 Behdad Esfahbod <besfahbo@redhat.com> 2.2.1-8
- Add freetype-composite.patch and freetype-more-composite.patch
  from upstream. (#131851)

* Mon Aug 28 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.1-7
- Require pkgconfig in the -devel package

* Fri Aug 18 2006 Jesse Keating <jkeating@redhat.com> - 2.2.1-6
- pass --disable-static to %%configure. (#172628)

* Thu Aug 17 2006 Jesse Keating <jkeating@redhat.com> - 2.2.1-5
- don't package static libs

* Sun Aug 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.2.1-4.fc6
- fix a problem with the multilib patch (#202366)

* Thu Jul 27 2006 Matthias Clasen  <mclasen@redhat.com> - 2.2.1-3
- fix multilib issues

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.2.1-2.1
- rebuild

* Fri Jul 07 2006 Behdad Esfahbod <besfahbo@redhat.com> 2.2.1-2
- Remove unused BuildRequires

* Fri Jul 07 2006 Behdad Esfahbod <besfahbo@redhat.com> 2.2.1-1
- Update to 2.2.1
- Remove FreeType 1, to move to extras
- Install new demos ftbench, ftchkwd, ftgamma, and ftvalid
- Enable modules gxvalid and otvalid

* Wed May 17 2006 Karsten Hopp <karsten@redhat.de> 2.1.10-6
- add buildrequires libICE-devel, libSM-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.1.10-5.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.1.10-5.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 18 2005 Bill Nottingham  <notting@redhat.com> 2.1.10-5
- Remove references to obsolete /usr/X11R6 paths

* Tue Nov  1 2005 Matthias Clasen  <mclasen@redhat.com> 2.1.10-4
- Switch requires to modular X

* Fri Oct 21 2005 Matthias Clasen  <mclasen@redhat.com> 2.1.10-3
- BuildRequire gettext 

* Wed Oct 12 2005 Jason Vas Dias <jvdias@redhat.com> 2.1.10-2
- fix 'without_bytecode_interpreter 0' build: freetype-2.1.10-enable-ft2-bci.patch

* Fri Oct  7 2005 Matthias Clasen  <mclasen@redhat.com> 2.1.10-1
- Update to 2.1.10
- Add necessary fixes

* Tue Aug 16 2005 Kristian Høgsberg <krh@redhat.com> 2.1.9-4
- Fix freetype-config on 64 bit platforms.

* Thu Jul 07 2005 Karsten Hopp <karsten@redhat.de> 2.1.9-3
- BuildRequires xorg-x11-devel

* Fri Mar  4 2005 David Zeuthen <davidz@redhat.com> - 2.1.9-2
- Rebuild

* Wed Aug  4 2004 Owen Taylor <otaylor@redhat.com> - 2.1.9-1
- Upgrade to 2.1.9
- Since we are just using automake for aclocal, use it unversioned,
  instead of specifying 1.4.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Apr 19 2004 Owen Taylor <otaylor@redhat.com> 2.1.7-4
- Add patch from freetype CVS to fix problem with eexec (#117743)
- Add freetype-devel to buildrequires and -devel requires
  (Maxim Dzumanenko, #111108)

* Wed Mar 10 2004 Mike A. Harris <mharris@redhat.com> 2.1.7-3
- Added -fno-strict-aliasing to CFLAGS and CXXFLAGS to try to fix SEGV and
  SIGILL crashes in mkfontscale which have been traced into freetype and seem
  to be caused by aliasing issues in freetype macros (#118021)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com> 2.1.7-2.1
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 2.1.7-2
- rebuilt

* Fri Jan 23 2004 Owen Taylor <otaylor@redhat.com> 2.1.7-1
- Upgrade to 2.1.7

* Tue Sep 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- allow compiling without the demos as that requires XFree86
  (this allows bootstrapping XFree86 on new archs)

* Fri Aug  8 2003 Elliot Lee <sopwith@redhat.com> 2.1.4-4.1
- Rebuilt

* Tue Jul  8 2003 Owen Taylor <otaylor@redhat.com> 2.1.4-4.0
- Bump for rebuild

* Wed Jun 25 2003 Owen Taylor <otaylor@redhat.com> 2.1.4-3
- Fix crash with non-format-0 hdmx tables (found by David Woodhouse)

* Mon Jun  9 2003 Owen Taylor <otaylor@redhat.com> 2.1.4-1
- Version 2.1.4
- Relibtoolize to get deplibs right for x86_64
- Use autoconf-2.5x for freetype-1.4 to fix libtool-1.5 compat problem (#91781)
- Relativize absolute symlinks to fix the -debuginfo package 
  (#83521, Mike Harris)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 2.1.3-9
- fix build with gcc 3.3

* Tue Feb 25 2003 Owen Taylor <otaylor@redhat.com>
- Add a memleak fix for the gzip backend from Federic Crozat

* Thu Feb 13 2003 Elliot Lee <sopwith@redhat.com> 2.1.3-7
- Run libtoolize/aclocal/autoconf so that libtool knows to generate shared libraries 
  on ppc64.
- Use _smp_mflags (for freetype 2.x only)

* Tue Feb  4 2003 Owen Taylor <otaylor@redhat.com>
- Switch to using %%configure (should fix #82330)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan  6 2003 Owen Taylor <otaylor@redhat.com> 2.1.3-4
- Make FreeType robust against corrupt fonts with recursive composite 
  glyphs (#74782, James Antill)

* Thu Jan  2 2003 Owen Taylor <otaylor@redhat.com> 2.1.3-3
- Add a patch to implement FT_LOAD_TARGET_LIGHT
- Fix up freetype-1.4-libtool.patch 

* Sat Dec 12 2002 Mike A. Harris <mharris@redhat.com> 2.1.3-2
- Update to freetype 2.1.3
- Removed ttmkfdir sources and patches, as they have been moved from the
  freetype packaging to XFree86 packaging, and now to the ttmkfdir package
- Removed patches that are now included in 2.1.3:
  freetype-2.1.1-primaryhints.patch, freetype-2.1.2-slighthint.patch,
  freetype-2.1.2-bluefuzz.patch, freetype-2.1.2-stdw.patch,
  freetype-2.1.2-transform.patch, freetype-2.1.2-autohint.patch,
  freetype-2.1.2-leftright.patch
- Conditionalized inclusion of freetype 1.4 library.

* Wed Dec 04 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- disable perl, it is not used at all

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com> 2.1.2-11
- Instead of removing unpackaged file, include it in the package.

* Sat Nov 30 2002 Mike A. Harris <mharris@redhat.com> 2.1.2-10
- Attempted to fix lib64 issue in freetype-demos build with X11_LINKLIBS
- Cleaned up various _foodir macros throughtout specfile
- Removed with_ttmkfdir build option as it is way obsolete

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 2.1.2-8
- remove unpackaged files from the buildroot

* Wed Aug 28 2002 Owen Taylor <otaylor@redhat.com>
- Fix a bug with PCF metrics

* Fri Aug  9 2002 Owen Taylor <otaylor@redhat.com>
- Backport autohinter improvements from CVS

* Tue Jul 23 2002 Owen Taylor <otaylor@redhat.com>
- Fix from CVS for transformations (#68964)

* Tue Jul  9 2002 Owen Taylor <otaylor@redhat.com>
- Add another bugfix for the postscript hinter

* Mon Jul  8 2002 Owen Taylor <otaylor@redhat.com>
- Add support for BlueFuzz private dict value, fixing rendering 
  glitch for Luxi Mono.

* Wed Jul  3 2002 Owen Taylor <otaylor@redhat.com>
- Add an experimental FT_Set_Hint_Flags() call

* Mon Jul  1 2002 Owen Taylor <otaylor@redhat.com>
- Update to 2.1.2
- Add a patch fixing freetype PS hinter bug

* Fri Jun 21 2002 Mike A. Harris <mharris@redhat.com> 2.1.1-2
- Added ft rpm build time conditionalizations upon user requests

* Tue Jun 11 2002 Owen Taylor <otaylor@redhat.com> 2.1.1-1
- Version 2.1.1

* Mon Jun 10 2002 Owen Taylor <otaylor@redhat.com>
- Add a fix for PCF character maps

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri May 17 2002 Mike A. Harris <mharris@redhat.com> 2.1.0-2
- Updated freetype to version 2.1.0
- Added libtool fix for freetype 1.4 (#64631)

* Wed Mar 27 2002 Nalin Dahyabhai <nalin@redhat.com> 2.0.9-2
- use "libtool install" instead of "install" to install some binaries (#62005)

* Mon Mar 11 2002 Mike A. Harris <mharris@redhat.com> 2.0.9-1
- Updated to freetype 2.0.9

* Sun Feb 24 2002 Mike A. Harris <mharris@redhat.com> 2.0.8-4
- Added proper docs+demos source for 2.0.8.

* Sat Feb 23 2002 Mike A. Harris <mharris@redhat.com> 2.0.8-3
- Added compat patch so 2.x works more like 1.x
- Rebuilt with new build toolchain

* Fri Feb 22 2002 Mike A. Harris <mharris@redhat.com> 2.0.8-2
- Updated to freetype 2.0.8, however docs and demos are stuck at 2.0.7
  on the freetype website.  Munged specfile to deal with the problem by using
  {oldversion} instead of version where appropriate.  <sigh>

* Sat Feb  2 2002 Tim Powers <timp@redhat.com> 2.0.6-3
- bumping release so that we don't collide with another build of
  freetype, make sure to change the release requirement in the XFree86
  package

* Fri Feb  1 2002 Mike A. Harris <mharris@redhat.com> 2.0.6-2
- Made ttmkfdir inclusion conditional, and set up a define to include
  ttmkfdir in RHL 7.x builds, since ttmkfdir is now moving to the new
  XFree86-font-utils package.

* Wed Jan 16 2002 Mike A. Harris <mharris@redhat.com> 2.0.6-1
- Updated freetype to version 2.0.6

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 2.0.5-4
- automated rebuild

* Fri Nov 30 2001 Elliot Lee <sopwith@redhat.com> 2.0.5-3
- Fix bug #56901 (ttmkfdir needed to list Unicode encoding when generating
  font list). (ttmkfdir-iso10646.patch)
- Use _smp_mflags macro everywhere relevant. (freetype-pre1.4-make.patch)
- Undo fix for #24253, assume compiler was fixed.

* Mon Nov 12 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0.5-2
- Fix build with gcc 3.1 (#56079)

* Sun Nov 11 2001 Mike A. Harris <mharris@redhat.com> 2.0.5-1
- Updated freetype to version 2.0.5

* Sat Sep 22 2001 Mike A. Harris <mharris@redhat.com> 2.0.4-2
- Added new subpackage freetype-demos, added demos to build
- Disabled ftdump, ftlint in utils package favoring the newer utils in
  demos package.

* Tue Sep 11 2001 Mike A. Harris <mharris@redhat.com> 2.0.4-1
- Updated source to 2.0.4
- Added freetype demo's back into src.rpm, but not building yet.

* Wed Aug 15 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-7
- Changed package to use {findlang} macro to fix bug (#50676)

* Sun Jul 15 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-6
- Changed freetype-devel to group Development/Libraries (#47625)

* Mon Jul  9 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0.3-5
- Fix up FT1 headers to please Qt 3.0.0 beta 2

* Sun Jun 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0.3-4
- Add ft2build.h to -devel package, since it's included by all other
  freetype headers, the package is useless without it

* Thu Jun 21 2001 Nalin Dahyabhai <nalin@redhat.com> 2.0.3-3
- Change "Requires: freetype = name/ver" to "freetype = version/release",
  and move the requirements to the subpackages.

* Mon Jun 18 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-2
- Added "Requires: freetype = name/ver"

* Tue Jun 12 2001 Mike A. Harris <mharris@redhat.com> 2.0.3-1
- Updated to Freetype 2.0.3, minor specfile tweaks.
- Freetype2 docs are is in a separate tarball now. Integrated it.
- Built in new environment.

* Fri Apr 27 2001 Bill Nottingham <notting@redhat.com>
- rebuild for C++ exception handling on ia64

* Sat Jan 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Build ttmkfdir with -O0, workaround for Bug #24253

* Fri Jan 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- libtool is used to build libttf, so use libtool to link ttmkfdir with it
- fixup a paths for a couple of missing docs

* Thu Jan 11 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update ttmkfdir

* Wed Dec 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 2.0.1 and 1.4
- Mark locale files as such

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- move .la file to devel pkg
- FHS paths

* Thu Feb 17 2000 Preston Brown <pbrown@redhat.com>
- revert spaces patch, fix up some foundry names to match X ones

* Mon Feb 07 2000 Nalin Dahyabhai <nalin@redhat.com>
- add defattr, ftmetric, ftsbit, ftstrtto per bug #9174

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description and summary

* Wed Jan 12 2000 Preston Brown <pbrown@redhat.com>
- make ttmkfdir replace spaces in family names with underscores (#7613)

* Tue Jan 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.3.1
- handle RPM_OPT_FLAGS

* Wed Nov 10 1999 Preston Brown <pbrown@redhat.com>
- fix a path for ttmkfdir Makefile

* Thu Aug 19 1999 Preston Brown <pbrown@redhat.com>
- newer ttmkfdir that works better, moved ttmkfdir to /usr/bin from /usr/sbin
- freetype utilities moved to subpkg, X dependency removed from main pkg
- libttf.so symlink moved to devel pkg

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- fixed the doc file list

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- added ttmkfdir

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- update to 1.2

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize to sanitize config.sub and get ARM support
- dispoze of the patch (not necessary anymore)

* Wed Oct 21 1998 Preston Brown <pbrown@redhat.com>
- post/postun sections for ldconfig action.

* Tue Oct 20 1998 Preston Brown <pbrown@redhat.com>
- initial RPM, includes normal and development packages.
