Name:           aegisub-plugin-dependency-control
Version:        0.7.0
Release:        1%{?dist}
Summary:        Enterprise Aegisub Script Management
# vendored dkjson.lua also under MIT, see file header
#     modules/l0/dkjson/vendor/dkjson.lua
License:        MIT
URL:            https://github.com/TypesettingTools/DependencyControl
Source0:        %{url}/archive/v%{version}.tar.gz

# this also disables debug packages
BuildArch:      noarch
# copied from aegisub.spec; not required on COPR, but whatever
ExcludeArch: ppc64le s390x

Requires:       aegisub
# modules/l0/DependencyControl/Downloader.moon:208
Requires:       libcurl
# modules/l0/DependencyControl/hash.moon:114
Requires:       openssl-libs


%description
DependencyControl provides versioning, automatic script update, dependency
management and script management services to Aegisub macros and modules.


%prep
%autosetup -n DependencyControl-%{version}


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
* Fri Jul 24 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.7.0-1
- new version
- remove `ffi-experiments` and `luajson` per upstream requirements
- remove `lua-moonscript` BuildReq for `ffi-exp` build
- drop now-unused ISC license
- add `openssl-libs` and `libcurl` as `Requires`
- update Summary and Description
- change package to `noarch` as it doesn't contain any binaries
- add ExcludeArch
- add `STYLE.md` as `%doc`

* Fri Jun 27 2025 Tarulia <mihawk.90+git@googlemail.com> - 0.6.4~alpha-2
- Use wildcards to disown automation directory

* Fri Jun 27 2025 Tarulia <mihawk.90+git@googlemail.com>
- Initial Package for version 0.6.4-alpha

