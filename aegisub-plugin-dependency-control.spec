# spec file adapted from AUR PKGBUILD
# https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=aegisub-dependency-control

%global date   20260723.1
%global commit 619842f5e989bb7482d5172da835f6ffd2988a4e

Name:           aegisub-plugin-dependency-control-pre
Version:        0.6.4^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        1%{?dist}
Summary:        Aegisub Script Manager
# vendored dkjson.lua also under MIT, see file header
#     modules/l0/dkjson/vendor/dkjson.lua
License:        MIT
URL:            https://github.com/TypesettingTools/DependencyControl
Source0:        %{url}/archive/%{commit}.tar.gz

# this also disables debug packages
BuildArch:      noarch
# copied from aegisub.spec; not required on COPR, but whatever
ExcludeArch: ppc64le s390x

Requires:       aegisub
Requires:       libcurl
# modules/l0/DependencyControl/hash.moon#L114
Requires:       libcrypto.so.3


%description
Package manager for scripts for the Aegisub subtitle editor


%prep
%autosetup -n DependencyControl-%{commit}


%build
# nothing to build


%install
%define aegiauto %{buildroot}%{_datadir}/aegisub/automation

# TODO: this should use install, but:
#   install throws an error and fails the build
#   install: omitting directory 'macros/l0.DependencyControl.Toolbox'

# TODO: Once we have releases, copy everything as is
#   Upstream packages the tarballs in the correct structure,
#   so we don't need to do any sorting ourselves

# mkdir -p "%{aegiauto}"
# cp -r . "%{aegiauto}"
# chmod -x,u=rwX,g=rX,o=rX -R "%{aegiauto}"

# install -m 644 modules/* "%{aegiauto}/include/l0"
mkdir -p "%{aegiauto}/include/"
cp -r modules/* "%{aegiauto}/include/"
chmod -x,u=rwX,g=rX,o=rX -R "%{aegiauto}/include/"

# install -D -m 644 macros/* -t "%{aegiauto}/autoload"
mkdir -p "%{aegiauto}/autoload"
cp -r macros/* "%{aegiauto}/autoload"
chmod -x,u=rwX,g=rX,o=rX -R "%{aegiauto}/autoload"


%check
# TODO: Release tarballs contain tests, so let's run them if we can


%files
%license LICENSE
%doc README.md
%doc STYLE.md
%{_datadir}/aegisub/automation/include/*
%{_datadir}/aegisub/automation/autoload/*


%changelog
* Thu Jul 23 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4^20260723.1.619842f-1
- New version

* Wed Jul 22 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4^20260722.2.f116ef3-2
- Add ExcludeArch

* Wed Jul 22 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4^20260722.2.f116ef3-1
- New version

* Wed Jul 22 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4^20260722.fd41832-3
- REVERT ME: Use distinct package name

* Wed Jul 22 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4^20260722.fd41832-2
- Swap `libcurl-devel` for `libcurl`

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

