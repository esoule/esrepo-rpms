#!/bin/sh

releasever=6

function guess_repo_name()
{
	local filename=$1
	local repo_name
	case $filename in
	fsarchiver-*|coan-*|k4dirstat-*|krusader-*|rtems-4.6au-*|rtems-4.6-*|mtd-utils-*|unifdef-*|os-tweaks*|ttt-*|xca*|esrepo-release-*)
		repo_name=main
		;;
	bcpp-*|uncrustify*)
		repo_name=main
		;;
	cppunit113*)
		repo_name=main
		;;
	ccache-*|cppunit*|firstinst*|freetype-*|emacs-git-*|git-*|gitk-*|gitweb-*|perl-Git-*|livesys*|minicom-*|squashfs-tools-*|wine-*|vim-*|wireshark-*)
		repo_name=extras
		;;
	coccinelle-*|hevea-*|latexmk-*|ocaml-*)
		repo_name=extras
		;;
	cproto*|keepalived*|quilt*|rtems-4.6ng6-*|rtems-4.6ng10-*|rtems-4.6ng11-*)
		repo_name=testing
		;;
	fcompat-*)
		repo_name=testing
		;;
	livecd-tools*|python-imgcreate*)
		repo_name=extras
		;;
	crosstool-build-filesystem-*|re*fonts*)
		repo_name=internal
		;;
	*)
		repo_name=invalidreponame
		;;
	esac
	echo $repo_name
	return 0
}

function guess_debug_info_section()
{
	local filename=$1
	local debuginfo_section_name=
	case $filename in
	*-debuginfo-*.rpm)
		debuginfo_section_name=debuginfo
		;;
	*.rpm)
		debuginfo_section_name=packages
		;;
	*)
		debuginfo_section_name=invalidsection
		;;
	esac
	echo $debuginfo_section_name
	return 0
}

function guess_binary_rpm_section()
{
	local arch_name=$1
	local filename=$2
	local binary_rpm_section_name=
	case $filename in
	*.src.rpm)
		binary_rpm_section_name=sources/SRPMS
		;;
	*.rpm)
		binary_rpm_section_name=$arch_name/RPMS
		;;
	*)
		binary_rpm_section_name=invalidsection
		;;
	esac
	echo $binary_rpm_section_name
	return 0
}

function do_rpm_sort()
{
	local arch_name=$1
	shift
	case $arch_name in
	i386|x86_64)
		;;
	*)
		echo "Invalid arch $arch_name" >&2
		return 1
		;;
	esac
	echo "Arch $arch_name"
	for filename in "$@" ; do
		if [ ! -f "$filename" ] ; then
			continue
		fi
		local filename_base=`basename $filename`
		local repo_name=`guess_repo_name $filename_base`
		local debuginfo_section_name=`guess_debug_info_section $filename_base`
		local binary_rpm_section_name=`guess_binary_rpm_section $arch_name $filename_base`
		mkdir -v -p out/$repo_name/$debuginfo_section_name/centos/$releasever/$binary_rpm_section_name
		cp -v --no-clobber $filename out/$repo_name/$debuginfo_section_name/centos/$releasever/$binary_rpm_section_name/$filename_base
	done
}

do_rpm_sort "$@"

