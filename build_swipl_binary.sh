#!/bin/bash
git clone https://github.com/SWI-Prolog/swipl-devel.git
cd swipl-devel
git submodule update --init
cd swipl-devel
mkdir build
cd build
cmake -DSWIPL_PACKAGE_LIST="clib;plunit;sgml;semweb;chr;clpqr;nlp;yaml;swipy" -DUSE_GM=OFF ..
make
ctest -j $(nproc) --output-on-failure
