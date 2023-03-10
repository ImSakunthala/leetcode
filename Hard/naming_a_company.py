"""
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.



Example 1:

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.


Constraints:

2 <= ideas.length <= 5 * 104
1 <= ideas[i].length <= 10
ideas[i] consists of lowercase English letters.
All the strings in ideas are unique.
"""
from builtins import filter
from typing import List
from collections import defaultdict
import time


class Solution:
    def brute_force(self, ideas: List[str]) -> int:
        start_time = time.time()
        name_idea = []

        for name1 in ideas:
            for name2 in ideas:

                if name1 != name2:
                    name_1 = name2[0] + name1[1:]
                    name_2 = name1[0] + name2[1:]
                    if name_1 not in ideas:
                        if name_2 not in ideas:
                            name_idea.append([name_1, name_2])

        print("--- %s seconds ---" % (time.time() - start_time))

        return len(name_idea)

    def distinctNames(self, ideas: List[str]) -> int:
        result = 0
        start_time = time.time()

        idea_groups = defaultdict(list)

        for idea in ideas:
            idea_groups[idea[1:]].append(idea)

        list_of_groups = [group for group in idea_groups.values()]

        for group1 in list_of_groups:
            length_of_group = self.length_of_group(group1, list_of_groups)
            result += len(length_of_group)
        print("--- %s seconds ---" % (time.time() - start_time))
        return result

    def length_of_group(self, group1: list, list_og_groups: List[list]) -> list:
        result = []

        for idea1 in group1:
            for group2 in list_og_groups:
                if group1 != group2:
                    for idea2 in group2:
                        if idea1[0] != idea2[0]:
                            result.append([idea1, idea2])
        return result

solution = Solution()
print(solution.brute_force(ideas=["ufrd", "evjfco", "ojdyeze", "pildaslfj", "bhush", "q", "fvbvd", "gmyfxe", "gsnzuzxd",
                                  "acaw", "kv", "ak", "itktagmfvc", "xafbvv", "iucpfg", "lhgxuanmk", "efljasin",
                                  "raldgyqnl", "pxcuapwd", "ymfiudiy", "qubqhventm", "htcpug", "bliwkz", "ibd",
                                  "wmackcg",
                                  "hjy", "frvviojvjl", "ialerc", "xyeppctwam", "fonjranlmq", "pdnwak", "gzjkoyxn",
                                  "imyvh",
                                  "wxpnt", "kzrdvqrcz", "qvwwvumv", "hvd", "heaqhxvn", "fpqb", "qmwebgbq", "x", "zm",
                                  "ad",
                                  "jmfqqphb", "fqdsfskyxa", "sxtzh", "s", "bosjkmv", "dxazbbk", "eguj", "cvu", "kr",
                                  "uvm",
                                  "godsfrbd", "sgj", "cvxrzer", "xbb", "hhcjyc", "p", "sg", "gppoq", "pzenuvvi",
                                  "rjhhk",
                                  "rdtci", "rp", "ttqacsxhd", "u", "braflwzfvn", "sabfkglhpp", "c", "tamy", "tchuflso",
                                  "w",
                                  "fgkwtwgkje", "reuvvjnga", "msrfj", "wgwfflbia", "eizpigf", "ezpkwrkfye", "jsd",
                                  "bvgvrzvb", "xeb", "jo", "hcsnhodewy", "t", "mebfwel", "grzcebhdm", "mhoyzwc",
                                  "zhfnbiodb", "dtwinj", "xph", "oagejrbw", "otlvqywmbj", "nloryp", "bwmwvyhdpk", "tn",
                                  "bzpu", "iicrfdnxzg", "zexi", "fcdt", "pwdq", "shthfmmz", "ytupezhd", "li", "ktqyl",
                                  "bpaqphrymg", "wq", "iwhagzdr", "dhykysqamu", "euniekj", "sm", "zf", "fnige",
                                  "xvnifcpnbm", "lwxm", "qcnbmwavsl", "gmkmlolfp", "merpmw", "ujsito", "vfmqygu",
                                  "weemh",
                                  "cmqfjc", "bsi", "baycguvsk", "beemh", "xsj", "kpm", "m", "wgvh", "qjpn", "ez",
                                  "pabfkglhpp", "jkwaleku", "gujo", "tgpc", "szkgafvpu", "bibwzumdzk", "ucloyz",
                                  "dkxazydf",
                                  "pjfwbx", "g", "lwwkaypq", "sbx", "sxr", "pwxco", "qmmlqtr", "qjwgtc", "abcunxeuz",
                                  "ehqolylwy", "hcjpmhew", "mqjervmdn", "vjnti", "mapr", "hkxru", "idfrdpkdzy",
                                  "klxpubomc",
                                  "bwwepvrbs", "wsmjuzvyrj", "oz", "ujmxsgkbqw", "bzamyz", "mpuo", "dpbzutc", "ye",
                                  "oswzwnqmxt", "ftvdj", "qa", "k", "pewwqberzj", "lkxngnzyhd", "twfbg", "krxqbcw",
                                  "rza",
                                  "uhnpmcp", "rdnmekawa", "bdtci", "hoccmond", "zovrgabd", "bfptusy", "lcguji",
                                  "jrznpo",
                                  "h", "jegid", "ccnbmwavsl", "xdxjiu", "czg", "pnksktifrw", "vszouj", "ec", "unoulota",
                                  "qbksmdhrfl", "nuemd", "skk", "pyjlymwj", "vetlrnzyp", "lxoj", "yeqgz", "j",
                                  "kwswyofcd",
                                  "fnadu", "spqq", "tlqgtdbz", "jgtpg", "d", "xjqrbsv", "lu", "qlz", "sguzxjg", "zknw",
                                  "kbvt", "iaju", "bm", "om", "hwniqofxmk", "msrqlfqbmz", "zlkljalfuk", "gyqiecft",
                                  "kgieoqqged", "uncajn", "zxdttqrcq", "cgien", "tlqjhd", "qh", "kvx", "tnfcip",
                                  "uiyaixpzoa", "hlms", "cys", "iez", "fuzrxfx", "tus", "uxhsl", "dyttyyur", "pb",
                                  "zwvfbibbzk", "jcv", "geeskwdv", "etrrctme", "cn", "sbkou", "qehxc", "kjmwyep",
                                  "nsewcy",
                                  "rjnye", "kvus", "joemuly", "vcgkqyacc", "aivr", "uzmvau", "orabkt", "lvmxwdjy",
                                  "hugw",
                                  "wutq", "imhvii", "ev", "yoda", "cqyligiq", "jhyl", "piqjyenws", "gbjnb", "int",
                                  "krouwpcvf", "uaygpmgrxm", "nqakxp", "zsy", "a", "qkobvf", "mld", "gj", "yfrxzp",
                                  "qetwhnkav", "junficb", "wpzolbyomp", "ndvafzxgw", "kfetkof", "zeam", "dqyelgc",
                                  "hlqizp",
                                  "zztfegg", "dkf", "qjmbmwm", "mo", "necijfqgl", "ksus", "gfaqtwokn", "iefzg", "sier",
                                  "xbsxppxnof", "ervviojvjl", "uhsmgsfpc", "gyoriyhjv", "apsvhqfku", "zedpul",
                                  "dfijydxnbk",
                                  "vajpmtv", "xqwfjgkove", "iwxolneugu", "l", "kqixmaljie", "nceqhmky", "umjkdbp",
                                  "fauizhiz", "ilovtl", "ntmymf", "b", "blqyeozud", "luubvtaza", "kkqutkavb", "adu",
                                  "qlncjz", "nzg", "jypszs", "msevbx", "qifrc", "mbd", "khzmrppp", "phxtvpibnh", "hi",
                                  "wegtljkhz", "vygksg", "znnxas", "fxqqastbi", "upviltbs", "mrvtkfxqz", "hbyhawmdf",
                                  "sker", "diu", "sqckv", "wrdsfkz", "bhxv", "uqbqs", "riqz", "hw", "iyxjdoyjs",
                                  "sksgltkdgh", "pub", "sowbbdpm", "cpidjcktia", "fie", "kyytk", "njq", "ip", "kcwj",
                                  "uo",
                                  "rgniqun", "timrmt", "gdtgok", "vu", "iyuqgipd", "gczqfwpea", "lixkgpjyt", "weed",
                                  "rchhnojpyt", "ipqkvz", "rrjwkzb", "wjoprckvz", "fmlu", "yxsqs", "nuqmyiivf",
                                  "gbgizujoz",
                                  "bxxxb", "sptrhkof", "f", "uuh", "uyoftrd", "jfblfdro", "fwbh", "lnuvw", "nkhtvzc",
                                  "otlnjlmxng", "xrkievj", "qe", "vgur", "jpmchp", "dsmrhmzsav", "xuypdlqf", "ipm",
                                  "qdvwhaqirv", "gjdvsg", "ocuvuraln", "nwkpcjfzs", "gftlvkvtsy", "rmvvcpiy", "wfo",
                                  "jjdfgz", "dmckkg", "ouqcb", "n", "exp", "hzccsfisdg", "xwfxrked", "oaba",
                                  "eajeavpgk",
                                  "wmvvcpiy", "phuzhfet", "spvhcjcjkf", "zuaqjn", "mcdp", "ovbcho", "awndm",
                                  "nmhwviqsh",
                                  "vxicuxvo", "fzxwjrt", "qpzmdtbzm", "mnfcip", "hcqbf", "qfs", "ogyyhjn", "maoemq",
                                  "cbsyti", "wndk", "ykk", "dnbqgptwdi", "mdaxwnf", "mkdsh", "bdqcwlunm", "apntxmz",
                                  "zkpibygdg", "mknndceh", "kbcftqbvyl", "mlwn", "pkjlb", "ulqy", "lkf", "vdieyjkj",
                                  "bupa",
                                  "tjv", "opqbpmpt", "gr", "jmkrolrp", "clafjy", "ofxf", "ek", "tcpkl", "ozoijnd",
                                  "uybm",
                                  "hn", "zythamzz", "ayqdabeg", "nfkp", "seeed", "wpbbf", "fkyvotinr", "nsfhob",
                                  "bnsfqa",
                                  "bvlebiiljh", "hpycw", "atwyi", "buigtg", "nojhqg", "zeatqt", "nnfcip", "pteqfne",
                                  "byzivljxfx", "kngtchkh", "ublip", "bsbevyxreh", "aykodk", "ltwinj", "kvlebiiljh",
                                  "bbbeibja", "vbgjnz", "tjvy", "rvo", "ahnghgjx", "clkmga", "znwvzwi", "sdxmvq",
                                  "yjcz",
                                  "pdvlteoh", "fzqokaw", "iom", "pnjx", "mlsjpedb", "eufhzqyt", "cxasfr", "lp",
                                  "scnlouri",
                                  "cbpyzhmmpn", "stfmxjpyn", "ixazbbk", "lznzlkkvsr", "gwdiyzot", "mzt", "fz", "ge",
                                  "vvj",
                                  "uzge", "evvp", "iazduxrwqh", "fpnouyya", "sdrldphp", "r", "hfbsco", "eukeuowg",
                                  "jquhlraxje", "ksdvhnc", "cmj", "cgnqev", "soamuijlq", "xx", "mrikzjfdj", "spdgfkb",
                                  "ygsrjpglui", "uf", "qygxiduzt", "rbsrpcsuin", "iworwissw", "cnsbagxt", "khf",
                                  "bacwrqtmj", "krlo", "xdvnms", "wvh", "bnr", "orcakqbj", "ijhfqvoa", "waf", "vhimahp",
                                  "bspizjin", "nvbcho", "rcjts", "mf", "rzoijnd", "omwekniv", "ow", "fp", "ypqzcdkz",
                                  "ntaikqd", "wpycw", "hqkjmwm", "cezjxigi", "ifwzxq", "xkommk", "ygdeztnl", "dwin",
                                  "hfrgsyjmqj", "nvurxqhage", "ycjts", "fygjo", "ix", "ct", "fuhowzonh", "ziwfbeohxp",
                                  "zjjn", "csxemb", "nbrjxkgk", "evmp", "ah", "snxi", "wkjkoyeyn", "ynlvh", "kkumbufht",
                                  "rc", "gprtqz", "juro", "tdd", "tyko", "neyisbvnd", "bybmwsxwh", "silpcrif",
                                  "agozvuxr",
                                  "vgpk", "cgt", "huth", "oppmx", "kb", "nhbf", "qqbzg", "tingkixov", "zsygmj", "vmf",
                                  "rgj", "rkkfswqiay", "paqqtsdboi", "hauizhiz", "rpuophvhtg", "tbmwbkgmtc", "pmw",
                                  "crr",
                                  "ohd", "xrox", "cvf", "ocjje", "gjs", "y", "glqqjnye", "xmmwck", "nxldrwb",
                                  "cgubnevt",
                                  "yzllnsnuy", "kpoy", "wuuwlqvpvt", "hcl", "z", "kbhhg", "xdelalwwiy", "vbrf", "go",
                                  "qd",
                                  "uzrdvqrcz", "nj", "qhtmsbuvnl", "vrfpnpkx", "eaafhjvd", "ksocgyzw", "qmx", "ob",
                                  "pqyoep", "peizqg", "qb", "rmfk", "csq", "bmnlcmpb", "tycnzkkck", "sijexib", "fu",
                                  "npxyo", "jifdm", "bfbsco", "yhaneeeh", "grnrnsowv", "ahywep", "jhcdyajqzw", "hunl",
                                  "ozalifegd", "wvdtcrhbus", "rng", "pszouj", "wrxqg", "segzex", "xlpinmkoms",
                                  "myehfdqsf",
                                  "oamgb", "tp", "qkxay", "muq", "fhlrvjh", "xrq", "yhqolylwy", "fmjidpdq", "nwfp",
                                  "plmfzopu", "raq", "aspge", "cg", "wvkcppffli", "ngbft", "mvcx", "tcvvefngzh",
                                  "ysvchiviug", "gomvkt", "ekeiqqw", "ygjypjc", "bpciyeibml", "evtqvma", "hkuhjvjyv",
                                  "dn",
                                  "fyflcpja", "gftzucziet", "wwbxpdudxl", "zmuqndc", "ggoqeid", "nmfqmzrfv", "jqkdw",
                                  "kfccwvpsgj", "zzvjrgzt", "lbpr", "chxv", "i", "uuljtgt", "cupdgzqhm", "lg", "jmp",
                                  "dr",
                                  "tsbsekkmyw", "lzboy", "vuoujrxb", "rsdcjae", "qbdwbk", "tguwbae", "qttta",
                                  "nnnhejwho",
                                  "jxquldfmaw", "zhiaytjbk", "vouwn", "gxazbbk", "urhytjb", "dkqhvbocjx", "ajjfwoqje",
                                  "nmomedocu", "jlikoyj", "jmoo", "mse", "owhoatludb", "eetfffs", "zprofcb", "fgo",
                                  "zn",
                                  "sreveqqc", "qmlymw", "vswjyppqgc", "ljbcrytui", "bjppk", "wsvowp", "ocjui",
                                  "wmnsqnlb",
                                  "hts", "getgk", "pbhbgyci", "yxpufkhrp", "pzkpkbka", "zdz", "ykct", "xt",
                                  "uilolvbbnj",
                                  "o", "lggfvojs", "bpwzvywuzp", "dvpplsvy", "nmfamegpoj", "dgcqfpqkd", "wxoyfq",
                                  "seqas",
                                  "egljwyfy", "uzedntcz", "tazdpd", "ezytbwuab", "vhabhw", "sgpdl", "mptqovn",
                                  "nrimahca",
                                  "ubtfxqtg", "urt", "qlm", "ynakzoo", "wgvuipkblf", "iarjzugcd", "gs", "xnapihbkmm",
                                  "jfkomz", "xszsw", "xlc", "tultq", "xmt", "pwr", "ecqmkrw", "rtmnwbnd", "oczlg",
                                  "fwgvyyef", "puxqkvnwj", "vua", "usq", "ysgrk"]))
print('6 ->', solution.distinctNames(ideas=["coffee", "donuts", "time", "toffee"]))
print('0 ->', solution.brute_force(ideas=["lack", "back"]))
