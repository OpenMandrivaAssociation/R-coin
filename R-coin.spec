%bcond_without bootstrap
%global packname  coin
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0_20
Release:          1
Summary:          Conditional Inference Procedures in a Permutation Test Framework
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-20.tar.gz
Requires:         R-methods R-survival R-mvtnorm R-modeltools 
%if %{with bootstrap}
Requires:         R-xtable R-e1071 R-vcd 
%else
Requires:         R-multcomp R-xtable R-e1071 R-vcd 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-survival R-mvtnorm R-modeltools
%if %{with bootstrap}
BuildRequires:    R-xtable R-e1071 R-vcd 
%else
BuildRequires:    R-multcomp R-xtable R-e1071 R-vcd 
%endif

%description
Conditional inference procedures for the general independence problem
including two-sample, K-sample (non-parametric ANOVA), correlation,
censored, ordered and multivariate problems.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/documentation
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
