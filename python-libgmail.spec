%define 	module	libgmail

Summary:	libgmail - Python binding for Google's Gmail service
Summary(pl.UTF-8):   libgmail - wiązania Pythona do usługi Google Gmail
Name:		python-%{module}
Version:	0.1.5.1
Release:	1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	97b6fdd56b715068fddc38edb21b91cf
URL:		http://libgmail.sourceforge.net/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgmail project is a pure Python binding to provide access to
Google's Gmail web-mail service.

%description -l pl.UTF-8
Projekt libgmail umożliwia uzyskanie dostępu do usługi Google Gmail w
programach pisanych w Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
%{py_comp} .
%{py_ocomp} .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

install libgmail.py[co] $RPM_BUILD_ROOT%{py_sitescriptdir}
install lgconstants.py[co] $RPM_BUILD_ROOT%{py_sitescriptdir}

#install demos/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{py_sitescriptdir}/*.py[co]
#%{_examplesdir}/%{name}-%{version}
