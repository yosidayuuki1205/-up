# Copyright 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'variables': {
    'opencv_root': '<(DEPTH)/third_party/opencv',
    'opencv_src': '<(opencv_root)/src',
    'opencv_gen': '<(DEPTH)/third_party/opencv/gen/arch/<(OS)/<(target_arch)',
    'opencv_system_include%': '/usr/include/opencv',
    'use_system_opencv%': 0,
  },
  'conditions': [
    ['use_system_opencv==0', {
      'targets': [
        {
          'target_name': 'flann',
          'type': '<(library)',
          'sources': [
            'src/opencv/3rdparty/flann/algorithms/dist.cpp',
            'src/opencv/3rdparty/flann/flann.cpp',
            'src/opencv/3rdparty/flann/nn/index_testing.cpp',
            'src/opencv/3rdparty/flann/util/logger.cpp',
            'src/opencv/3rdparty/flann/util/random.cpp',
            'src/opencv/3rdparty/flann/util/saving.cpp',
          ],
          'include_dirs': [
            '<(opencv_src)/opencv/3rdparty/flann/algorithms',
            '<(opencv_src)/opencv/3rdparty/flann/nn',
            '<(opencv_src)/opencv/3rdparty/flann/util',
            '<(opencv_src)/opencv/3rdparty/include',
            '<(opencv_src)/opencv/3rdparty/include/flann',
          ],
        },
        {
          'target_name': 'lapack',
          'type': '<(library)',
          'sources': [
            'src/opencv/3rdparty/lapack/dsyevr.c',
            'src/opencv/3rdparty/lapack/slalsa.c',
            'src/opencv/3rdparty/lapack/sorml2.c',
            'src/opencv/3rdparty/lapack/scopy.c',
            'src/opencv/3rdparty/lapack/slassq.c',
            'src/opencv/3rdparty/lapack/dlarre.c',
            'src/opencv/3rdparty/lapack/dlasq2.c',
            'src/opencv/3rdparty/lapack/slarfg.c',
            'src/opencv/3rdparty/lapack/slaeda.c',
            'src/opencv/3rdparty/lapack/ddot.c',
            'src/opencv/3rdparty/lapack/dgetri.c',
            'src/opencv/3rdparty/lapack/slarft.c',
            'src/opencv/3rdparty/lapack/sgemm.c',
            'src/opencv/3rdparty/lapack/slarre.c',
            'src/opencv/3rdparty/lapack/slasq5.c',
            'src/opencv/3rdparty/lapack/strtrs.c',
            'src/opencv/3rdparty/lapack/dgetrf.c',
            'src/opencv/3rdparty/lapack/spotrf.c',
            'src/opencv/3rdparty/lapack/slapy2.c',
            'src/opencv/3rdparty/lapack/sormlq.c',
            'src/opencv/3rdparty/lapack/dsytri.c',
            'src/opencv/3rdparty/lapack/slaed1.c',
            'src/opencv/3rdparty/lapack/slaed5.c',
            'src/opencv/3rdparty/lapack/dlasda.c',
            'src/opencv/3rdparty/lapack/sgemv.c',
            'src/opencv/3rdparty/lapack/strti2.c',
            'src/opencv/3rdparty/lapack/dsyrk.c',
            'src/opencv/3rdparty/lapack/dlarrk.c',
            'src/opencv/3rdparty/lapack/sormbr.c',
            'src/opencv/3rdparty/lapack/sbdsdc.c',
            'src/opencv/3rdparty/lapack/dlascl.c',
            'src/opencv/3rdparty/lapack/slanst.c',
            'src/opencv/3rdparty/lapack/dlanst.c',
            'src/opencv/3rdparty/lapack/dorml2.c',
            'src/opencv/3rdparty/lapack/slaset.c',
            'src/opencv/3rdparty/lapack/dorm2r.c',
            'src/opencv/3rdparty/lapack/dorgbr.c',
            'src/opencv/3rdparty/lapack/dstemr.c',
            'src/opencv/3rdparty/lapack/dlasdq.c',
            'src/opencv/3rdparty/lapack/dlansy.c',
            'src/opencv/3rdparty/lapack/dlalsd.c',
            'src/opencv/3rdparty/lapack/sdot.c',
            'src/opencv/3rdparty/lapack/dsytf2.c',
            'src/opencv/3rdparty/lapack/slabrd.c',
            'src/opencv/3rdparty/lapack/dormql.c',
            'src/opencv/3rdparty/lapack/ilaenv.c',
            'src/opencv/3rdparty/lapack/dlaed9.c',
            'src/opencv/3rdparty/lapack/sormqr.c',
            'src/opencv/3rdparty/lapack/dlange.c',
            'src/opencv/3rdparty/lapack/dlabrd.c',
            'src/opencv/3rdparty/lapack/dlasd6.c',
            'src/opencv/3rdparty/lapack/dpotrs.c',
            'src/opencv/3rdparty/lapack/dlazq3.c',
            'src/opencv/3rdparty/lapack/idamax.c',
            'src/opencv/3rdparty/lapack/dsterf.c',
            'src/opencv/3rdparty/lapack/slasd7.c',
            'src/opencv/3rdparty/lapack/dlacpy.c',
            'src/opencv/3rdparty/lapack/dlasd8.c',
            'src/opencv/3rdparty/lapack/ssyr2k.c',
            'src/opencv/3rdparty/lapack/slasda.c',
            'src/opencv/3rdparty/lapack/dormtr.c',
            'src/opencv/3rdparty/lapack/slalsd.c',
            'src/opencv/3rdparty/lapack/dlarrj.c',
            'src/opencv/3rdparty/lapack/dlarra.c',
            'src/opencv/3rdparty/lapack/dlar1v.c',
            'src/opencv/3rdparty/lapack/dtrtrs.c',
            'src/opencv/3rdparty/lapack/slasd5.c',
            'src/opencv/3rdparty/lapack/slaruv.c',
            'src/opencv/3rdparty/lapack/dlamrg.c',
            'src/opencv/3rdparty/lapack/slaebz.c',
            'src/opencv/3rdparty/lapack/dgetf2.c',
            'src/opencv/3rdparty/lapack/sgelqf.c',
            'src/opencv/3rdparty/lapack/sgebrd.c',
            'src/opencv/3rdparty/lapack/slartg.c',
            'src/opencv/3rdparty/lapack/sorglq.c',
            'src/opencv/3rdparty/lapack/dormlq.c',
            'src/opencv/3rdparty/lapack/slaed2.c',
            'src/opencv/3rdparty/lapack/ssytrd.c',
            'src/opencv/3rdparty/lapack/dlaed5.c',
            'src/opencv/3rdparty/lapack/dlagts.c',
            'src/opencv/3rdparty/lapack/slarrf.c',
            'src/opencv/3rdparty/lapack/sorm2l.c',
            'src/opencv/3rdparty/lapack/sorgqr.c',
            'src/opencv/3rdparty/lapack/dlasq3.c',
            'src/opencv/3rdparty/lapack/slaed6.c',
            'src/opencv/3rdparty/lapack/dgesv.c',
            'src/opencv/3rdparty/lapack/dlasr.c',
            'src/opencv/3rdparty/lapack/s_cat.c',
            'src/opencv/3rdparty/lapack/dlasq5.c',
            'src/opencv/3rdparty/lapack/dbdsqr.c',
            'src/opencv/3rdparty/lapack/slae2.c',
            'src/opencv/3rdparty/lapack/srot.c',
            'src/opencv/3rdparty/lapack/sormql.c',
            'src/opencv/3rdparty/lapack/dlasq4.c',
            'src/opencv/3rdparty/lapack/sgeqrf.c',
            'src/opencv/3rdparty/lapack/sormtr.c',
            'src/opencv/3rdparty/lapack/slarrb.c',
            'src/opencv/3rdparty/lapack/slarrd.c',
            'src/opencv/3rdparty/lapack/sgetri.c',
            'src/opencv/3rdparty/lapack/dlartg.c',
            'src/opencv/3rdparty/lapack/dpotf2.c',
            'src/opencv/3rdparty/lapack/sorg2r.c',
            'src/opencv/3rdparty/lapack/dsytrd.c',
            'src/opencv/3rdparty/lapack/dgels.c',
            'src/opencv/3rdparty/lapack/slasd4.c',
            'src/opencv/3rdparty/lapack/slatrd.c',
            'src/opencv/3rdparty/lapack/ieeeck.c',
            'src/opencv/3rdparty/lapack/slasq4.c',
            'src/opencv/3rdparty/lapack/slarrv.c',
            'src/opencv/3rdparty/lapack/dtrmv.c',
            'src/opencv/3rdparty/lapack/dlaed1.c',
            'src/opencv/3rdparty/lapack/s_cmp.c',
            'src/opencv/3rdparty/lapack/ssterf.c',
            'src/opencv/3rdparty/lapack/dgelq2.c',
            'src/opencv/3rdparty/lapack/dlarrd.c',
            'src/opencv/3rdparty/lapack/ssyrk.c',
            'src/opencv/3rdparty/lapack/slamrg.c',
            'src/opencv/3rdparty/lapack/dlasrt.c',
            'src/opencv/3rdparty/lapack/slaed7.c',
            'src/opencv/3rdparty/lapack/dlarrv.c',
            'src/opencv/3rdparty/lapack/dlae2.c',
            'src/opencv/3rdparty/lapack/sgelsd.c',
            'src/opencv/3rdparty/lapack/dscal.c',
            'src/opencv/3rdparty/lapack/dlabad.c',
            'src/opencv/3rdparty/lapack/slaisnan.c',
            'src/opencv/3rdparty/lapack/dsytd2.c',
            'src/opencv/3rdparty/lapack/dlaed2.c',
            'src/opencv/3rdparty/lapack/slarnv.c',
            'src/opencv/3rdparty/lapack/dlaneg.c',
            'src/opencv/3rdparty/lapack/dorm2l.c',
            'src/opencv/3rdparty/lapack/f77_aloc.c',
            'src/opencv/3rdparty/lapack/strmm.c',
            'src/opencv/3rdparty/lapack/dlaisnan.c',
            'src/opencv/3rdparty/lapack/slals0.c',
            'src/opencv/3rdparty/lapack/dger.c',
            'src/opencv/3rdparty/lapack/slar1v.c',
            'src/opencv/3rdparty/lapack/slaed0.c',
            'src/opencv/3rdparty/lapack/dlaeda.c',
            'src/opencv/3rdparty/lapack/sger.c',
            'src/opencv/3rdparty/lapack/dcopy.c',
            'src/opencv/3rdparty/lapack/dlazq4.c',
            'src/opencv/3rdparty/lapack/daxpy.c',
            'src/opencv/3rdparty/lapack/ssyevr.c',
            'src/opencv/3rdparty/lapack/sgels.c',
            'src/opencv/3rdparty/lapack/dorglq.c',
            'src/opencv/3rdparty/lapack/dgelqf.c',
            'src/opencv/3rdparty/lapack/slarrc.c',
            'src/opencv/3rdparty/lapack/dlaebz.c',
            'src/opencv/3rdparty/lapack/sgetrs.c',
            'src/opencv/3rdparty/lapack/slasr.c',
            'src/opencv/3rdparty/lapack/dsteqr.c',
            'src/opencv/3rdparty/lapack/dtrtri.c',
            'src/opencv/3rdparty/lapack/dtrmm.c',
            'src/opencv/3rdparty/lapack/dstein.c',
            'src/opencv/3rdparty/lapack/dlaruv.c',
            'src/opencv/3rdparty/lapack/slaneg.c',
            'src/opencv/3rdparty/lapack/slarfb.c',
            'src/opencv/3rdparty/lapack/dorgqr.c',
            'src/opencv/3rdparty/lapack/dlasd3.c',
            'src/opencv/3rdparty/lapack/dlarnv.c',
            'src/opencv/3rdparty/lapack/precomp.c',
            'src/opencv/3rdparty/lapack/dsytrs.c',
            'src/opencv/3rdparty/lapack/dlarfg.c',
            'src/opencv/3rdparty/lapack/slaed9.c',
            'src/opencv/3rdparty/lapack/dgemm.c',
            'src/opencv/3rdparty/lapack/dgebrd.c',
            'src/opencv/3rdparty/lapack/slas2.c',
            'src/opencv/3rdparty/lapack/dlasq1.c',
            'src/opencv/3rdparty/lapack/dlarrr.c',
            'src/opencv/3rdparty/lapack/dpotri.c',
            'src/opencv/3rdparty/lapack/slasrt.c',
            'src/opencv/3rdparty/lapack/slagts.c',
            'src/opencv/3rdparty/lapack/dlasd4.c',
            'src/opencv/3rdparty/lapack/sbdsqr.c',
            'src/opencv/3rdparty/lapack/slarrk.c',
            'src/opencv/3rdparty/lapack/slaed8.c',
            'src/opencv/3rdparty/lapack/sstebz.c',
            'src/opencv/3rdparty/lapack/dlarrb.c',
            'src/opencv/3rdparty/lapack/saxpy.c',
            'src/opencv/3rdparty/lapack/dlauu2.c',
            'src/opencv/3rdparty/lapack/dasum.c',
            'src/opencv/3rdparty/lapack/pow_ri.c',
            'src/opencv/3rdparty/lapack/slange.c',
            'src/opencv/3rdparty/lapack/dpotrf.c',
            'src/opencv/3rdparty/lapack/dbdsdc.c',
            'src/opencv/3rdparty/lapack/sgesv.c',
            'src/opencv/3rdparty/lapack/drot.c',
            'src/opencv/3rdparty/lapack/sorgbr.c',
            'src/opencv/3rdparty/lapack/spotf2.c',
            'src/opencv/3rdparty/lapack/ssteqr.c',
            'src/opencv/3rdparty/lapack/dstebz.c',
            'src/opencv/3rdparty/lapack/dsyr2.c',
            'src/opencv/3rdparty/lapack/dlalsa.c',
            'src/opencv/3rdparty/lapack/sgebd2.c',
            'src/opencv/3rdparty/lapack/dgeqr2.c',
            'src/opencv/3rdparty/lapack/ssymv.c',
            'src/opencv/3rdparty/lapack/dlasdt.c',
            'src/opencv/3rdparty/lapack/dtrti2.c',
            'src/opencv/3rdparty/lapack/slasdt.c',
            'src/opencv/3rdparty/lapack/sorgl2.c',
            'src/opencv/3rdparty/lapack/slazq4.c',
            'src/opencv/3rdparty/lapack/dtrsm.c',
            'src/opencv/3rdparty/lapack/slascl.c',
            'src/opencv/3rdparty/lapack/iparmq.c',
            'src/opencv/3rdparty/lapack/sswap.c',
            'src/opencv/3rdparty/lapack/dlarrc.c',
            'src/opencv/3rdparty/lapack/dlassq.c',
            'src/opencv/3rdparty/lapack/dlasd5.c',
            'src/opencv/3rdparty/lapack/dlaswp.c',
            'src/opencv/3rdparty/lapack/slagtf.c',
            'src/opencv/3rdparty/lapack/dormbr.c',
            'src/opencv/3rdparty/lapack/dgesdd.c',
            'src/opencv/3rdparty/lapack/dlaed8.c',
            'src/opencv/3rdparty/lapack/dswap.c',
            'src/opencv/3rdparty/lapack/dlaed7.c',
            'src/opencv/3rdparty/lapack/sgesdd.c',
            'src/opencv/3rdparty/lapack/slasdq.c',
            'src/opencv/3rdparty/lapack/slaed3.c',
            'src/opencv/3rdparty/lapack/dlapy2.c',
            'src/opencv/3rdparty/lapack/dlaed4.c',
            'src/opencv/3rdparty/lapack/dsytrf.c',
            'src/opencv/3rdparty/lapack/dgeqrf.c',
            'src/opencv/3rdparty/lapack/slasd0.c',
            'src/opencv/3rdparty/lapack/slasd3.c',
            'src/opencv/3rdparty/lapack/dgemv.c',
            'src/opencv/3rdparty/lapack/slasd6.c',
            'src/opencv/3rdparty/lapack/dlamch.c',
            'src/opencv/3rdparty/lapack/dlasd0.c',
            'src/opencv/3rdparty/lapack/s_copy.c',
            'src/opencv/3rdparty/lapack/snrm2.c',
            'src/opencv/3rdparty/lapack/dsymv.c',
            'src/opencv/3rdparty/lapack/dgelsd.c',
            'src/opencv/3rdparty/lapack/dlarf.c',
            'src/opencv/3rdparty/lapack/strsm.c',
            'src/opencv/3rdparty/lapack/xerbla.c',
            'src/opencv/3rdparty/lapack/slasq1.c',
            'src/opencv/3rdparty/lapack/dlasd1.c',
            'src/opencv/3rdparty/lapack/slazq3.c',
            'src/opencv/3rdparty/lapack/spotri.c',
            'src/opencv/3rdparty/lapack/dlarfb.c',
            'src/opencv/3rdparty/lapack/sstein.c',
            'src/opencv/3rdparty/lapack/strmv.c',
            'src/opencv/3rdparty/lapack/pow_ii.c',
            'src/opencv/3rdparty/lapack/slarrr.c',
            'src/opencv/3rdparty/lapack/slauum.c',
            'src/opencv/3rdparty/lapack/dlals0.c',
            'src/opencv/3rdparty/lapack/slasq2.c',
            'src/opencv/3rdparty/lapack/dgetrs.c',
            'src/opencv/3rdparty/lapack/dlatrd.c',
            'src/opencv/3rdparty/lapack/slauu2.c',
            'src/opencv/3rdparty/lapack/slaev2.c',
            'src/opencv/3rdparty/lapack/slacpy.c',
            'src/opencv/3rdparty/lapack/dlaed0.c',
            'src/opencv/3rdparty/lapack/slasq6.c',
            'src/opencv/3rdparty/lapack/dlasd2.c',
            'src/opencv/3rdparty/lapack/slarrj.c',
            'src/opencv/3rdparty/lapack/sasum.c',
            'src/opencv/3rdparty/lapack/dsyr.c',
            'src/opencv/3rdparty/lapack/slasd2.c',
            'src/opencv/3rdparty/lapack/dlaed3.c',
            'src/opencv/3rdparty/lapack/slasd8.c',
            'src/opencv/3rdparty/lapack/sstemr.c',
            'src/opencv/3rdparty/lapack/slabad.c',
            'src/opencv/3rdparty/lapack/slansy.c',
            'src/opencv/3rdparty/lapack/spotrs.c',
            'src/opencv/3rdparty/lapack/dnrm2.c',
            'src/opencv/3rdparty/lapack/sgeqr2.c',
            'src/opencv/3rdparty/lapack/slamch.c',
            'src/opencv/3rdparty/lapack/sgetf2.c',
            'src/opencv/3rdparty/lapack/dlaev2.c',
            'src/opencv/3rdparty/lapack/pow_di.c',
            'src/opencv/3rdparty/lapack/slarf.c',
            'src/opencv/3rdparty/lapack/dlagtf.c',
            'src/opencv/3rdparty/lapack/slarra.c',
            'src/opencv/3rdparty/lapack/dlaed6.c',
            'src/opencv/3rdparty/lapack/dlarrf.c',
            'src/opencv/3rdparty/lapack/ssytd2.c',
            'src/opencv/3rdparty/lapack/slasv2.c',
            'src/opencv/3rdparty/lapack/dsyr2k.c',
            'src/opencv/3rdparty/lapack/ssyr2.c',
            'src/opencv/3rdparty/lapack/slaswp.c',
            'src/opencv/3rdparty/lapack/dormqr.c',
            'src/opencv/3rdparty/lapack/isamax.c',
            'src/opencv/3rdparty/lapack/dlasq6.c',
            'src/opencv/3rdparty/lapack/strtri.c',
            'src/opencv/3rdparty/lapack/slasq3.c',
            'src/opencv/3rdparty/lapack/dorg2r.c',
            'src/opencv/3rdparty/lapack/dlarft.c',
            'src/opencv/3rdparty/lapack/dlauum.c',
            'src/opencv/3rdparty/lapack/sgetrf.c',
            'src/opencv/3rdparty/lapack/dlaset.c',
            'src/opencv/3rdparty/lapack/dlas2.c',
            'src/opencv/3rdparty/lapack/dlasv2.c',
            'src/opencv/3rdparty/lapack/sgelq2.c',
            'src/opencv/3rdparty/lapack/dlasd7.c',
            'src/opencv/3rdparty/lapack/sscal.c',
            'src/opencv/3rdparty/lapack/dgebd2.c',
            'src/opencv/3rdparty/lapack/slaed4.c',
            'src/opencv/3rdparty/lapack/slasd1.c',
            'src/opencv/3rdparty/lapack/sorm2r.c',
            'src/opencv/3rdparty/lapack/dorgl2.c',
            'src/opencv/3rdparty/lapack/dlasyf.c',
          ],
          'include_dirs': [
            '<(opencv_src)/opencv/3rdparty/include',
          ],
        },
        {
          'target_name': 'cxcore',
          'type': '<(library)',
          'dependencies': [
            'flann',
            'lapack',
            '<(DEPTH)/third_party/zlib/zlib.gyp:zlib',
          ],
          'sources': [
            'src/opencv/src/cxcore/cxalloc.cpp',
            'src/opencv/src/cxcore/cxarithm.cpp',
            'src/opencv/src/cxcore/cxarray.cpp',
            'src/opencv/src/cxcore/cxconvert.cpp',
            'src/opencv/src/cxcore/cxcopy.cpp',
            'src/opencv/src/cxcore/_cxcore.h',
            'src/opencv/src/cxcore/cxdatastructs.cpp',
            'src/opencv/src/cxcore/cxdrawing.cpp',
            'src/opencv/src/cxcore/cxdxt.cpp',
            'src/opencv/src/cxcore/cxflann.cpp',
            'src/opencv/src/cxcore/cxlapack.cpp',
            'src/opencv/src/cxcore/cxmathfuncs.cpp',
            'src/opencv/src/cxcore/cxmatmul.cpp',
            'src/opencv/src/cxcore/cxmatrix.cpp',
            'src/opencv/src/cxcore/cxstat.cpp',
            'src/opencv/src/cxcore/cxpersistence.cpp',
            'src/opencv/src/cxcore/cxprecomp.cpp',
            'src/opencv/src/cxcore/cxrand.cpp',
            'src/opencv/src/cxcore/cxsystem.cpp',
            'src/opencv/src/cxcore/cxtables.cpp',
          ],
         'include_dirs': [
            # opencv provides its own copy of zlib.h, but we want to use
            # our version in third_party/zlib, so third_party/zlib must
            # appear early in the list of include dirs.
            '<(DEPTH)/third_party/zlib',
            '<(opencv_src)/opencv/include/opencv',
            '<(opencv_src)/opencv/3rdparty/include',
          ],
        },
        {
          'target_name': 'cv',
          'type': '<(library)',
          'dependencies': [
            'cxcore',
          ],
          'sources': [
            'src/opencv/src/cv/cvaccum.cpp',
            'src/opencv/src/cv/cvapprox.cpp',
            'src/opencv/src/cv/cvcalibinit.cpp',
            'src/opencv/src/cv/cvcalibration.cpp',
            'src/opencv/src/cv/cvcamshift.cpp',
            'src/opencv/src/cv/cvcanny.cpp',
            'src/opencv/src/cv/cvcascadedetect.cpp',
            'src/opencv/src/cv/cvcheckchessboard.cpp',
            'src/opencv/src/cv/cvcolor.cpp',
            'src/opencv/src/cv/cvcontours.cpp',
            'src/opencv/src/cv/cvcontourtree.cpp',
            'src/opencv/src/cv/cvconvhull.cpp',
            'src/opencv/src/cv/cvcorner.cpp',
            'src/opencv/src/cv/cvcornersubpix.cpp',
            'src/opencv/src/cv/cvderiv.cpp',
            'src/opencv/src/cv/cvdistransform.cpp',
            'src/opencv/src/cv/cvemd.cpp',
            'src/opencv/src/cv/cvfeatureselect.cpp',
            'src/opencv/src/cv/cvfloodfill.cpp',
            'src/opencv/src/cv/cvfundam.cpp',
            'src/opencv/src/cv/cvgeometry.cpp',
            'src/opencv/src/cv/cvhaar.cpp',
            'src/opencv/src/cv/cvhistogram.cpp',
            'src/opencv/src/cv/cvhough.cpp',
            'src/opencv/src/cv/cvimgwarp.cpp',
            'src/opencv/src/cv/cvkalman.cpp',
            'src/opencv/src/cv/cvlinefit.cpp',
            'src/opencv/src/cv/cvlkpyramid.cpp',
            'src/opencv/src/cv/cvmatchcontours.cpp',
            'src/opencv/src/cv/cvmodelest.cpp',
            'src/opencv/src/cv/cvmoments.cpp',
            'src/opencv/src/cv/cvmorph.cpp',
            'src/opencv/src/cv/cvmotempl.cpp',
            'src/opencv/src/cv/cvoptflowbm.cpp',
            'src/opencv/src/cv/cvoptflowhs.cpp',
            'src/opencv/src/cv/cvoptflowlk.cpp',
            'src/opencv/src/cv/cvposit.cpp',
            'src/opencv/src/cv/cvprecomp.cpp',
            'src/opencv/src/cv/cvpyramids.cpp',
            'src/opencv/src/cv/cvpyrsegmentation.cpp',
            'src/opencv/src/cv/cvrotcalipers.cpp',
            'src/opencv/src/cv/cvsamplers.cpp',
            'src/opencv/src/cv/cvshapedescr.cpp',
            'src/opencv/src/cv/cvsmooth.cpp',
            'src/opencv/src/cv/cvsnakes.cpp',
            'src/opencv/src/cv/cvsubdivision2d.cpp',
            'src/opencv/src/cv/cvsumpixels.cpp',
            'src/opencv/src/cv/cvtables.cpp',
            'src/opencv/src/cv/cvtemplmatch.cpp',
            'src/opencv/src/cv/cvthresh.cpp',
            'src/opencv/src/cv/cvundistort.cpp',
            'src/opencv/src/cv/cvutils.cpp',
            'src/opencv/src/cv/cvfilter.cpp',
            'src/opencv/src/cv/cvinpaint.cpp',
            'src/opencv/src/cv/cvsegmentation.cpp',
          ],
          'include_dirs': [
            '<(opencv_src)/opencv/include/opencv',
          ],
        },
        {
          'target_name': 'highgui',
          'type': '<(library)',
          'dependencies': [
            'cv',
            '<(DEPTH)/third_party/zlib/zlib.gyp:zlib',
            '<(DEPTH)/third_party/libjpeg/libjpeg.gyp:libjpeg',
            '<(DEPTH)/third_party/libpng/libpng.gyp:libpng',
          ],
          'sources': [
            'src/opencv/src/highgui/bitstrm.cpp',
            'src/opencv/src/highgui/cvcap.cpp',
            'src/opencv/src/highgui/cvcap_images.cpp',
            'src/opencv/src/highgui/grfmt_base.cpp',
            'src/opencv/src/highgui/grfmt_bmp.cpp',
            'src/opencv/src/highgui/grfmt_jpeg.cpp',
            'src/opencv/src/highgui/grfmt_png.cpp',
            'src/opencv/src/highgui/grfmt_pxm.cpp',
            'src/opencv/src/highgui/grfmt_sunras.cpp',
            'src/opencv/src/highgui/grfmt_tiff.cpp',
            'src/opencv/src/highgui/image.cpp',
            'src/opencv/src/highgui/loadsave.cpp',
            'src/opencv/src/highgui/precomp.cpp',
            'src/opencv/src/highgui/utils.cpp',
            'src/opencv/src/highgui/window.cpp',
          ],
          'include_dirs': [
            '<(opencv_gen)/include',
            '<(opencv_src)/opencv/include/opencv',
          ],
        },
      ],
    },
    { # use_system_opencv
      'targets': [
        {
          'target_name': 'highgui',
          'type': 'settings',
          'include_dirs': [
            '<(opencv_system_include)',
          ],
          'direct_dependent_settings': {
            'defines': [
              'USE_SYSTEM_OPENCV',
            ],
            'include_dirs': [
              '<(opencv_system_include)',
            ],
          },
          'defines': [
            'USE_SYSTEM_OPENCV',
          ],
          'link_settings': {
            'libraries': [
              '-lcv',
              '-lcxcore',
              '-lhighgui',
            ],
          },
        },
      ],
    }],
  ],
}
