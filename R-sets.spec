#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sets
Version  : 1.0.22
Release  : 27
URL      : https://cran.r-project.org/src/contrib/sets_1.0-22.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sets_1.0-22.tar.gz
Summary  : Sets, Generalized Sets, Customizable Sets and Intervals
Group    : Development/Tools
License  : GPL-2.0
Requires: R-sets-lib = %{version}-%{release}
BuildRequires : R-proxy
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
generalizations such as fuzzy sets, multisets, and
             fuzzy multisets, customizable sets, and intervals.

%package lib
Summary: lib components for the R-sets package.
Group: Libraries

%description lib
lib components for the R-sets package.


%prep
%setup -q -n sets
cd %{_builddir}/sets

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675271091

%install
export SOURCE_DATE_EPOCH=1675271091
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sets/CITATION
/usr/lib64/R/library/sets/DESCRIPTION
/usr/lib64/R/library/sets/INDEX
/usr/lib64/R/library/sets/Meta/Rd.rds
/usr/lib64/R/library/sets/Meta/data.rds
/usr/lib64/R/library/sets/Meta/features.rds
/usr/lib64/R/library/sets/Meta/hsearch.rds
/usr/lib64/R/library/sets/Meta/links.rds
/usr/lib64/R/library/sets/Meta/nsInfo.rds
/usr/lib64/R/library/sets/Meta/package.rds
/usr/lib64/R/library/sets/Meta/vignette.rds
/usr/lib64/R/library/sets/NAMESPACE
/usr/lib64/R/library/sets/NEWS.Rd
/usr/lib64/R/library/sets/R/sets
/usr/lib64/R/library/sets/R/sets.rdb
/usr/lib64/R/library/sets/R/sets.rdx
/usr/lib64/R/library/sets/data/fuzzy_docs.rda
/usr/lib64/R/library/sets/doc/index.html
/usr/lib64/R/library/sets/doc/sets.R
/usr/lib64/R/library/sets/doc/sets.Rnw
/usr/lib64/R/library/sets/doc/sets.pdf
/usr/lib64/R/library/sets/help/AnIndex
/usr/lib64/R/library/sets/help/aliases.rds
/usr/lib64/R/library/sets/help/paths.rds
/usr/lib64/R/library/sets/help/sets.rdb
/usr/lib64/R/library/sets/help/sets.rdx
/usr/lib64/R/library/sets/html/00Index.html
/usr/lib64/R/library/sets/html/R.css
/usr/lib64/R/library/sets/po/en@quot/LC_MESSAGES/R-sets.mo

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sets/libs/sets.so
/usr/lib64/R/library/sets/libs/sets.so.avx2
/usr/lib64/R/library/sets/libs/sets.so.avx512
