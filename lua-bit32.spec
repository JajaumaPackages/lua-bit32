# version detection makes no sense 
%global luaver 5.1
# for compiled modules
%global lualibdir %{_libdir}/lua/%{luaver}

Name:           lua-bit32
Version:        5.3.0
Release:        1%{?dist}
Summary:        Lua 5.2 bit manipulation library

License:        MIT
URL:            https://luarocks.org/modules/siffiejoe/bit32
Source0:        https://github.com/keplerproject/lua-compat-5.2/archive/bitlib-%{version}.tar.gz

BuildRequires:  lua-devel >= %{luaver}
Requires:       lua(abi) >= %{luaver}

%description
bit32 is the native Lua 5.2 bit manipulation library, backported to Lua 5.1.

%prep
%setup -q -n lua-compat-5.2-bitlib-%{version}


%build
%{__cc} %{optflags} -fPIC -Ic-api -c lbitlib.c -o lbitlib.o
%{__cc} %{__global_ldflags} -shared -o bit32.so lbitlib.o


%install
rm -rf %{buildroot}
install -d %{buildroot}%{lualibdir}
install -p -m755 bit32.so %{buildroot}%{lualibdir}


%files
%doc LICENSE
%{lualibdir}/*


%changelog
* Sun Apr 17 2016 Jajauma's Packages <jajauma@yandex.ru> - 5.3.0-1
- Public release
