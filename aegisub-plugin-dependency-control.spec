# spec file adapted from AUR PKGBUILD
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=aegisub-dependency-control

%global date   20260722
%global commit fd418320cf280d23a318447ae5fe4676673b8ef7

Name:           aegisub-plugin-dependency-control
Version:        0.6.4^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        1%{?dist}
Summary:        Aegisub Script Manager
# vendored dkjson.lua also under MIT, see file header
#     modules/l0/dkjson/vendor/dkjson.lua
License:        'MIT'
URL:            https://github.com/TypesettingTools/DependencyControl
Source0:        https://github.com/TypesettingTools/DependencyControl/archive/%{commit}.tar.gz

# this also disables debug packages
BuildArch:      noarch

Requires:       aegisub
# requires unversioned SO at runtime
Requires:       libcurl-devel
# /modules/l0/DependencyControl/hash.moon#L114
Requires:       libcrypto.so.3


%description
Package manager for scripts for the Aegisub subtitle editor


%prep
%autosetup -n DependencyControl-%{commit}


%build


%install
%define aegiauto %{buildroot}%{_datadir}/aegisub/automation

# TODO: this should use install, but:
#   install throws an error and fails the build
#   install: omitting directory 'macros/l0.DependencyControl.Toolbox'

# install -m 644 modules/* "%{aegiauto}/include/l0"
mkdir -p "%{aegiauto}/include/"
cp -r modules/* "%{aegiauto}/include/"
chmod -x,u=rwX,g=rX,o=rX -R "%{aegiauto}/include/"

# install -D -m 644 macros/* -t "%{aegiauto}/autoload"
mkdir -p "%{aegiauto}/autoload"
cp -r macros/* "%{aegiauto}/autoload"
chmod -x,u=rwX,g=rX,o=rX -R "%{aegiauto}/autoload"


%files
%license LICENSE
%doc README.md
%doc STYLE.md
%{_datadir}/aegisub/automation/include/*
%{_datadir}/aegisub/automation/autoload/*


%changelog
* Wed Jul 22 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4^20260722.fd41832-1
- drop now-unused ISC license
- remove `ffi-experiments` and `luajson` per upstream requirements
- change package to `noarch` as it doesn't contain any binaries
- move `libcurl-devel` to `Require` because it's a runtime dependency
- remove `lua-moonscript` dependency required for `ffi-exp` build
- change `%autosetup` path for commit-tarball
- WIP: use `cp -r` for macros and modules, should ideally use `install`
- add `STYLE.md` as `%doc`

* Fri Jun 27 2025 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4~alpha-2
- Use wildcards to disown automation directory

* Fri Jun 27 2025 Tarulia <mihawk.90+git@googlemail.com>
- Initial Package for version 0.6.4-alpha

