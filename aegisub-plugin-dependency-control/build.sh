#!/bin/sh

### preparation

spec=./aegisub-plugin-dependency-control.spec
frel=$(rpm -E %fedora)

if [ "$1" == "all" ]; then
	echo "Building for Fedora Release $(($frel - 1)), ${frel}, and $(($frel + 1))."
	./build.sh frel $(($frel - 1))
	./build.sh frel $(($frel + 1))
	./build.sh $2
	exit
fi;

if [ "$1" == "frel" ] && [ "$2" != "" ]; then
	frel=$2
	echo ">>>>>>> Fedora ${frel} starting."
else
	echo ">>>>>>> Fedora ${frel} starting - defaulted."
fi;

# delimited by spaces, every space is a new "field" for cut, hence field 9 for the version/release
mver=$(cat $spec | grep Version\: | cut -d" " -f9)
rver=$(cat $spec | grep Release\: | cut -d" " -f9 | sed -e 's/%{?dist}//')

set -x
### build phase
rm ./f_downloads/*.tar.gz
spectool -g $spec --directory ./f_downloads
rm -rf ./f_upload/$frel/
mock -r fedora+rpmfusion_nonfree-$frel-x86_64 --sources=./f_downloads --spec=$spec --resultdir=./f_upload/$frel/ --rootdir=/home/tarulia/Development/aegisub/aegisub-plugin-dependency-control.spec/mock_root --no-cleanup-after

pushd ./f_upload/$frel && \
#sha512sum aegisub-plugin-dependency-control-$mver-$rver.fc$frel.x86_64.rpm > aegisub-plugin-dependency-control-$mver-$rver.fc$frel.sha512 && \
\
if [ "$1" == "install" ]; then
	sudo dnf install aegisub-plugin-dependency-control-$mver-$rver.fc$frel.x86_64.rpm
fi

popd

set +x

echo "<<<<<<< Fedora ${frel} done."

