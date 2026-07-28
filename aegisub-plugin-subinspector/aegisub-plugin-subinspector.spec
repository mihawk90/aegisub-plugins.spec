# The build doesn't produce symbols and build fails without them
# No idea how I could force any
%global debug_package %{nil}

%global date   20190824
%global commit 872fec2caa26b416eae1c118cb778d714348299a

Name:           aegisub-plugin-subinspector
Version:        0.5.2^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        1%{?dist}
Summary:        Low-level subtitle inspection library
License:        MIT
URL:            https://github.com/TypesettingTools/SubInspector
Source0:        %{url}/archive/%{commit}.tar.gz

# copied from aegisub.spec; not required on COPR, but whatever
ExcludeArch:    ppc64le s390x

BuildRequires:  meson ninja-build gcc cmake
BuildRequires:  libass-devel

Requires:       aegisub

Provides:       bundled(libSubInspector.so)


%description
SubInspector is a library for low level inspection and analysis of subtitles
post-rasterization.

It targets the Advanced SubStation Alpha subtitle format (ASS) and uses libass
to parse and rasterize the subtitles.


%prep
%autosetup -n SubInspector-%{commit}
meson build


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
* Tue Jul 28 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.5.2^20190824.872fec2-1
- Initial packaging

