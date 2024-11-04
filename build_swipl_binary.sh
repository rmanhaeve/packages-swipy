#!/bin/bash
git clone https://github.com/SWI-Prolog/swipl-devel.git
cd swipl-devel
git submodule update --init
cd swipl-devel
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=../bundled_swipl -DSWIPL_PACKAGE_LIST="clib;plunit;sgml;semweb;chr;clpqr;nlp;yaml;swipy" -DINSTALL_DOCUMENTATION=OFF -DUSE_GM=OFF ..
make
ctest -j $(nproc) --output-on-failure
