%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	A Wiki written in Ruby
Summary(pl):	Wiki napisane w Ruby
Name:		ruwiki
Version:	0.9.3
Release:	1
License:	Ruby License
Group:		Applications/WWW
Source0:	http://rubyforge.org/frs/download.php/2314/%{name}-%{version}.tar.gz
# Source0-md5:	f5538cc2a723438954b1466edd6dfbed
Source1:	setup.rb
# Source1-md5:	17e93fc639caf25d7d1abbb400335b1d
URL:		http://rubyforge.org/projects/ruwiki/
BuildRequires:	ruby
Requires:	ruby-Diff-LCS
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_cgibindir	/home/services/httpd/cgi-bin

%description
Ruwiki is a simple, extensible Wiki-clone written in Ruby, supporting
CGI and WEBrick interfaces, templates, CSS formatting, namespaces, and
internationalisation. A focus on antispam techniques has been applied.

%description -l pl
Ruwiki to prosty, rozszerzalny klon Wiki napisany w Ruby. Obs³uguje
skrypty CGI oraz interfejsy WEBrick, skórki, formatowanie przy u¿yciu
CSS a tak¿e internacjonalizacje. Posiada mechanizmy antyspamowe.

%prep
%setup -q

%build
install %{SOURCE1} .
mkdir share/ruwiki -p
mv data share/ruwiki/data
mv templates share/ruwiki/templates
mv share data
mkdir cgi-bin
mv bin/ruwiki.cgi cgi-bin
rm bin/ruwiki_service.rb
ruby setup.rb config \
        --rb-dir=%{ruby_rubylibdir} \
				--so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{_cgibindir}}
install cgi-bin/%{name}.cgi $RPM_BUILD_ROOT%{_cgibindir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

rdoc -o rdoc lib --inline-source

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_cgibindir}/*
%{ruby_rubylibdir}/*
%{_datadir}/%{name}
