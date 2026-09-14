# The build doesn't produce symbols and build fails without them
# No idea how I could force any
%global debug_package %{nil}

%global libass  0.17.5

Name:           aegisub-plugin-subinspector
Version:        0.6.0
Release:        1%{?dist}
Summary:        Low-level subtitle inspection library
# libSubInspector = MIT
# Inspector.moon  = CC0 = CC0-1.0
License:        MIT and CC0-1.0
URL:            https://github.com/TypesettingTools/SubInspector
Source0:        %{url}/archive/v%{version}.tar.gz
# now hard-depends on vendored libass
# see patch in subprojects/libass.wrap
Source1:        https://github.com/libass/libass/releases/download/%{libass}/libass-%{libass}.tar.xz

# copied from aegisub.spec; not required on COPR, but whatever
ExcludeArch:    ppc64le s390x

BuildRequires:  meson ninja-build gcc cmake
# we don't actually need libass-devel, but it's easier for dependencies
BuildRequires:  libass-devel nasm

Requires:       aegisub

Provides:       bundled(libSubInspector.so)


%description
SubInspector is a library for low level inspection and analysis of subtitles
post-rasterization.

It targets the Advanced SubStation Alpha subtitle format (ASS) and uses libass
to parse and rasterize the subtitles.


%prep
%autosetup -n SubInspector-%{version}
tar -x --xz -f %{SOURCE1} -C subprojects
meson setup build


%build
cd build
%ninja_build


%install
%global aegiauto %{buildroot}%{_datadir}/aegisub/automation

# TODO: throws W: arch-dependent-file-in-usr-share
# but Inspector.moon:76 uses relative path
install -D -m644 examples/Aegisub/Inspector.moon "%{aegiauto}/include/SubInspector/Inspector.moon"
install -D -m644 build/src/libSubInspector.so    "%{aegiauto}/include/SubInspector/Inspector/libSubInspector.so"


%check
# no tests present


%files
%license COPYING
%{_datadir}/aegisub/automation/include/*


%changelog
* Mon Sep 14 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.0-1
- new version
- update License field (previously missed CC0)
- add vendored libass for required patch

* Tue Jul 28 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.5.2^20190824.872fec2-1
- Initial packaging

