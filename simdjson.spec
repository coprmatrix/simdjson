#
# spec file for package simdjson
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define so_version @SIMDJSON_LIB_SOVERSION@

Name:           simdjson
Version:        v3.9.5
Release:        0
Summary:        Parsing gigabytes of JSON per second
License:        Apache-2.0
URL:            https://github.com/simdjson/simdjson
Source:         %{name}-%{version}.tar
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it.
We need a fresh approach. The simdjson library uses commonly available SIMD
instructions and microparallel algorithms to parse JSON 4x faster than
RapidJSON and 25x faster than JSON for Modern C++.
* Fast: Over 4x faster than commonly used production-grade JSON parsers.
* Record Breaking Features: Minify JSON at 6 GB/s, validate UTF-8 at 13 GB/s,
  NDJSON at 3.5 GB/s.
* Easy: First-class, easy to use and carefully documented APIs.
* Strict: Full JSON and UTF-8 validation, lossless parsing. Performance with no
  compromises.
* Automatic: Selects a CPU-tailored parser at runtime. No configuration needed.
* Reliable: From memory allocation to error handling, simdjson's design avoids
  surprises.
* Peer Reviewed: Our research appears in venues like VLDB Journal, Software:
  Practice and Experience.

%package devel
Summary:        Parsing gigabytes of JSON per second
Requires:       %{name}
Requires:       libsimdjson%{so_version}
Requires:       pkgconfig

%description devel
JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it.
We need a fresh approach. The simdjson library uses commonly available SIMD
instructions and microparallel algorithms to parse JSON 4x faster than
RapidJSON and 25x faster than JSON for Modern C++.
* Fast: Over 4x faster than commonly used production-grade JSON parsers.
* Record Breaking Features: Minify JSON at 6 GB/s, validate UTF-8 at 13 GB/s,
  NDJSON at 3.5 GB/s.
* Easy: First-class, easy to use and carefully documented APIs.
* Strict: Full JSON and UTF-8 validation, lossless parsing. Performance with no
  compromises.
* Automatic: Selects a CPU-tailored parser at runtime. No configuration needed.
* Reliable: From memory allocation to error handling, simdjson's design avoids
  surprises.
* Peer Reviewed: Our research appears in venues like VLDB Journal, Software:
  Practice and Experience.

%package -n libsimdjson%{so_version}
Summary:        Parsing gigabytes of JSON per second

%description -n libsimdjson%{so_version}
JSON is everywhere on the Internet. Servers spend a *lot* of time parsing it.
We need a fresh approach. The simdjson library uses commonly available SIMD
instructions and microparallel algorithms to parse JSON 4x faster than
RapidJSON and 25x faster than JSON for Modern C++.
* Fast: Over 4x faster than commonly used production-grade JSON parsers.
* Record Breaking Features: Minify JSON at 6 GB/s, validate UTF-8 at 13 GB/s,
  NDJSON at 3.5 GB/s.
* Easy: First-class, easy to use and carefully documented APIs.
* Strict: Full JSON and UTF-8 validation, lossless parsing. Performance with no
  compromises.
* Automatic: Selects a CPU-tailored parser at runtime. No configuration needed.
* Reliable: From memory allocation to error handling, simdjson's design avoids
  surprises.
* Peer Reviewed: Our research appears in venues like VLDB Journal, Software:
  Practice and Experience.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n libsimdjson%{so_version} -p /sbin/ldconfig
%postun -n libsimdjson%{so_version} -p /sbin/ldconfig

%files
%license LICENSE
%doc SECURITY.md README.md

%files devel
%{_includedir}/simdjson.h
%{_libdir}/libsimdjson.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%files -n libsimdjson%{so_version}
%{_libdir}/libsimdjson.so.%{so_version}*

%changelog
