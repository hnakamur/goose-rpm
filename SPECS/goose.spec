%define debug_package %{nil}

%global commit             479f9453e648d9401db0ad6e04aad62a9bd22eaa
%global middlecommit       %(c=%{commit}; echo ${c:0:12})
%global shortcommit        %(c=%{commit}; echo ${c:0:7})

Name:	        goose
Version:	0
Release:	0.1.git%{shortcommit}%{?dist}
Summary:	Go dependency tool

Group:		Development/Tools
License:	MIT
URL:		https://bitbucket.org/hnakamur/goose

# This tarball was created with the following commands.
#
# mkdir -p goose/go/src/bitbucket.org/hnakamur/goose
# cd goose/go
# export GOPATH=$PWD
# cd src/bitbucket.org/hnakamur/goose
# curl -sS https://bitbucket.org/hnakamur/goose/get/479f9453e648d9401db0ad6e04aad62a9bd22eaa.tar.gz | tar zxf - --strip-component=1
# go get -u github.com/go-sql-driver/mysql/...
# go get -u github.com/kylelemons/go-gypsy/yaml/...
# go get -u github.com/lib/pq/...
# go get -u github.com/mattn/go-sqlite3/...
# go get -u github.com/ziutek/mymysql/godrv/...
# cd $GOPATH/../..
# rm -rf goose/go/pkg goose/go/bin
# tar cf - goose | gzip -9 > goose.tar.gz
Source0:	goose.tar.gz

BuildRoot:      %{name}
BuildRequires:  golang >= 1.8

%description
goose is a database migration tool.
You can manage your database's evolution by creating incremental SQL or Go scripts.

This is a fork of https://bitbucket.org/liamstask/goose

%prep
%setup -c -n %{name}

%build
export GOPATH=%{_builddir}/%{name}/%{name}/go
cd "$GOPATH/src/bitbucket.org/hnakamur/goose"
go install ./... || :

%install
%{__rm} -rf %{buildroot}
%{__install} -pD -m 755 "%{_builddir}/%{name}/%{name}/go/bin/goose" %{buildroot}%{_bindir}/goose

%files
%defattr(0755,root,root,-)
%{_bindir}/goose

%changelog
* Thu May 11 2017 <hnakamur@gmail.com> - 0-0.1.git479f94.el7.centos
- Initial release
