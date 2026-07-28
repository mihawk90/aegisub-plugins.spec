%global date   20230725
%global commit 91a4ac771b08ecffdcc8c084592286961d99c5f2

Name:           aegisub-plugin-yutils
Version:        0^%{date}.%(c=%{commit}; echo ${c:0:7})
Release:        2%{?dist}
Summary:        An ASS typeset utilities library for Aegisub
License:        MIT
URL:            https://github.com/TypesettingTools/Yutils
Source0:        %{url}/archive/%{commit}.tar.gz

# this also disables debug packages
BuildArch:      noarch
# copied from aegisub.spec; not required on COPR, but whatever
ExcludeArch:    ppc64le s390x

Requires:       aegisub
# ffi prefixes "lib" and suffixes ".so" automatically
# https://luajit.org/ext_ffi_api.html#:~:text=clib%20%3D%20ffi.load(name%20%5B%2Cglobal%5D)
# libpango-1.0.so in L270
Requires:       pango-devel

# libpng.so in L440
Recommends:     libpng-devel


%description
Yutils is a Lua library with functions for media decoding, shape manipulation,
advanced math, UTF-8 coded texts, ASS (Advanced Substation Alpha) script parsing
and with some other small helpers.


%prep
%autosetup -n Yutils-%{commit}


%build
# nothing to build


%install
install -D -m 644 src/Yutils.lua -t "%{buildroot}%{_datadir}/aegisub/automation/include"


%check
# There are tests/, but I don't know how to determine if they passed


%files
# license is in fileheader
%doc README.md
%doc docs/*
%{_datadir}/aegisub/automation/include/*


%changelog
* Sat Jul 25 2026 Tarulia <mihawk.90+git@googlemail.com> - 0^20230725.91a4ac7-2
- Fix rpmlint warning

* Thu Jul 23 2026 Tarulia <mihawk.90+git@googlemail.com> - 0^20230725.91a4ac7-1
- Initial packaging

