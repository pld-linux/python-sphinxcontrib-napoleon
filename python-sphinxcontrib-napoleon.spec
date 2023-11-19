#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (not included in sdist)
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx "napoleon" extension
Summary(pl.UTF-8):	Rozszerzenie "napoleon" dla Sphinksa
Name:		python-sphinxcontrib-napoleon
Version:	0.7
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-napoleon/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-napoleon/sphinxcontrib-napoleon-%{version}.tar.gz
# Source0-md5:	080555f8bcdf5de9819798c24bdd02f8
URL:		https://pypi.org/project/sphinxcontrib-napoleon/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.2
BuildRequires:	python-docutils >= 0.10
BuildRequires:	python-mock >= 1.0.1
BuildRequires:	python-nose >= 1.3.0
BuildRequires:	python-pockets >= 0.3
BuildRequires:	python-six >= 1.5.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.2
BuildRequires:	python3-docutils >= 0.10
BuildRequires:	python3-nose >= 1.3.0
BuildRequires:	python3-pockets >= 0.3
BuildRequires:	python3-six >= 1.5.2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-pockets >= 0.3
BuildRequires:	python-six >= 1.5.2
BuildRequires:	sphinx-pdg-2 >= 1.3.1
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Napoleon - marching toward legible docstrings.

%description -l pl.UTF-8
Napoleon - wyjście naprzeciw czytelnym docstringom.

%package -n python3-sphinxcontrib-napoleon
Summary:	Sphinx "napoleon" extension
Summary(pl.UTF-8):	Rozszerzenie "napoleon" dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-sphinxcontrib-napoleon
Napoleon - marching toward legible docstrings.

%description -n python3-sphinxcontrib-napoleon -l pl.UTF-8
Napoleon - wyjście naprzeciw czytelnym docstringom.

%package apidocs
Summary:	API documentation for Python sphinxcontrib-napoleon module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinxcontrib-napoleon
Group:		Documentation

%description apidocs
API documentation for Python sphinxcontrib-napoleon module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinxcontrib-napoleon.

%prep
%setup -q -n sphinxcontrib-napoleon-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py_sitescriptdir}/sphinxcontrib/napoleon
%{py_sitescriptdir}/sphinxcontrib_napoleon-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_napoleon-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-napoleon
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/napoleon
%{py3_sitescriptdir}/sphinxcontrib_napoleon-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_napoleon-%{version}-py*-nspkg.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
