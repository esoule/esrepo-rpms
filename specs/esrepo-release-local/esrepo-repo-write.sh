#!/bin/sh

function show_bin_repo()
{
local name=$1
local desc=$2
local enabled=0
if [ $name = main ] ; then
    enabled=1
fi
echo "[esrepo-${name}]"
echo "name=esrepo for Enterprise Linux \$releasever - ${desc} - \$basearch"
echo "baseurl=${TOP_URL}/${name}/packages/centos/\$releasever/\$basearch/"
echo "enabled=${enabled}"
echo "gpgcheck=0"
echo ""
return 0
}

function show_debuginfo_repo()
{
local name=$1
local desc=$2
local enabled=0
echo "[esrepo-${name}-debuginfo]"
echo "name=esrepo for Enterprise Linux \$releasever - ${desc} Debuginfo - \$basearch"
echo "baseurl=${TOP_URL}/${name}/debuginfo/centos/\$releasever/\$basearch/"
echo "enabled=${enabled}"
echo "gpgcheck=0"
echo ""
return 0
}

function show_source_repo()
{
local name=$1
local desc=$2
local enabled=0
echo "[esrepo-${name}-source]"
echo "name=esrepo for Enterprise Linux \$releasever - ${desc} Sources"
echo "baseurl=${TOP_URL}/${name}/packages/centos/\$releasever/sources/"
echo "enabled=${enabled}"
echo "gpgcheck=0"
echo ""
return 0
}

if [ -z "${TOP_URL}" ] ; then
    TOP_URL='http://centos.mirror.local/ftp/pub/linux/esrepo'
fi

if [ -z "${SITE_DIST_STR}" ] ; then
    SITE_DIST_STR='local'
fi

echo "# yum repository configuration for esrepo"
echo "# site=${SITE_DIST_STR}"
echo "# Top URL=${TOP_URL}"
echo ""

show_bin_repo main Main
show_bin_repo extras Extras
show_bin_repo testing Testing

show_source_repo main Main
show_source_repo extras Extras
show_source_repo testing Testing

show_debuginfo_repo main Main
show_debuginfo_repo extras Extras
show_debuginfo_repo testing Testing

