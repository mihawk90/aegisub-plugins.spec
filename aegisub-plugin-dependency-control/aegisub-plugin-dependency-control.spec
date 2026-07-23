# spec file adapted from AUR PKGBUILD
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=aegisub-dependency-control

# disable this because honestly I can't be bothered
%global debug_package %{nil} 

%global ffiexpver b8897ead55b84ec4148e900882bff8336b38f939
%global luajsonver 1.3.3

Name:           aegisub-plugin-dependency-control
Version:        0.6.4~alpha
Release:        2%{?dist}
Summary:        Aegisub Script Manager
License:        'MIT' 'ISC'
URL:            https://github.com/TypesettingTools/DependencyControl
Source0:        https://github.com/TypesettingTools/DependencyControl/archive/v%{version_no_tilde}.tar.gz
Source1:        https://github.com/TypesettingTools/ffi-experiments/archive/%{ffiexpver}.tar.gz
Source2:        https://github.com/harningt/luajson/archive/%{luajsonver}.tar.gz

BuildRequires:  g++ meson lua-moonscript libcurl-devel
Requires:       aegisub

%description
Package manager for scripts for the Aegisub subtitle editor

%prep
%autosetup -n DependencyControl-%{version_no_tilde}


# unpack ffi-experiments
mkdir -p %{_builddir}/SOURCES/ffi-experiments
tar -x --gzip -f %{SOURCE1} -C %{_builddir}/SOURCES/ffi-experiments --strip-components=1

# unpack luajson
mkdir -p %{_builddir}/SOURCES/luajson
tar -x --gzip -f %{SOURCE2} -C %{_builddir}/SOURCES/luajson --strip-components=1


%build
cd %{_builddir}/SOURCES/ffi-experiments
meson build
meson compile -C build


%install
%define aegiauto %{buildroot}%{_datadir}/aegisub/automation
mkdir -p "%{aegiauto}/include/l0"

cp -r modules/* "%{aegiauto}/include/l0"
install -D -m 644 macros/* -t "%{aegiauto}/autoload"

# ffiexp
cd "%{_builddir}/SOURCES/ffi-experiments"
install -D -m644 build/bad-mutex/BadMutex.lua                 "%{aegiauto}/include/BM/BadMutex.lua"
install -D -m644 build/bad-mutex/libBadMutex.so               "%{aegiauto}/include/BM/BadMutex/libBadMutex.so"
install -D -m644 build/download-manager/DownloadManager.lua   "%{aegiauto}/include/DM/DownloadManager.lua"
install -D -m644 build/download-manager/libDownloadManager.so "%{aegiauto}/include/DM/DownloadManager/libDownloadManager.so"
install -D -m644 build/precise-timer/PreciseTimer.lua         "%{aegiauto}/include/PT/PreciseTimer.lua"
install -D -m644 build/precise-timer/libPreciseTimer.so       "%{aegiauto}/include/PT/PreciseTimer/libPreciseTimer.so"
install -D -m644 build/requireffi/requireffi.lua              "%{aegiauto}/include/requireffi/requireffi.lua"

install -D -m644 LICENSE "%{buildroot}%{_datadir}/licenses/%{name}/LICENSE_ffi-experiments"

# luajson
cd "%{_builddir}/SOURCES/luajson"
install -m 644 lua/json.lua "%{aegiauto}/include"
cp -r lua/json "%{aegiauto}/include"

install -D -m644 LICENSE "%{buildroot}%{_datadir}/licenses/%{name}/LICENSE_luajson"

%files
%license LICENSE
%license %{_datadir}/licenses/%{name}/LICENSE_ffi-experiments
%license %{_datadir}/licenses/%{name}/LICENSE_luajson
%doc README.md
%{_datadir}/aegisub/automation/include/*
%{_datadir}/aegisub/automation/autoload/*


%changelog
* Fri Jun 27 2025 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4~alpha-2
- Use wildcards to disown automation directory

* Fri Jun 27 2025 Tarulia <mihawk.90+git@googlemail.com>
- Initial Package for version 0.6.4-alpha

