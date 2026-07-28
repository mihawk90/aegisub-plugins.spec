# The build doesn't produce symbols and build fails without them
# No idea how I could force any
%global debug_package %{nil}

%global date   20190220
%global commit faf6f3b3d1a2e0b400fad2d6b7534f073044cc65

Name:           scxvid
Version:        1^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        1%{?dist}
Summary:        Standalone, cross-platform port of the AviSynth SCXvid plugin
# no explicit license in upstream, but compiles against GPL2 lib
License:        GPL-2.0-or-later
URL:            https://github.com/soyokaze/SCXvid-standalone
Source0:        %{url}/archive/%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  xvidcore-devel

Supplements:    aegisub


%description
Uses the Xvid encoder library to extract frame information. Primarily useful for
identifying scene changes (i.e. key frames) for use in Aegisub or similar tools.


%prep
%autosetup -n SCXvid-standalone-%{commit}


%build
%build_cc -o scxvid scxvid.c -fPIE -lxvidcore -pie


%install
install -D -m 755 scxvid -t "%{buildroot}%{_bindir}"


%check
# no tests


%files
%doc README.md
%{_bindir}/scxvid


%changelog
* Tue Jul 28 2026 Tarulia <mihawk.90+git@googlemail.com> - 1^20190220.faf6f3b-1
- Initial packaging

