# ----------------------------------------------------------------------
# -- RECO py template file for dumping the PixelTree only
# ----------------------------------------------------------------------

import os
import FWCore.ParameterSet.Config as cms
process = cms.Process("Demo")

# ----------------------------------------------------------------------
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append('HLTrigReport')
process.MessageLogger.categories.append('L1GtTrigReport')
process.options = cms.untracked.PSet( SkipEvent = cms.untracked.vstring('ProductNotFound'), wantSummary = cms.untracked.bool(True) )

# -- Database configuration
process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.load("CondCore.DBCommon.CondDBSetup_cfi")

# -- Conditions
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2018_design_v4', '')

# -- Input files
# POOLSOURCE

# -- Input files
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/F984AE43-81BB-924A-B609-D2E71471F135.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/F06B1CC1-4447-EB4B-8B5A-E8F004AC0C48.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/D5F18775-BB4D-A344-9920-D34B4A0C89A8.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/8F8A2BB9-A66C-6146-872B-92154E039CB9.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/882A401C-F2B9-9B44-BC93-1443307F359E.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/811A788B-30E0-5945-AC69-372EE9C8C764.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/66F378A5-9A08-B944-BFF6-8F73CD82477E.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/5AF605CB-B724-CF42-9E76-436B27BC9777.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/38253A92-BB14-0E4E-A34A-141F264562AF.root',
'/store/relval/CMSSW_10_4_0_pre2/RelValTTbar_13/GEN-SIM-RECO/PU25ns_103X_upgrade2018_design_v4-v1/10000/06AD71DD-7CA3-FE45-8331-2F175EB42C56.root',
	#"/store/relval/CMSSW_7_4_0/RelValSingleMuPt10_UP15/GEN-SIM-RECO/MCRUN2_74_V7_GENSIM_7_1_15-v1/00000/D04150EB-9DDD-E411-8E3D-002618943911.root"
    )
)
# -- number of events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(300)
    )

# -- Trajectory producer
process.load("RecoTracker.TrackProducer.TrackRefitters_cff")
process.TrackRefitter.src = 'generalTracks'
process.TrackRefitter.NavigationSchool = ""

# -- RecHit production
process.load("RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi")

# -- skimming
process.PixelFilter = cms.EDFilter(
    "SkimEvents",
    verbose                        = cms.untracked.int32(0),
    filterOnPrimaryVertex          = cms.untracked.int32(0),
    primaryVertexCollectionLabel   = cms.untracked.InputTag('offlinePrimaryVertices'),
    filterOnTracks                 = cms.untracked.int32(0),
    trackCollectionLabel           = cms.untracked.InputTag('generalTracks'),
    filterOnPixelCluster           = cms.untracked.int32(1),
    PixelClusterCollectionLabel    = cms.untracked.InputTag('siPixelClusters'),
    filterOnL1TechnicalTriggerBits = cms.untracked.int32(0),
    L1TechnicalTriggerBits         = cms.untracked.vint32(40, 41)
    )

# -- the tree filler
try:
    rootFileName = os.environ["JOB"] + ".root"
except KeyError:
    rootFileName = "pixelTree_MC.root"

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(
      rootFileName
      )
    )
process.PixelTree = cms.EDAnalyzer(
    "PixelTree",
    verbose                      = cms.untracked.int32(0),
    rootFileName                 = cms.untracked.string(rootFileName),
    #type                         = cms.untracked.string(getDataset(process.source.fileNames[0])),
    globalTag                    = process.GlobalTag.globaltag,
    dumpAllEvents                = cms.untracked.int32(0),
    PrimaryVertexCollectionLabel = cms.untracked.InputTag('offlinePrimaryVertices'),
    muonCollectionLabel          = cms.untracked.InputTag('muons'),
    trajectoryInputLabel         = cms.untracked.InputTag('TrackRefitter::Demo'),
    trackCollectionLabel         = cms.untracked.InputTag('generalTracks'),
    pixelClusterLabel            = cms.untracked.InputTag('siPixelClusters'),
    pixelRecHitLabel             = cms.untracked.InputTag('siPixelRecHits'),
    HLTProcessName               = cms.untracked.string('HLT'), 
    L1GTReadoutRecordLabel       = cms.untracked.InputTag('gtDigis'), 
    hltL1GtObjectMap             = cms.untracked.InputTag('hltL1GtObjectMap'), 
    HLTResultsLabel              = cms.untracked.InputTag('TriggerResults::HLT'),
    associatePixel = cms.bool(True),
    associateStrip = cms.bool(False),
    associateRecoTracks = cms.bool(False),
    ROUList = cms.vstring(
        'TrackerHitsPixelBarrelLowTof', 
        'TrackerHitsPixelBarrelHighTof', 
        'TrackerHitsPixelEndcapLowTof', 
        'TrackerHitsPixelEndcapHighTof'),
    pixelSimLinkSrc = cms.InputTag("simSiPixelDigis"),
    )

# -- Path
process.p = cms.Path(
#    process.PixelFilter*
    process.siPixelRecHits*
    process.TrackRefitter*
    process.PixelTree
    )
