%global pypi_name nnpy

%global common_description %{expand:
cffi-based Python bindings for nanomsg}

%{?python_enable_dependency_generator}

Name:           python-%{pypi_name}
Summary:        cffi-based Python bindings for nanomsg
Version:        1.4.2
Release:        1%{?dist}
License:        MIT

URL:            https://github.com/nanomsg/nnpy
Source0:        %{pypi_source %{pypi_name} %{version}}

BuildRequires:  gcc
BuildRequires:  nanomsg-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)

# test requirements
BuildRequires:  python3-cffi

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info/
%{python3_sitearch}/*.so


%changelog
* Mon Feb 18 2019 Troy Dawson <tdawson@redhat.com> - 1.4.2-1
- Initial package
