# Copyright (C) 2023 jbleyel
#
# DistroBuildInfo.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dogtag is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DistroBuildInfo.py.  If not, see <http://www.gnu.org/licenses/>.

# Changelog:
# 1.0 Initial version
# 1.1 add global blacklist / add filters

__version__ = "1.1"


import requests
import re

MACHINEARM = "dreamone dreamtwo og2s4k iziboxx4 ustym4ks2ottx novaler4kpro sx88v2 sfx6008 zgemmah82h gbquad4k gbue4k zgemmah7 pulse4kmini pulse4k sf8008 vusolo4k osmio4kplus beyonwizv2 mutant51 mutant66se gbtrio4kpro ip8 novaler4kse axmultiboxse anadolmultiboxse og2ott4k mutant66se sx988 ustym4kottpremium ferguson4k force4 protek4k dinobot4kmini axashis4kcombo axashis4kcomboplus dinobot4kplus zgemmah9s zgemmah9t zgemmah92s zgemmah92h ax51 anadol4k anadol4kv2 anadol4kcombo dinobot4k dinobot4kse e4hdultra lunix34k dm900 galaxy4k tmtwin4k vimastec1500 sf4008 bre2ze4k revo4k force3uhd force3uhdplus gi11000 beyonwizu4 dual pulse4k hitube4kpro dinobot4ktwin maxytecmultise iziboxelite4k vipersingle zgemmah9combose zgemmah92hse zgemmai55se anadolmultitwin axmulticombo axmultitwin protek4kx2 vipertwin vuuno4k vuultimo4k turing sf8008m osmini4k gbx34k viper4k51 ax61 gbip4k iziboxx3 arivatwin arivacombo dinobot4kelite jdhdduo zgemmah102s  zgemmah102h zgemmah10combo iziboxecohd iziboxone4k hitube4k viper4kv20 vuzero4k vuduo4kse dm920 vuuno4kse gbue4k zgemmah9twin axashistwin anadolprohd5 zgemmah9twinse spycatminiv2 anadolmulti maxytecmulti gbtrio4k axashisc4k viper4k protek4kx1 ustym4kpro iziboxone4kplus viper4kv40 axashistwinplus zgemmah9sse hitube4kplus viper4kv30 novaler4k zgemmah11s zgemmah112h osmio4k zgemmah9combo vuduo4k ax60 zgemmai55plus mutant60 lunix4k"
MACHINEMIPSEL = "dm800se dm500hd gb800solo zgemmah4 viperslim tiviaraplus zgemmah6 dm520 dm8000 dm7020hd dm7020hdv2 dm800sev2 dm500hdv2 dm7080 dm820 vipert2c vipercombo vipercombohdd evoslimse evoslimt2c  formuler1tc formuler3ip formuler4ip zgemmah2splus zgemmah52splus tiviarmin mbmicrov2 zgemmah52s zgemmah52tc zgemmah32tc vimastec1000 e4hdcombo formuler4turbo mutant530c sf238 9911lx twinboxlcdci5 novaip novacombo novatwin evominiplus mutant11 9910lx sf208 sf228 e4hdhybrid zgemmai55 zgemmah5 sf98 galaxym6 odinplus zgemmaslc 9900lx et7x00mini evomini zgemmahs zgemmah2s zgemmah2h e4hd t2cable xpeedlxcs2 xpeedlxcc mutant500c odin2hybrid mbmicro sf108 twinboxlcd singleboxlcd triplex quadbox2400 formuler1 vizyonvita mutant1100 mutant1200 mutant1265 mutant1500 mutant2400 formuler3 axase3c formuler4 axase3 evoe3hd geniuse3hd evo genius starsatlx axodinc axodin classm  maram9 et9x00 et6x00 et5x00 et4x00 et8500 et8000 et10000 et7x00 x1plus xcombo tyrant zgemmash1 zgemmash2 zgemmas2s zgemmass x2plus xp1000mk xp1000plus enibox xp1000max sf8 enfinity mago marvel1 bre2ze zgemmah3ac zgemmah5ac optimussos3plus osninopro lunix lunixco osnino osninoplus purehdse alphatriple evoslim tmnanom3 bre2zet2c force2nano gbultraueh gbx3h sf128 sf138 osmega spycatminiplus tmnanosem2plus force2plushv gbx2 osminiplus gbultraue gbquad gb800se gb800ue gb800seplus gb800ueplus gbipbox gbx1 gbx3 vuduo2 vusolose vusolo2 vuzero vuuno  vuduo vuultimo vusolo mbhybrid gbquadplus force2se mbtwinplus opticumtt beyonwizt2 osmini sf3038 spycat spycatmini bwidowx atemionemesis  beyonwizt4 sezammarvel xpeedlx3 mbultra sezam5000hd sezam1000hd  mbmini mbtwin beyonwizt3 xpeedlx1 xpeedlx2 mbminiplus atemio5x00 ventonhdx atemio6000 atemio6100  atemio6200 tmnanose tmnanosem2 tmnanosecombo optimussos force2 force2plus megaforce2 tmnano2super tm2t tmnano tmnano2t tmsingle tmtwin tmnano3t iqonios100hd iqonios200hd roxxs200hd mediaart200hd iqonios300hd force1 force1plus megaforce1plus optimussos1plus optimussos2plus optimussos1 optimussos2 mediabox iqonios300hdv2 worldvisionf1 worldvisionf1plus fusionhd fusionhdse purehd sogno8800hd uniboxhde 9920lx"

machines = set(MACHINEARM.split() + MACHINEMIPSEL.split())

filters = {
    "Open8eIGHT": r'(sx|sf|xp1000plus)',
    "OpenDROID": r'(zgemmah2h)',
    "TeamBlue": r'(gb)',
    "EGAMI": r'(zgemmah|novaler)'
}

BLACKLIST = ['dreamone', 'dreamtwo', 'zgemmah10combo', 'enfinity', 'marvel1', 'ch625dt', 'uniboxhde', 'protek4kx1', '7220s', 'starsatlx', 'ew7356', 'gb7356', 'xc7362', 'beyonwizt3', '7210s', 'mutant66se', 'evoslimse', 'x2plus', 'force2se', 'inihde2', 'anadolprohd5', 'force2plus', 'mago', 'zgemmah102s', 'anadolmultitwin', 'e3hd', '7400s', 'twinboxlcdci5', 'yh73625', 'mutant1265', 'tyrant', 'ch62lc', 'beyonwizt4', 'u56', 'zgemmah9combose', 'novaip', 'u571', 'odinm9', 'geniuse3hd', 'tm2t', 'axmultitwin', 'ew7362', 'gb7362', 'novaler4kpro', 'gi11000', 'vg1000', 'mediaart200hd', 'mbmini', 'iziboxx4', 'u57', 'novacombo', '7100s', 'force2', 'inihdp', 'yh625tc', 'xp1000max', 'sogno8800hd', 'viper4kv30', 'ew7358', 'dags7252', 'force2plushv', 'tmnano3t', 'turing', 'i55se', 'x1plus', 'yh7362', 'xpeedlx2', 'lunixco', 'g100', 'blackbox7405', 'zgemmah112h', 'genius', 'u42', 'iqonios300hd', 'revo4k', 'tmnano2super', 'ferguson4k', 'dags7356', 'galaxy4k', 'protek4k', 'mbminiplus', 'dagsmv200', 'alphatriple', 'maxytecmultise', 'purehd', 'ch625lc', 'u5pvr', 'iqonios300hdv2', 'dags73625', 'gb73625', 'sezam1000hd', 'vg5000', 'megaforce1plus', 'u55', 'sf238', 'gbmv200', 'dags72604', '7225s', 'axodinc', 'axashistwinplus', 'force4', 'evoe3hd', 'beyonwizu4', 'evomini', 'jj7362', 'iziboxone4kplus', 'zgemmah5ac', 'mediabox', 'fusionhdse', 'dags7362', 'u5', 'sezam5000hd', '7000s', 'yh625dt', 'force1plus', 'vizyonvita', 'sezammarvel', 'yh62tc', 'purehdse', 'dags7335', 'gb7358', 'mbtwinplus', 'roxxs200hd', 'u533', 'inihde', 't2cable', '9911lx', 'tmnano', 'mutant1100', 'gb7325', 'odinm7', '7215s', 'viperslim', 'zgemmah2splus', 'vg2000', 'mbtwin', 'mutant530c', '9920lx', 'u532', 'gb7252', 'mbhybrid', 'optimussos', 'u41', 'u43', 'dinobot4kse', 'tmnano2t', 'force3uhd', '9910lx', 'force1', 'iqonios200hd', 'axase3c', 'xpeedlx1', 'zgemmah102h', 'enibox', 'g300', 'protek4kx2', 'galaxym6', 'u52', 'u51', 'vipert2c', 'zgemmah3ac', 'xc7346', 'mbmicrov2', 'force3uhdplus', 'mbmicro', 'classm', 'beyonwizt2', 'zgemmai55se', 'ventonhdx', 'axase3', 'iqonios100hd', 'dinobot4kelite', '7005s', 'vimastec1500', 'evo', '7300s', 'u45', 'vipersingle', 'gb72604', '7105s', 'vimastec1000', 'evoslimt2c', 'novatwin', 'ultramini', 'g101', 'megaforce2', 'fusionhd', '8100s', 'evominiplus', 'inihdx', 'force2nano', 'u53', 'mbultra']


def getmodels(BUILDMACHINE):
    MACHINE = BUILDMACHINE
    if (BUILDMACHINE == "classm") or (BUILDMACHINE == "starsatlx") or (BUILDMACHINE == "genius") or (BUILDMACHINE == "evo") or (BUILDMACHINE == "galaxym6") or (BUILDMACHINE == "axodin") or (BUILDMACHINE == "axodinc"):
        MACHINE = "odinm7"
    elif (BUILDMACHINE == "geniuse3hd") or (BUILDMACHINE == "evoe3hd") or (BUILDMACHINE == "axase3") or (BUILDMACHINE == "axase3c"):
        MACHINE = "e3hd"
    elif (BUILDMACHINE == "maram9"):
        MACHINE = "odinm9"
    elif (BUILDMACHINE == "ventonhdx") or (BUILDMACHINE == "sezam5000hd") or (BUILDMACHINE == "mbtwin") or (BUILDMACHINE == "beyonwizt3"):
        MACHINE = "inihdx"
    elif (BUILDMACHINE == "sezam1000hd") or (BUILDMACHINE == "xpeedlx1") or (BUILDMACHINE == "xpeedlx2") or (BUILDMACHINE == "mbmini") or (BUILDMACHINE == "atemio5x00") or (BUILDMACHINE == "bwidowx"):
        MACHINE = "inihde"
    elif (BUILDMACHINE == "atemio6000") or (BUILDMACHINE == "atemio6100") or (BUILDMACHINE == "atemio6200") or (BUILDMACHINE == "mbminiplus") or (BUILDMACHINE == "mbhybrid") or (BUILDMACHINE == "bwidowx2") or (BUILDMACHINE == "beyonwizt2") or (BUILDMACHINE == "opticumtt") or (BUILDMACHINE == "evoslim") or (BUILDMACHINE == "xpeedlxpro"):
        MACHINE = "inihde2"
    elif (BUILDMACHINE == "xpeedlx3") or (BUILDMACHINE == "sezammarvel") or (BUILDMACHINE == "atemionemesis") or (BUILDMACHINE == "mbultra") or (BUILDMACHINE == "beyonwizt4"):
        MACHINE = "inihdp"
    elif (BUILDMACHINE == "xp1000mk") or (BUILDMACHINE == "xp1000max") or (BUILDMACHINE == "sf8") or (BUILDMACHINE == "xp1000plus"):
        MACHINE = "xp1000"
    elif (BUILDMACHINE == "mixoslumi"):
        MACHINE = "eboxlumi"
    elif (BUILDMACHINE == "mixosf7"):
        MACHINE = "ebox7358"
    elif (BUILDMACHINE == "mixosf5mini") or (BUILDMACHINE == "gi9196lite"):
        MACHINE = "ebox5100"
    elif (BUILDMACHINE == "mixosf5") or (BUILDMACHINE == "gi9196m"):
        MACHINE = "ebox5000"
    elif (BUILDMACHINE == "sogno8800hd") or (BUILDMACHINE == "uniboxhde"):
        MACHINE = "blackbox7405"
    elif (BUILDMACHINE == "enfinity") or (BUILDMACHINE == "marvel1"):
        MACHINE = "ew7358"
    elif (BUILDMACHINE == "mutant2400") or (BUILDMACHINE == "quadbox2400"):
        MACHINE = "hd2400"
    elif (BUILDMACHINE == "mutant11"):
        MACHINE = "hd11"
    elif (BUILDMACHINE == "mutant1100") or (BUILDMACHINE == "vizyonvita"):
        MACHINE = "hd1100"
    elif (BUILDMACHINE == "mutant1200"):
        MACHINE = "hd1200"
    elif (BUILDMACHINE == "mutant1265"):
        MACHINE = "hd1265"
    elif (BUILDMACHINE == "mutant1500"):
        MACHINE = "hd1500"
    elif (BUILDMACHINE == "mutant500c"):
        MACHINE = "hd500c"
    elif (BUILDMACHINE == "mutant530c"):
        MACHINE = "hd530c"
    elif (BUILDMACHINE == "vimastec1000"):
        MACHINE = "vs1000"
    elif (BUILDMACHINE == "enibox") or (BUILDMACHINE == "mago") or (BUILDMACHINE == "x1plus") or (BUILDMACHINE == "sf108"):
        MACHINE = "vg5000"
    elif (BUILDMACHINE == "t2cable"):
        MACHINE = "jj7362"
    elif (BUILDMACHINE == "x2plus"):
        MACHINE = "ew7356"
    elif (BUILDMACHINE == "bre2ze"):
        MACHINE = "ew7362"
    elif (BUILDMACHINE == "evomini"):
        MACHINE = "ch62lc"
    elif (BUILDMACHINE == "zgemmash1") or (BUILDMACHINE == "zgemmas2s") or (BUILDMACHINE == "zgemmass") or (BUILDMACHINE == "zgemmash2"):
        MACHINE = "sh1"
    elif (BUILDMACHINE == "zgemmahs") or (BUILDMACHINE == "zgemmah2s") or (BUILDMACHINE == "zgemmah2h") or (BUILDMACHINE == "novatwin") or (BUILDMACHINE == "novacombo") or (BUILDMACHINE == "zgemmah3ac") or (BUILDMACHINE == "zgemmah32tc") or (BUILDMACHINE == "zgemmah2splus"):
        MACHINE = "h3"
    elif (BUILDMACHINE == "zgemmaslc"):
        MACHINE = "lc"
    elif (BUILDMACHINE == "zgemmai55") or (BUILDMACHINE == "novaip"):
        MACHINE = "i55"
    elif (BUILDMACHINE == "zgemmai55plus"):
        MACHINE = "i55plus"
    elif (BUILDMACHINE == "zgemmai55se"):
        MACHINE = "i55se"
    elif (BUILDMACHINE == "zgemmah4"):
        MACHINE = "h4"
    elif (BUILDMACHINE == "zgemmah5") or (BUILDMACHINE == "zgemmah52s") or (BUILDMACHINE == "zgemmah5ac") or (BUILDMACHINE == "zgemmah52tc") or (BUILDMACHINE == "zgemmah52splus"):
        MACHINE = "h5"
    elif (BUILDMACHINE == "zgemmah6"):
        MACHINE = "h6"
    elif (BUILDMACHINE == "zgemmah7"):
        MACHINE = "h7"
    elif (BUILDMACHINE == "zgemmah82h"):
        MACHINE = "h8"
    elif (BUILDMACHINE == "zgemmah9s") or (BUILDMACHINE == "zgemmah9t") or (BUILDMACHINE == "zgemmah9splus") or (BUILDMACHINE == "zgemmah92s") or (BUILDMACHINE == "zgemmah92h"):
        MACHINE = "h9"
    elif (BUILDMACHINE == "zgemmah92hse") or (BUILDMACHINE == "zgemmah9sse"):
        MACHINE = "h9se"
    elif (BUILDMACHINE == "zgemmah9combose") or (BUILDMACHINE == "zgemmah9twinse"):
        MACHINE = "h9combose"
    elif (BUILDMACHINE == "zgemmah9combo") or (BUILDMACHINE == "zgemmah9twin"):
        MACHINE = "h9combo"
    elif (BUILDMACHINE == "zgemmah102s") or (BUILDMACHINE == "zgemmah102h") or (BUILDMACHINE == "zgemmah10combo"):
        MACHINE = "h10"
    elif (BUILDMACHINE == "zgemmah11s") or (BUILDMACHINE == "zgemmah112h"):
        MACHINE = "h11"
    elif (BUILDMACHINE == "zgemmahzeros"):
        MACHINE = "hzero"
    elif (BUILDMACHINE == "xcombo"):
        MACHINE = "vg2000"
    elif (BUILDMACHINE == "tyrant"):
        MACHINE = "vg1000"
    elif (BUILDMACHINE == "mbmicro") or (BUILDMACHINE == "e4hd") or (BUILDMACHINE == "e4hdhybrid"):
        MACHINE = "7000s"
    elif (BUILDMACHINE == "mbmicrov2"):
        MACHINE = "7005s"
    elif (BUILDMACHINE == "twinboxlcd") or (BUILDMACHINE == "singleboxlcd"):
        MACHINE = "7100s"
    elif (BUILDMACHINE == "twinboxlcdci5"):
        MACHINE = "7105s"
    elif (BUILDMACHINE == "sf208") or (BUILDMACHINE == "sf228"):
        MACHINE = "7210s"
    elif (BUILDMACHINE == "sf238"):
        MACHINE = "7215s"
    elif (BUILDMACHINE == "9910lx"):
        MACHINE = "7220s"
    elif (BUILDMACHINE == "9911lx") or (BUILDMACHINE == "e4hdcombo") or (BUILDMACHINE == "9920lx"):
        MACHINE = "7225s"
    elif (BUILDMACHINE == "odin2hybrid"):
        MACHINE = "7300s"
    elif (BUILDMACHINE == "odinplus"):
        MACHINE = "7400s"
    elif (BUILDMACHINE == "e4hdultra") or (BUILDMACHINE == "protek4k"):
        MACHINE = "8100s"
    elif (BUILDMACHINE == "xpeedlxcs2") or (BUILDMACHINE == "xpeedlxcc") or (BUILDMACHINE == "et7x00mini"):
        MACHINE = "ultramini"
    elif (BUILDMACHINE == "mbtwinplus") or (BUILDMACHINE == "sf3038") or (BUILDMACHINE == "alphatriple"):
        MACHINE = "g300"
    elif (BUILDMACHINE == "sf128") or (BUILDMACHINE == "sf138"):
        MACHINE = "g100"
    elif (BUILDMACHINE == "bre2zet2c"):
        MACHINE = "g101"
    elif (BUILDMACHINE == "osmega"):
        MACHINE = "xc7346"
    elif (BUILDMACHINE == "spycat") or (BUILDMACHINE == "osmini") or (BUILDMACHINE == "spycatmini") or (BUILDMACHINE == "osminiplus") or (BUILDMACHINE == "spycatminiplus"):
        MACHINE = "xc7362"
    elif (BUILDMACHINE == "spycat4kmini") or (BUILDMACHINE == "spycat4k") or (BUILDMACHINE == "spycat4kcombo"):
        MACHINE = "xc7439"
    elif (BUILDMACHINE == "dcube") or (BUILDMACHINE == "mkcube") or (BUILDMACHINE == "ultima"):
        MACHINE = "cube"
    elif (BUILDMACHINE == "amikomini") or (BUILDMACHINE == "dynaspark") or (BUILDMACHINE == "dynasparkplus") or (BUILDMACHINE == "amiko8900") or (BUILDMACHINE == "sognorevolution") or (BUILDMACHINE == "arguspingulux") or (BUILDMACHINE == "arguspinguluxmini") or (BUILDMACHINE == "arguspinguluxplus") or (BUILDMACHINE == "sparkreloaded") or (BUILDMACHINE == "sabsolo") or (BUILDMACHINE == "fulanspark1") or (BUILDMACHINE == "sparklx") or (BUILDMACHINE == "gis8120"):
        MACHINE = "spark"
    elif (BUILDMACHINE == "dynaspark7162") or (BUILDMACHINE == "amikoalien") or (BUILDMACHINE == "sognotriple") or (BUILDMACHINE == "sparktriplex") or (BUILDMACHINE == "sabtriple") or (BUILDMACHINE == "sparkone") or (BUILDMACHINE == "giavatar"):
        MACHINE = "spark7162"
    elif (BUILDMACHINE == "tm2t") or (BUILDMACHINE == "tmnano") or (BUILDMACHINE == "tmnano2t") or (BUILDMACHINE == "tmsingle") or (BUILDMACHINE == "tmtwin") or (BUILDMACHINE == "iqonios100hd") or (BUILDMACHINE == "iqonios300hd") or (BUILDMACHINE == "iqonios300hdv2") or (BUILDMACHINE == "optimussos1") or (BUILDMACHINE == "mediabox") or (BUILDMACHINE == "iqonios200hd") or (BUILDMACHINE == "roxxs200hd") or (BUILDMACHINE == "mediaart200hd") or (BUILDMACHINE == "optimussos2"):
        MACHINE = "dags7335"
    elif (BUILDMACHINE == "tmnano2super") or (BUILDMACHINE == "tmnano3t") or (BUILDMACHINE == "force1") or (BUILDMACHINE == "force1plus") or (BUILDMACHINE == "megaforce1plus") or (BUILDMACHINE == "worldvisionf1") or (BUILDMACHINE == "worldvisionf1plus") or (BUILDMACHINE == "optimussos1plus") or (BUILDMACHINE == "optimussos2plus") or (BUILDMACHINE == "optimussos3plus"):
        MACHINE = "dags7356"
    elif (BUILDMACHINE == "tmnanose") or (BUILDMACHINE == "tmnanosem2") or (BUILDMACHINE == "tmnanosem2plus") or (BUILDMACHINE == "tmnanosecombo") or (BUILDMACHINE == "force2plus") or (BUILDMACHINE == "force2") or (BUILDMACHINE == "megaforce2") or (BUILDMACHINE == "optimussos") or (BUILDMACHINE == "force2se") or (BUILDMACHINE == "fusionhd") or (BUILDMACHINE == "fusionhdse") or (BUILDMACHINE == "purehd") or (BUILDMACHINE == "force2nano") or (BUILDMACHINE == "tmnanom3") or (BUILDMACHINE == "valalinux"):
        MACHINE = "dags7362"
    elif (BUILDMACHINE == "force2plushv") or (BUILDMACHINE == "purehdse") or (BUILDMACHINE == "lunix") or (BUILDMACHINE == "lunixco"):
        MACHINE = "dags73625"
    elif (BUILDMACHINE == "revo4k") or (BUILDMACHINE == "force3uhd") or (BUILDMACHINE == "force3uhdplus") or (BUILDMACHINE == "tmtwin4k") or (BUILDMACHINE == "galaxy4k") or (BUILDMACHINE == "tm4ksuper") or (BUILDMACHINE == "lunix34k"):
        MACHINE = "dags7252"
    elif (BUILDMACHINE == "force4") or (BUILDMACHINE == "lunix4k"):
        MACHINE = "dags72604"
    elif (BUILDMACHINE == "dual"):
        MACHINE = "dagsmv200"
    elif (BUILDMACHINE == "gb800se") or (BUILDMACHINE == "gb800ue"):
        MACHINE = "gb7325"
    elif (BUILDMACHINE == "gb800seplus") or (BUILDMACHINE == "gb800ueplus") or (BUILDMACHINE == "gbipbox"):
        MACHINE = "gb7358"
    elif (BUILDMACHINE == "gbultrase") or (BUILDMACHINE == "gbultraue") or (BUILDMACHINE == "gbx1") or (BUILDMACHINE == "gbx3"):
        MACHINE = "gb7362"
    elif (BUILDMACHINE == "gbx2") or (BUILDMACHINE == "gbultraueh") or (BUILDMACHINE == "gbx3h"):
        MACHINE = "gb73625"
    elif (BUILDMACHINE == "gbquad") or (BUILDMACHINE == "gbquadplus"):
        MACHINE = "gb7356"
    elif (BUILDMACHINE == "gbquad4k") or (BUILDMACHINE == "gbue4k"):
        MACHINE = "gb7252"
    elif (BUILDMACHINE == "gbx34k"):
        MACHINE = "gb72604"
    elif (BUILDMACHINE == "gbtrio4k") or (BUILDMACHINE == "gbip4k") or (BUILDMACHINE == "gbtrio4kpro"):
        MACHINE = "gbmv200"
    elif (BUILDMACHINE == "sf98") or (BUILDMACHINE == "force2nano") or (BUILDMACHINE == "evoslimse"):
        MACHINE = "yh7362"
    elif (BUILDMACHINE == "evoslimt2c"):
        MACHINE = "yh62tc"
    elif (BUILDMACHINE == "evominiplus"):
        MACHINE = "ch625lc"
    elif (BUILDMACHINE == "vipert2c"):
        MACHINE = "yh625tc"
    elif (BUILDMACHINE == "vipercombo"):
        MACHINE = "yh625dt"
    elif (BUILDMACHINE == "vipercombohdd"):
        MACHINE = "ch625dt"
    elif (BUILDMACHINE == "viperslim"):
        MACHINE = "yh73625"
    elif (BUILDMACHINE == "evominiplus"):
        MACHINE = "ch625lc"
    elif (BUILDMACHINE == "mutant51") or (BUILDMACHINE == "ax51") or (BUILDMACHINE == "bre2ze4k"):
        MACHINE = "hd51"
    elif (BUILDMACHINE == "mutant60") or (BUILDMACHINE == "ax60"):
        MACHINE = "hd60"
    elif (BUILDMACHINE == "mutant61") or (BUILDMACHINE == "ax61"):
        MACHINE = "hd61"
    elif (BUILDMACHINE == "mutant66se"):
        MACHINE = "hd66se"
    elif (BUILDMACHINE == "vimastec1500"):
        MACHINE = "vs1500"
    elif (BUILDMACHINE == "gi11000") or (BUILDMACHINE == "viper4k51"):
        MACHINE = "et1x000"
    elif (BUILDMACHINE == "beyonwizu4"):
        MACHINE = "et13000"
    elif (BUILDMACHINE == "dinoboth265") or (BUILDMACHINE == "axashistwin"):
        MACHINE = "u41"
    elif (BUILDMACHINE == "spycatminiv2") or (BUILDMACHINE == "anadolprohd5") or (BUILDMACHINE == "iziboxecohd") or (BUILDMACHINE == "jdhdduo") or (BUILDMACHINE == "vipertwin") or (BUILDMACHINE == "vipersingle"):
        MACHINE = "u42"
    elif (BUILDMACHINE == "turing"):
        MACHINE = "u43"
    elif (BUILDMACHINE == "axashistwinplus"):
        MACHINE = "u45"
    elif (BUILDMACHINE == "dinobot4k") or (BUILDMACHINE == "mediabox4k") or (BUILDMACHINE == "anadol4k"):
        MACHINE = "u5"
    elif (BUILDMACHINE == "axashis4kcombo") or (BUILDMACHINE == "dinobot4kl") or (BUILDMACHINE == "anadol4kv2") or (BUILDMACHINE == "anadol4kcombo") or (BUILDMACHINE == "protek4kx1"):
        MACHINE = "u51"
    elif (BUILDMACHINE == "dinobot4kplus") or (BUILDMACHINE == "axashis4kcomboplus"):
        MACHINE = "u52"
    elif (BUILDMACHINE == "dinobot4kmini"):
        MACHINE = "u53"
    elif (BUILDMACHINE == "arivacombo"):
        MACHINE = "u532"
    elif (BUILDMACHINE == "arivatwin"):
        MACHINE = "u533"
    elif (BUILDMACHINE == "dinobot4kpro"):
        MACHINE = "u54"
    elif (BUILDMACHINE == "dinobotu55") or (BUILDMACHINE == "iziboxone4k") or (BUILDMACHINE == "hitube4k") or (BUILDMACHINE == "iziboxx3"):
        MACHINE = "u55"
    elif (BUILDMACHINE == "axashisc4k") or (BUILDMACHINE == "dinobot4kelite"):
        MACHINE = "u56"
    elif (BUILDMACHINE == "viper4kv20") or (BUILDMACHINE == "protek4kx2") or (BUILDMACHINE == "iziboxelite4k") or (BUILDMACHINE == "dinobot4ktwin") or (BUILDMACHINE == "hitube4kpro") or (BUILDMACHINE == "viper4kv30") or (BUILDMACHINE == "hitube4kplus") or (BUILDMACHINE == "iziboxx4"):
        MACHINE = "u57"
    elif (BUILDMACHINE == "iziboxone4kplus") or (BUILDMACHINE == "viper4kv40"):
        MACHINE = "u571"
    elif (BUILDMACHINE == "dinobot4kse") or (BUILDMACHINE == "ferguson4k"):
        MACHINE = "u5pvr"
    elif (BUILDMACHINE == "clap4k"):
        MACHINE = "cc1"
    elif (BUILDMACHINE == "maxytecmultise") or (BUILDMACHINE == "axmultiboxse") or (BUILDMACHINE == "anadolmultiboxse") or (BUILDMACHINE == "novaler4kse"):
        MACHINE = "multiboxse"
    elif (BUILDMACHINE == "anadolmulti") or (BUILDMACHINE == "maxytecmulti") or (BUILDMACHINE == "anadolmultitwin") or (BUILDMACHINE == "axmulticombo") or (BUILDMACHINE == "axmultitwin") or (BUILDMACHINE == "novaler4k"):
        MACHINE = "multibox"
    elif (BUILDMACHINE == "novaler4kpro"):
        MACHINE = "multiboxpro"
    return MACHINE


models = []
for machine in machines:
    model = getmodels(machine)
    if model not in models:
        models.append(model)

models = set(models)

FEED_URLS1 = [
	("OpenViX", "https://www.openvix.co.uk/json/%s", "machinebuild"),
	("OpenHDF", "https://flash.hdfreaks.cc/openhdf/json/%s", "machinebuild"),
	("Open8eIGHT", "http://openeight.de/json/%s", "machinebuild"),
	("OpenDROID", "https://opendroid.org/json/%s", "machinebuild"),
	("TeamBlue", "https://images.teamblue.tech/json/%s", "machinebuild"),
	("EGAMI", "https://image.egami-image.com/json/%s", "machinebuild"),
	("OpenBH", "https://images.openbh.net/json/%s", "machinebuild"),
	("OpenSPA", "https://openspa.webhop.info/online/json.php?box=%s", "machinebuild")
]

FEED_URLS2 = [
	("OpenPLi", "http://downloads.openpli.org/json/%s", "model"),
	("OpenVision", "https://images.openvision.dedyn.io/json/%s", "model")
]

model_machines = {}

for machine in set(list(machines) + list(models)):
    model_machines[machine] = []

for feed in FEED_URLS1:
    distro = feed[0]
    white = []
    print("Check %s" % distro)
    filter = filters.get(distro)
    for machine in machines:
        if machine in BLACKLIST:
            continue
        if not filter or re.match(filter, machine):
            url = feed[1] % machine
            x = requests.get(url)
            if x and x.text and len(x.text) > 10:
                model_machines[machine].append(distro)
                white.append(machine)
#    print("Distro:%s -> %s" % (distro, white))

for feed in FEED_URLS2:
    distro = feed[0]
    white = []
    print("Check %s" % distro)
    filter = filters.get(distro)
    for machine in models:
        if machine in BLACKLIST:
            continue
        if not filter or re.match(filter, machine):
            url = feed[1] % machine
            x = requests.get(url)
            if x and x.text and len(x.text) > 10:
                model_machines[machine].append(distro)
                white.append(machine)
#    print("Distro:%s -> %s" % (distro, white))

black = []

for machine in model_machines.items():
    with open("Rel/%s" % machine[0], "w") as fd:
        if not machine[1]:
            black.append(machine[0])
        fd.write(" ".join(machine[1]))

with open("Rel/black.lst", "w") as fd:
    fd.write("\n".join(black))
