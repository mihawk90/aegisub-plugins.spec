%global srcname DependencyControl

Name:           aegisub-plugin-dependency-control
Version:        0.8.1
Release:        2%{?dist}
Summary:        Enterprise Aegisub Script Management
# vendored dkjson.lua also under MIT, see file header
#     modules/l0/dkjson/vendor/dkjson.lua
License:        MIT
URL:            https://github.com/TypesettingTools/DependencyControl
Source0:        %{url}/releases/download/v%{version}/%{srcname}-v%{version}.zip

# Not included in zip (for now?)
%global rawurl %(u=%{url}; echo ${u/github/raw.githubusercontent})
Source100:      %{rawurl}/refs/tags/v%{version}/LICENSE
Source101:      %{rawurl}/refs/tags/v%{version}/README.md
Source102:      %{rawurl}/refs/tags/v%{version}/STYLE.md

# this also disables debug packages
BuildArch:      noarch
# copied from aegisub.spec; not required on COPR, but whatever
ExcludeArch:    ppc64le s390x

Requires:       aegisub
# modules/l0/DependencyControl/Downloader.moon:208
Requires:       libcurl
# modules/l0/DependencyControl/hash.moon:114
Requires:       openssl-libs


%description
DependencyControl provides versioning, automatic script update, dependency
management and script management services to Aegisub macros and modules.


%prep
%autosetup -n "automation"
# copy to sourcedir so we can reference them by filename in %files
cp %{SOURCE100} %{SOURCE101} %{SOURCE102} .


%build
# nothing to build


%install
%define aegiauto %{buildroot}%{_datadir}/aegisub/automation

# TODO: this should use install, but:
#   install throws an error and fails the build
# install -m 644 -D * -t "%{aegiauto}"
#   install: omitting directory 'autoload'
#   install: omitting directory 'include'
#   install: omitting directory 'tests'

mkdir -p "%{aegiauto}"
cp -r */* "%{aegiauto}"
chmod -x,u=rwX,g=rX,o=rX -R "%{aegiauto}"


%check
# TODO: Release tarballs contain tests, so let's run them if we can


%files
%license LICENSE
%doc README.md
%doc STYLE.md
%{_datadir}/aegisub/automation/*


%changelog
* Sat Jul 25 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.8.1-2
- DepCtrl: Fix rpmlint `files-duplicate` warning

* Sat Jul 25 2026 Tarulia <mihawk.90+git@googlemail.com> - 0.8.1-1
- new version
- use upstream release archive
  - add LICENSE, README, and STYLE not included in archive

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

