#!/bin/bash
rm -rf swipl-devel
git clone https://github.com/rmanhaeve/swipl-devel.git
cd swipl-devel
git submodule update --init
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=../bundled_swipl -DSWIPL_PACKAGE_LIST="clib;plunit;sgml;semweb;chr;clpqr;nlp;yaml" -DINSTALL_DOCUMENTATION=OFF -DUSE_GM=OFF ..
make
ctest -j $(nproc) --output-on-failure
make install
