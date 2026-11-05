Name:		python-phonemizer
Version:	3.4.0
Release:	1
Summary:	Convert text to phonemes
License:	GPL-3.0-or-later
Group:		Development/Python
URL:		https://github.com/bootphon/phonemizer
Source0:	https://files.pythonhosted.org/packages/bc/7d/5a96ddb130552f6365a090b5fd12ace803a95a858e3f67258f2ad13dc51f/phonemizer-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# libespeak-ng is loaded with ctypes, so the ELF generator does not see it.
Requires:	espeak-ng

%description
phonemizer converts text to phonemes. Kokoro uses the espeak-ng backend
and the system libespeak-ng. The optional segments backend is not required.

# Upstream's package finder also picks up the test suite and Sphinx config.
%prep -a
rm -rf test docs

%files
%doc README.md
%license LICENSE
%{_bindir}/phonemize
%{py_sitedir}/phonemizer
%{py_sitedir}/phonemizer-*.dist-info
