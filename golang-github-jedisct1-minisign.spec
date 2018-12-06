# Run tests in check section
%bcond_without check

%global goipath         github.com/jedisct1/go-minisign
%global commit          f4dbde220b4f73d450949b9ba27fa941faa05a78

%global common_description %{expand:
A Golang library to verify Minisign signatures.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Minisign library for Golang
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitf4dbde2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180529gitf4dbde2
- First package for Fedora

