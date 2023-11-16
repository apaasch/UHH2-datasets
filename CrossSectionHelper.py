import importlib.util
from collections import namedtuple,Mapping
import os
import sys


CMSSW_BASE = os.environ.get("CMSSW_BASE")


def namedtuple_with_defaults(typename, field_names, default_values=()):
    T = namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T


class MCSampleValuesHelperPrototype():
    """
    Prototype class for MCSampleValuesHelper
    """

    __years = ["UL16preVFP","UL16postVFP","UL17","UL18","2022preEE","2022postEE","2023"]
    __energies = ["13TeV"]
    __xs_field_names = []
    __nevt_field_names = []
    __br_field_names = []
    __kfactor_field_names = []
    __corr_field_names = []
    __xml_field_names = []
    _key_field_map = {
        "CrossSection"   : ("XSec",-1.0),
        "NEvents"        : ("NEVT",-1.0),
        "BranchingRatio" : ("BRat",1.0),
        "kFactor"        : ("kFac",1.0),
        "Correction"     : ("Corr",1.0),
        "XMLname"        : ("Xml",""),
    }
    for __val in __years+__energies:
        for mode in ["", "Source"]:
            __xs_field_names.append("XSec"+mode+"_"+__val)
            __nevt_field_names.append("NEVT"+mode+"_"+__val)
            __br_field_names.append("BRat"+mode+"_"+__val)
            __kfactor_field_names.append("kFac"+mode+"_"+__val)
            __corr_field_names.append("Corr"+mode+"_"+__val)
            __xml_field_names.append("Xml"+mode+"_"+__val)
    XSValues      = namedtuple_with_defaults("XSValues",      __xs_field_names,       [_key_field_map["CrossSection"][1],""]*len(__years+__energies))
    NEventsValues = namedtuple_with_defaults("NEventsValues", __nevt_field_names,     [_key_field_map["NEvents"][1],""]*len(__years+__energies))
    BRValues      = namedtuple_with_defaults("BRValues",      __br_field_names,       [_key_field_map["BranchingRatio"][1],""]*len(__years+__energies))
    kFactorValues = namedtuple_with_defaults("kFactorValues", __kfactor_field_names,  [_key_field_map["kFactor"][1],""]*len(__years+__energies))
    CorrValues    = namedtuple_with_defaults("CorrValues",    __corr_field_names,     [_key_field_map["Correction"][1],""]*len(__years+__energies))
    XMLValues     = namedtuple_with_defaults("XMLValues",     __xml_field_names,      [_key_field_map["XMLname"][1],""]*len(__years+__energies))


class MCSampleValuesHelper(MCSampleValuesHelperPrototype):
    """Stores the cross sections and k-factors associated to a given physics process.

    The lists of years and energies used to identify a given cross section are also stored within this class.
    Given a process name, and year the appropriate cross section will be returned.

    Args:
        extra_dicts (:obj:`dict` of :obj:`dict` of :obj:`namedtuple_with_defaults`): Extra cross sections and k-factors to add to the __values_dict.

    Example:
        from CrossSectionHelper import *
        helper = MCSampleValuesHelper()
        helper.get_lumi("TTbarTo2L2Nu","13TeV","2018")
        helper.get_xs("TTbarTo2L2Nu","13TeV","2018")
        helper.get_nevt("TTbarTo2L2Nu","13TeV","2018")
        helper.get_br("TTbarTo2L2Nu","13TeV","2018")
        helper.get_xml("TTbar","13TeV","2016")
    """

    __values_dict = {

        "JetHT_RunA": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL18=171502033,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018A-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018A-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_RunB": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=9726665+133752091,
                NEVT_UL17=63043590,
                NEVT_UL18=78253065,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016B-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016B-{ver1,ver2}_HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017B-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017B-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018B-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018B-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_RunC": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=46495988,
                NEVT_UL17=96264601,
                NEVT_UL18=70027804,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016C-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017C-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017C-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018C-UL2018_MiniAODv2_GT36-v1.xml", XmlSource_UL18="/JetHT/Run2018C-UL2018_MiniAODv2_GT36-v1/MINIAOD",
            ),
        },

        "JetHT_RunD": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=73330042,
                NEVT_UL17=46145204,
                NEVT_UL18=356976276,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016D-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017D-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017D-UL2017_MiniAODv2-v1/MINIAOD",
                Xml_UL18="RunII_106X_v2/data/UL18/JetHT_Run2018D-UL2018_MiniAODv2-v2.xml", XmlSource_UL18="/JetHT/Run2018D-UL2018_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunE": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=69219288,
                NEVT_UL17=89630771,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016E-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017E-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017E-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunF": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=41564915,
                NEVT_UL16postVFP=6613811,
                NEVT_UL17=115429972,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/data/UL16preVFP/JetHT_Run2016F-HIPM_UL2016_MiniAODv2-v2.xml", XmlSource_UL16preVFP="/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016F-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016F-UL2016_MiniAODv2-v2/MINIAOD",
                Xml_UL17="RunII_106X_v2/data/UL17/JetHT_Run2017F-UL2017_MiniAODv2-v1.xml", XmlSource_UL17="/JetHT/JetHT_Run2017F-UL2017_MiniAODv2-v1/MINIAOD",
            ),
        },

        "JetHT_RunG": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=120745085,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016G-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016G-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "JetHT_RunH": {
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16postVFP=124054791,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16postVFP="RunII_106X_v2/data/UL16postVFP/JetHT_Run2016H-UL2016_MiniAODv2-v2.xml", XmlSource_UL16postVFP="/JetHT/JetHT_Run2016H-UL2016_MiniAODv2-v2/MINIAOD",
            ),
        },

        "QCD_Pt-15To20_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.804e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4702434.35096,
                NEVT_UL16postVFP=4351376.89588,
                NEVT_UL17=8303461.32576,
                NEVT_UL18=8855628.80125,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-15To20_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-20To30_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.525e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=29577312.2432,
                NEVT_UL16postVFP=29444607.714,
                NEVT_UL17=63163429.4457,
                NEVT_UL18=56254769.7319,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-20To30_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-30To50_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.366e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=26234818.0,
                NEVT_UL16postVFP=34132958.0,
                NEVT_UL17=57541818.0,
                NEVT_UL18=54774188.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30To50_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50To80_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.777e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=18641525.0,
                NEVT_UL16postVFP=20634072.0,
                NEVT_UL17=37145092.0,
                NEVT_UL18=37496434.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50To80_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80To120_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=8.862e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=20304318.4332,
                NEVT_UL16postVFP=21067289.5974,
                NEVT_UL17=42429014.0691,
                NEVT_UL18=42790996.6794,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80To120_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120To170_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.118e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=17582197.0466,
                NEVT_UL16postVFP=18915898.1684,
                NEVT_UL17=36756675.8228,
                NEVT_UL18=36907183.365,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120To170_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170To300_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=7.015e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=34986547.0,
                NEVT_UL16postVFP=32519689.0,
                NEVT_UL17=68143863.0,
                NEVT_UL18=68405126.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170To300_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300To470_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=6.201e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=26598488.6412,
                NEVT_UL16postVFP=28533156.0495,
                NEVT_UL17=54139451.5127,
                NEVT_UL18=56123430.7554,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300To470_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-470To600_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=5.908e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=19033401.1611,
                NEVT_UL16postVFP=18786627.538,
                NEVT_UL17=36772363.2966,
                NEVT_UL18=36226532.3567,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-470To600_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-600To800_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.825e+01, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=19147516.5358,
                NEVT_UL16postVFP=17852444.5469,
                NEVT_UL17=36664638.0857,
                NEVT_UL18=36450873.0597,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-600To800_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-800To1000_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.276e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=34818002.0,
                NEVT_UL16postVFP=36874214.0,
                NEVT_UL17=72233265.0,
                NEVT_UL18=75504652.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-800To1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-1000_MuEnrichedPt5" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.077e+00, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=12037432.0,
                NEVT_UL16postVFP=13437681.0,
                NEVT_UL17=25762679.0,
                NEVT_UL18=26237172.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-1000_MuEnrichedPt5_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-15to20_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.322e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=3955016.88151,
                NEVT_UL17=7872865.56044,
                NEVT_UL18=7734191.6292,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-15to20_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-20to30_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=4.915e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=6944461.1873,
                NEVT_UL17=13911351.1134,
                NEVT_UL18=14097326.3763,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-20to30_EMEnriched_CP5_pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_Pt-30to50_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=6.418e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4195275.0,
                NEVT_UL16postVFP=4256783.0,
                NEVT_UL17=8549222.0,
                NEVT_UL18=8433047.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-30to50_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-50to80_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.987e+06, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=5199617.0,
                NEVT_UL16postVFP=5350943.0,
                NEVT_UL17=10094541.0,
                NEVT_UL18=10338693.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-50to80_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-80to120_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.671e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4430933.68065,
                NEVT_UL16postVFP=4759037.9018,
                NEVT_UL17=9454898.89424,
                NEVT_UL18=9260620.50861,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-80to120_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-120to170_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=6.661e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4667710.26898,
                NEVT_UL16postVFP=4799237.98617,
                NEVT_UL17=9671184.56819,
                NEVT_UL18=9539918.29005,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-120to170_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-170to300_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.654e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1797043.0,
                NEVT_UL16postVFP=1791497.0,
                NEVT_UL17=3631617.0,
                NEVT_UL18=3668140.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-170to300_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt-300toInf_EMEnriched" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.100e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=1118836.0,
                NEVT_UL16postVFP=1090760.0,
                NEVT_UL17=2158056.0,
                NEVT_UL18=2215994.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt-300toInf_EMEnriched_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_15to20_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=1.869e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=-1,
                NEVT_UL16postVFP=8265331.06524,
                NEVT_UL17=-1,
                NEVT_UL18=16182982.3804,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="", XmlSource_UL16preVFP="",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_15to20_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="", XmlSource_UL17="",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_15to20_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_15to20_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_20to30_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.055e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7913585.84161,
                NEVT_UL16postVFP=7164608.24167,
                NEVT_UL17=13974982.5352,
                NEVT_UL18=13965314.3132,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_20to30_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_30to80_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.612e+05, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7829691.54456,
                NEVT_UL16postVFP=7621532.16967,
                NEVT_UL17=14954896.9288,
                NEVT_UL18=15128473.4127,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_30to80_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_80to170_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=3.376e+04, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7690702.0,
                NEVT_UL16postVFP=7808513.0,
                NEVT_UL17=15312170.0,
                NEVT_UL18=14742089.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_80to170_bcToE_CP5_pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_Pt_170to250_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=2.127e+03, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=7343309.67453,
                NEVT_UL16postVFP=7723899.25939,
                NEVT_UL17=14990835.6594,
                NEVT_UL18=15407532.0851,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL17_v2.xml", XmlSource_UL17="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_170to250_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_Pt_250toInf_bcToE" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(XSec_13TeV=5.634e+02, XSecSource_13TeV="GenXSecAnalyzer run on UL18 (other years give same result within +/- O(0.1%))"),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=6856820.0,
                NEVT_UL16postVFP=8044441.0,
                NEVT_UL17=15487120.0,
                NEVT_UL18=15486264.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16APV_v2.xml", XmlSource_UL16preVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL16_v2.xml", XmlSource_UL16postVFP="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL17_v3.xml", XmlSource_UL17="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v3/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_Pt_250toInf_bcToE_CP5_pythia8_Summer20UL18_v3.xml", XmlSource_UL18="/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3/MINIAODSIM",
            ),
        },

        "QCD_HT50to100" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=185900000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=35729712.0,
                NEVT_UL16postVFP=11080132.0,
                NEVT_UL17=26032341.0,
                NEVT_UL18=38225118.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT50to100_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT50to100_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT100to200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=23610000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=65503645.0,
                NEVT_UL16postVFP=72640095.0,
                NEVT_UL17=53299606.0,
                NEVT_UL18=82213301.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT100to200_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT100to200_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT200to300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1551000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=17969592.0,
                NEVT_UL16postVFP=42723038.0,
                NEVT_UL17=42316128.0,
                NEVT_UL18=56298746.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT200to300_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT200to300_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT300to500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=324300, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13586390.0,
                NEVT_UL16postVFP=45502889.0,
                NEVT_UL17=42914024.0,
                NEVT_UL18=60991701.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT300to500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT300to500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT500to700" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=30340, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=55497082.0,
                NEVT_UL16postVFP=15066884.0,
                NEVT_UL17=35745565.0,
                NEVT_UL18=48640047.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT500to700_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT500to700_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT700to1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=6440, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=15242034.0,
                NEVT_UL16postVFP=13714842.0,
                NEVT_UL17=33646855.0,
                NEVT_UL18=47925782.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT700to1000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v2.xml", XmlSource_UL18="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
            ),
        },

        "QCD_HT1000to1500" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=1118, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=13559959.0,
                NEVT_UL16postVFP=12416669.0,
                NEVT_UL17=10136610.0,
                NEVT_UL18=14244456.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1000to1500_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1000to1500_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT1500to2000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=108, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=9661950.0,
                NEVT_UL16postVFP=9244228.0,
                NEVT_UL17=7528926.0,
                NEVT_UL18=10751607.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT1500to2000_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT1500to2000_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCD_HT2000toInf" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=22, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_UL16preVFP=4827641.0,
                NEVT_UL16postVFP=4843949.0,
                NEVT_UL17=4089387.0,
                NEVT_UL18=5278880.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_UL16preVFP="RunII_106X_v2/SM/UL16preVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16APV_v1.xml", XmlSource_UL16preVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",
                Xml_UL16postVFP="RunII_106X_v2/SM/UL16postVFP/QCD_HT2000toInf_CP5_PSWeights_madgraphMLM-pythia8_Summer20UL16_v1.xml", XmlSource_UL16postVFP="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM",
                Xml_UL17="RunII_106X_v2/SM/UL17/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL17_v1.xml", XmlSource_UL17="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM",
                Xml_UL18="RunII_106X_v2/SM/UL18/QCD_HT2000toInf_CP5_PSWeights_madgraph-pythia8_Summer20UL18_v1.xml", XmlSource_UL18="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM",
            ),
        },

        "QCDPT50to80" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=16760000, XSecSource_13TeV="GenXSecAnalyzer averaged over years" # 13p6 TeV!
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=21136440.0,
                NEVT_2022postEE=19940303.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-50to80_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT80to120" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=2517000, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=30781516.0,
                NEVT_2022postEE=40071820.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-80to120_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT120to170" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=442200, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=31356801.0,
                NEVT_2022postEE=40071820.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-120to170_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT170to300" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=113400, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=29860794.0,
                NEVT_2022postEE=41065808.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-170to300_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT300to470" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=7619, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=58535897.0,
                NEVT_2022postEE=80355820.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-300to470_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT470to600" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=625.1, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=28540568.0,
                NEVT_2022postEE=48417913.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-470to600_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT600to800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=179.7, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=75092875.0,
                NEVT_2022postEE=92473677.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_HT-600to800_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_HT-600to800_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT800to1000" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=30.71, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=43868300.0,
                NEVT_2022postEE=53572105.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_HT-800to1000_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_HT-800to1000_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT1000to1400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=8.944, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=22322802.0,
                NEVT_2022postEE=27675691.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_HT-1000to1400_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_HT-1000to1400_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT1400to1800" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.8096, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=7466758.0,
                NEVT_2022postEE=9974680.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-1400to1800_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT1800to2400" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.1151, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=3683361.0,
                NEVT_2022postEE=3683361.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-1800to2400_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT2400to3200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.007592, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=2158928.0,
                NEVT_2022postEE=2694345.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-2400to3200_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },

        "QCDPT3200" : {
            "CrossSection" : MCSampleValuesHelperPrototype.XSValues(
                XSec_13TeV=0.0002311, XSecSource_13TeV="GenXSecAnalyzer averaged over years"
            ),
            "NEvents" : MCSampleValuesHelperPrototype.NEventsValues(
                NEVT_2022preEE=864567.0,
                NEVT_2022postEE=1294987.0,
            ),
            "XMLname" : MCSampleValuesHelperPrototype.XMLValues(
                Xml_2022preEE="Run3_126X_v1/2022/QCD_PT-3200_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022preEE="/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
                Xml_2022postEE="Run3_126X_v1/2022/QCD_PT-3200_EE_TuneCP5_13p6TeV_pythia8.xml", XmlSource_2022postEE="/QCD_PT-3200_TuneCP5_13p6TeV_pythia8/Run3Summer22EEMiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM",
            ),
        },
    }

    def __init__(self, extra_dicts=None, import_signal=None):

        if extra_dicts is not None:
            if type(extra_dicts) == dict:
                self.__values_dict.update(extra_dicts)
            elif type(extra_dicts) == list:
                for ed in extra_dicts:
                    self.__values_dict.update(ed)

        if import_signal is not None:
            imported_dict = self._import_signal(import_signal)
            self.__values_dict = {**self.__values_dict, **imported_dict}

    def _import_signal(self, signal_name):
        spec = importlib.util.spec_from_file_location(
            "MCSignalValuesHelper",
            f"{CMSSW_BASE}/src/UHH2/common/UHH2-datasets/xsec_signal_dicts/{signal_name}.py"
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules["MCSignalHelper"] = module
        spec.loader.exec_module(module)
        return module.MCSignalValuesHelper.signal_values_dict

    def get_value(self, name, energy, year, key, strict=False, info = ""):
        """Return the value for a given MC sample, energy or year, and information type

        If information is stored for both an energy and a year, the value for the given energy will be preferentially returned.
        If strict checking is turned on the function will raise an error if a given dictionary or piece of information isn't found.
          Otherwise the default value will be returned with no error (i.e. will return 1.0 for kFactors)

        Args:
            name (`str`): The process name for a given MC sample
            energy (`str`): The simulated energy used during production of the MC sample
            year (`str`): The production year of the MC sample
            key (`str`): The type of information being requested. The Options can be found in the _key_field_map.
            strict (`bool`): Whether or not to perform strict checking of the dictionary

        """
        fields = [self._key_field_map[key][0]+info+"_"+energy,self._key_field_map[key][0]+info+"_"+year]
        if not name in self.__values_dict:
            raise KeyError("ERROR MCSampleValuesHelper::Unknown process \"" + str(name) + "\"")
        if not key in self.__values_dict[name]:
            if strict:
                print(self.__values_dict[name])
                raise KeyError("ERROR MCSampleValuesHelper::The process \"" + str(name) + "\" does not contain a " + str(key) + " tuple")
            else:
                return self._key_field_map[key][1]
        if not any(f in self.__values_dict[name][key]._fields for f in fields):
            if strict:
                print(self.__values_dict[name][key])
                raise KeyError("ERROR MCSampleValuesHelper::The " + str(key) + " tuple for process \"" + str(name) + "\" does contain the key(s) \"" + str(fields) + "\"")
            else:
                self._key_field_map[key][1]

        if self.__values_dict[name][key].__getattribute__(fields[0]) != self._key_field_map[key][1]:
            return self.__values_dict[name][key].__getattribute__(fields[0])
        else:
            return self.__values_dict[name][key].__getattribute__(fields[1])

    def get_xs(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "CrossSection", True, info)

    def get_nevt(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "NEvents", True, info)

    def get_br(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "BranchingRatio", False, info)

    def get_kfactor(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "kFactor", False, info)

    def get_corr(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "Correction", False, info)

    def get_xml(self, name, energy, year, info=""):
        return self.get_value(name, energy, year, "XMLname", False, info)

    def get_lumi(self, name, energy, year, kFactor=False, Corrections=False):
        xsec = self.get_xs(name, energy, year)
        xsec *= self.get_br(name, energy, year)
        if kFactor: xsec *= self.get_kfactor(name, energy, year)
        if Corrections: xsec *= self.get_corr(name, energy, year)
        return abs(self.get_nevt(name, energy, year))/xsec

def print_database(raise_errors=False):
    helper = MCSampleValuesHelper()
    samples = list(MCSampleValuesHelper.__dict__["_MCSampleValuesHelper__values_dict"].keys())
    samples.sort()
    energies = MCSampleValuesHelperPrototype.__dict__["_MCSampleValuesHelperPrototype__energies"]
    years = MCSampleValuesHelperPrototype.__dict__["_MCSampleValuesHelperPrototype__years"]
    import re
    run_pattern = re.compile("(?P<run>(Run)+[ABCDEFGH]{1})")

    max_sample_length = max(len(s) for s in samples)
    abspath_uhh2datasets = os.path.dirname(os.path.abspath(__file__))
    wrong_xmlpaths = []

    def banner(text, decorator = "#", line_width = 30):
        print("")
        print(decorator*line_width)
        print("{text:{deco}^{width}s}".format(text=text,deco=decorator,width=line_width))
        print(decorator*line_width)
        print("")

    for energy in energies:
        banner(energy)
        for year in years:
            banner(year)
            for sample in samples:
                run_match = run_pattern.search(sample)
                isData = run_match is not None
                nevt = helper.get_nevt(sample,energy,year)
                lumi = "/" if (isData or nevt<0) else "%10.2g"%helper.get_lumi(sample,energy,year)
                nevt = "%10.2g"%nevt
                line = '{sample: <{width}}-> nevt:{nevt: >5}, lumi:{lumi: >5}'.format(sample=sample, width=max_sample_length+3, nevt=nevt, lumi=lumi)
                xmlpath = helper.get_xml(sample,energy,year)
                xmlabspath = os.path.join(abspath_uhh2datasets, xmlpath)
                if xmlpath != "" and not os.path.isfile(xmlabspath):
                    line += " "*3+"Error: XML not found!"
                    wrong_xmlpaths.append(xmlpath)
                print(line)

    if len(wrong_xmlpaths) > 0:
        print("")
        print("Error: Cannot find the following XML file(s):")
        for xmlpath in wrong_xmlpaths:
            print(xmlpath)
        print("")
        if raise_errors: raise ValueError("One or multiple XML path(s) are invalid")
    return 0


if(__name__ == "__main__"):
    import argparse
    parser = argparse.ArgumentParser(description="CrossSectionHelper Database: find and calculate crucial information for your Analysis!")

    parser.add_argument("--print", action="store_true", help="print number of events and calculated luminosity of all samples in database (This is primarily to test the integrety of the database).")
    parser.add_argument("--throw", action="store_true", help="raise erros if they occur. Should be used together with --print option.")

    args = parser.parse_args()

    if(args.print):
        print_database(args.throw)
