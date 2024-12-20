#!/bin/bash
git clone https://github.com/rmanhaeve/swipl-devel.git
cd swipl-devel
git submodule update --init
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=../../janus/bundled_swipl -DZLIB_USE_STATIC_LIBS=ON -DSWIPL_SO_VERSIONS=OFF -DSWIPL_PACKAGE_LIST="clib;plunit;sgml;semweb;chr;clpqr;nlp;yaml" -DINSTALL_DOCUMENTATION=OFF -DUSE_GM=OFF ..
make -j $(nproc) 
ctest -j $(nproc) --output-on-failure
make install
cd ../..
