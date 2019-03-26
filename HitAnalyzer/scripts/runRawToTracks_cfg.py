import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("MyRawToTracks",eras.Run2_2017)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load("Configuration.StandardSequences.Services_cff")

process.load('Configuration.EventContent.EventContent_cff')

process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

# needed for pixel RecHits (TkPixelCPERecord)
#process.load("Configuration.StandardSequences.Reconstruction_cff")

# clusterizer 
#process.load("RecoLocalTracker.Configuration.RecoLocalTracker_cff")


process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
# 2017
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v2' # fpr 90W 
#process.GlobalTag.globaltag = '92X_dataRun2_Express_v7' # from CMSSW927
# 2018
#process.GlobalTag.globaltag = '100X_dataRun2_Express_v2' # 
process.GlobalTag.globaltag = '101X_dataRun2_Express_v8' # 

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
# accept if 'path_1' succeeds
process.hltfilter = hlt.hltHighLevel.clone(
# Min-Bias
#    HLTPaths = ['HLT_Physics_v*'],  # not in ZB stream
#    HLTPaths = ['DST_Physics_v*'], useless 
#    HLTPaths = ['HLT_Random_v*'],
    HLTPaths = ['HLT_ZeroBias_v*'],
#    HLTPaths = ['HLT_ZeroBias*'],
#    HLTPaths = ['HLT_L1SingleMuOpen_v*'],
#    HLTPaths = ['HLT_L1Tech54_ZeroBias*'],
# Commissioning:
#    HLTPaths = ['HLT_L1_Interbunch_BSC_v*'],
#    HLTPaths = ['HLT_L1_PreCollisions_v1'],
#    HLTPaths = ['HLT_BeamGas_BSC_v*'],
#    HLTPaths = ['HLT_BeamGas_HF_v*'],
# LumiPixels
#    HLTPaths = ['AlCa_LumiPixels_Random_v*'],
#    HLTPaths = ['AlCa_LumiPixels_ZeroBias_v*'],
#    HLTPaths = ['AlCa_LumiPixels_v*'],
    
# examples
#    HLTPaths = ['p*'],
#    HLTPaths = ['path_?'],
    andOr = True,  # False = and, True=or
    throw = False
    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1))


myfilelist = cms.untracked.vstring()
myfilelist.extend([
])

process.source = cms.Source("PoolSource",
# fileNames =  myfilelist
#)
# fileNames =  cms.untracked.vstring('file:rawdata.root')

fileNames =  cms.untracked.vstring(
"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/22B731DE-EE83-E811-80A8-FA163E6B71E2.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/B6F4CC3D-F083-E811-A6AE-FA163E11300E.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/64839786-F083-E811-871D-FA163E2D815C.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/EA3E6685-F083-E811-BFCB-FA163E53585E.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/1055209E-F083-E811-A395-FA163EEF5766.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/DAB306B2-F083-E811-ABB2-FA163EEFE78F.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/9201F21A-F183-E811-A3F8-02163E017693.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/58E8628C-F383-E811-8118-FA163E4440F5.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/7A2F5892-F383-E811-9D87-FA163E75C6E8.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/984BE994-F383-E811-883B-FA163E6456FD.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/185DC666-F483-E811-B917-FA163E8DC37A.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/263618F4-F683-E811-95FF-FA163E8DC37A.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/00D919C3-F483-E811-9CEC-02163E012D22.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/B2BC8217-F783-E811-9376-FA163E014A3A.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/52154DEA-F783-E811-8685-FA163ECEE553.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/8E7579F9-F783-E811-A803-FA163E949BDE.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/D4FC3911-F883-E811-A2B2-FA163E77A6A7.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/228AD4F5-F783-E811-A584-FA163EFE4E9E.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/4E36121C-F883-E811-B22E-FA163EA6ABB6.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/50929FA3-F883-E811-885E-FA163E59DFFB.root",
#"/store/express/Run2018C/ExpressPhysics/FEVT/Express-v1/000/319/450/00000/BCE84922-F983-E811-A4A0-FA163E8561FE.root",

 )
#   skipEvents = cms.untracked.uint32(5000)
)

#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('303824:54-303824:999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('278193:77-278193:9999')
#process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange('302131:34-302131:943')

# for Raw2digi for data
process.siPixelDigis.InputLabel = 'rawDataCollector'
process.siStripDigis.ProductLabel = 'rawDataCollector'

#process.siPixelClustersPreSplitting.SeedThreshold = 1000
#process.siPixelClustersPreSplitting.ChannelThreshold = 2 #must be bigger than 1
#process.siPixelClustersPreSplitting.ClusterThreshold = 1000    # integer?
#process.siPixelClustersPreSplitting.ClusterThreshold_L1 = 1000 # integer?
#process.siPixelClustersPreSplitting.payloadType = cms.string('Full')


# for digi to clu
#process.siPixelClusters.src = 'siPixelDigis'

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('SiPixelClusterizer'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
#       threshold = cms.untracked.string('INFO')
#       threshold = cms.untracked.string('ERROR')
        threshold = cms.untracked.string('WARNING')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)


# pixel local reco (RecHits) needs the GenError object,
# not yet in GT, add here:
# DB stuff 
useLocalDB = False
if useLocalDB :
    process.DBReaderFrontier = cms.ESSource("PoolDBESSource",
     DBParameters = cms.PSet(
         messageLevel = cms.untracked.int32(0),
         authenticationPath = cms.untracked.string('')
     ),
     toGet = cms.VPSet(
       cms.PSet(
        record = cms.string('SiPixelGainCalibrationOfflineRcd'),
#        record = cms.string('SiPixelGainCalibrationRcd'),
        tag = cms.string('SiPixelGainCalibration_2018_v1_offline') #in DB
#        tag = cms.string('SiPixelGainCalibration_2017_v2_bugfix') #in DB
#        tag = cms.string('SiPixelGainCalibration_2017_v2_bugfix_offline')
#        tag = cms.string('SiPixelGainCalibration_2017_v2_offline')
#        tag = cms.string('SiPixelGainCalibration_2017_v3_offline')
#        tag = cms.string('SiPixelGainCalibration_2017_v4_offline')
#        tag = cms.string('SiPixelGainCalibration_2017_v5_offline') # v4 fixed
#        tag = cms.string('SiPixelGainCalibration_2017_v6_offline')
#        tag = cms.string('SiPixelGainCalibration_2017_v4')
#        tag = cms.string('SiPixelGainCalibration_2017_v5')
#        tag = cms.string('SiPixelGainCalibration_2017_v6') # full tag & in DB
#        tag = cms.string('SiPixelGainCalibration_2017_v4_1337_offline')
#        tag = cms.string('SiPixelGainCalibration_phase1_ideal_v2')
 	),
       ),
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v6_full.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v5_full.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v4_full.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v4_1337_offline.db')

#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v6_offline_oldvcalHL.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v6_offline.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v5_offline.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v4_offline.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v3_offline.db')
#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2017_v2_offline.db')
     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_2018_v1_offline.db')

#     connect = cms.string('sqlite_file:/afs/cern.ch/user/d/dkotlins/WORK/DB/Gains/SiPixelGainCalibration_phase1_ideal_v2.db')

#     connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
#     connect = cms.string('frontier://FrontierPrep/CMS_CONDITIONS')
    ) # end process
    process.myprefer = cms.ESPrefer("PoolDBESSource","DBReaderFrontier")
# end 


useLocalDBError = False
if useLocalDBError :
    process.DBReaderFrontier = cms.ESSource("PoolDBESSource",
     DBParameters = cms.PSet(
         messageLevel = cms.untracked.int32(0),
         authenticationPath = cms.untracked.string('')
     ),
     toGet = cms.VPSet(
       cms.PSet(
         record = cms.string('SiPixelGenErrorDBObjectRcd'),
# 	 tag = cms.string("SiPixelGenErrorDBObject38Tv1")
#        tag = cms.string('SiPixelGenErrorDBObject_38T_2012_IOV7_v1')
         tag = cms.string('SiPixelGenErrorDBObject_38T_v1_offline')
 	 ),
       ),
#     connect = cms.string('sqlite_file:siPixelGenErrors38T_2012_IOV7_v1.db')
#     connect = cms.string('frontier://FrontierProd/CMS_COND_31X_PIXEL')
#     connect = cms.string('frontier://FrontierPrep/CMS_COND_PIXEL')
     connect = cms.string('frontier://FrontierProd/CMS_COND_PIXEL_000')
    ) # end process
    process.myprefer = cms.ESPrefer("PoolDBESSource","DBReaderFrontier")
# end 



process.out = cms.OutputModule("PoolOutputModule",
    fileName =  cms.untracked.string('file:reco.root'),
#    fileName =  cms.untracked.string('file:/afs/cern.ch/work/d/dkotlins/public/data/tracks/tracks_1_0.root'),
    #outputCommands = cms.untracked.vstring("drop *","keep *_*_*_MyRawToClus") # 13.1MB per 10 events
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RECOEventContent.outputCommands,  # 4.9MB per 10 events 
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('RECO')
    )
)

process.d = cms.EDAnalyzer("PixClusterAna",
#process.d = cms.EDAnalyzer("PixClusterTest",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    #src = cms.InputTag("siPixelClusters"),
    src = cms.InputTag("siPixelClustersPreSplitting"),
    Tracks = cms.InputTag("generalTracks::MyRawToTracks"),
    Select1 = cms.untracked.int32(0),  # cut  
    Select2 = cms.untracked.int32(0),  # value     
)


process.c = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    src = cms.InputTag("generalTracks::MyRawToTracks"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),                             
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
)

process.c1 = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks::MyRawToTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(13),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(1),  # select the cut value   
)
process.c2 = cms.EDAnalyzer("PixClustersWithTracks",
    Verbosity = cms.untracked.bool(False),
    phase1 = cms.untracked.bool(True),
    src = cms.InputTag("generalTracks::MyRawToTracks"),
# for cosmics 
#    src = cms.InputTag("ctfWithMaterialTracksP5"),
#     PrimaryVertexLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
#     trajectoryInput = cms.string("TrackRefitterP5")
#     trajectoryInput = cms.string('cosmictrackfinderP5')
# additional selections
    Select1 = cms.untracked.int32(14),  # select the cut type, o no cut
    Select2 = cms.untracked.int32(1),  # select the cut value   
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('histo_tracks.root')
)


# copy the sequence below from  
# RecoTracker/IterativeTracking/python/iterativeTk_cff.py  - 71_pre7
process.myTracking = cms.Sequence(process.InitialStep*
                            process.DetachedTripletStep*
                            process.LowPtTripletStep*
                            process.PixelPairStep*
                            process.MixedTripletStep*
                            process.PixelLessStep*
                            process.TobTecStep*
                            process.earlyGeneralTracks*
                            # muonSeededStep*
                            process.preDuplicateMergingGeneralTracks*
                            process.generalTracksSequence*
                            process.ConvStep*
                            process.conversionStepTracks
                            )


#process.p = cms.Path(process.hltfilter*process.RawToDigi*process.reconstruction*process.c*process.c1*process.c2)
process.p = cms.Path(process.hltfilter*process.RawToDigi*process.reconstruction*process.c*process.d)

#process.ep = cms.EndPath(process.out)
